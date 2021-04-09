import ast

from typing import List

import pytest


def pytest_configure(config):
    config.pluginmanager.register(BTIPlugin())


class BTIError(Exception):
    pass


class BTIPlugin:
    def pytest_collect_file(self, path, parent):
        if path.strpath.endswith('.py'):
            return BTIFile.from_parent(parent, fspath=path)


class BTIFile(pytest.File):
    def collect(self):
        return [BTIItem.from_parent(self, name="bare-type-ignore")]


class BTIItem(pytest.Item):
    def runtest(self):
        errors = list(self._check_file(self.fspath))
        if errors:
            raise BTIError('\n'.join(errors))

    def repr_failure(self, excinfo, style=None):
        if excinfo.errisinstance(BTIError):
            return excinfo.value.args[0]
        return super().repr_failure(excinfo)

    def _check_file(self, path):
        tree = ast.parse(path.read(), type_comments=True)

        visitor = Visitor()
        visitor.visit(tree)

        yield from visitor.errors


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors: List[str] = []

    def visit_TypeIgnore(self, node: ast.TypeIgnore) -> None:
        if not node.tag:
            self.errors.append(f"Line {node.lineno}: '#type: ignore' without tag")
        self.generic_visit(node)
