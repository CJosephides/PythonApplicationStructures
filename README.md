# Python Application Structure

These are templates for building Python applications at various levels of complexity.

Many of the ideas here have been adapted from [Real Python: Python Application Layouts](https://realpython.com/python-application-layouts/).

Note: for simplicity, I have omitted the `env` and `.git` directories from the example directory structures shown below.

## Simple Command Line Interface Application

```
SimpleCLI/
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── simple_cli.py
└── tests.py
```

## Single Package Application

```
SinglePackage/
├── single_package
│   ├── helpers_single_package.py
│   ├── __init__.py
│   └── single.py
├── tests
│   ├── test_helpers_single_package.py
│   └── test_single.py
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

## Multiple (Internal) Package Application

```
MultiplePackages/
├── bin
├── data
│   ├── input.csv
│   └── output.xlsx
├── docs
│   ├── multiple.md
│   └── packages.md
├── multiple_packages
│   ├── multiple
│   ├── packages
│   ├── __init__.py
│   └── runner.py
├── tests
│   ├── multiple
│   └── packages
├── LICENSE
└── README.md
```

The `bin/` directory holds any executable files. Executables should not contain much code; instead, they should have an import and a call to the main function of the runner script.

The `docs/` directory holds documentation; ideally, we should have separate documentation for every internal sub-module.

The `data/` directory holds files that might be useful for testing. It is a location for files that the application will ingest or produce.

## Notes

### Naming

It may be better to avoid using the same name for a package and either a sub-package or module. I have found it difficult to get some `__init__.py` imports to behave properly when there are naming conflicts like these.

