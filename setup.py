import setuptools

setuptools.setup(
    name="pytest_bare_type_ignore",
    license="MIT",
    version="0.1.0",
    description="Pytest plugin that checks for bare `# type: ignore` comments",
    author="Ivan Tsouvarev",
    author_email="tsouvarev@mail.ru",
    url="https://github.com/tsouvarev/pytest-bare-type-ignore",
    py_modules=['pytest_bare_type_ignore'],
    install_requires=["pytest>5"],
    entry_points={
        'pytest11': [
            'bti = pytest_bare_type_ignore',
        ],
    },
    classifiers=[
        "Framework :: Pytest",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)