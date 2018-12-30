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
│   └── single_package.py
├── tests
│   ├── test_helpers_single_package.py
│   └── test_single_package.py
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
│   │   ├── helpers_multiple.py
│   │   ├── __init__.py
│   │   └── multiple.py
│   ├── packages
│   │   ├── helpers_packages.py
│   │   ├── __init__.py
│   │   └── packages.py
│   ├── __init__.py
│   └── runner.py
├── tests
│   ├── multiple
│   │   ├── test_helpers_multiple.py
│   │   └── test_multiple.py
│   └── packages
│       ├── test_helpers_packages.py
│       └── test_packages.py
├── LICENSE
└── README.md
```

The `bin/` directory holds any executable files. Executables should not contain much code; instead, they should have an import and a call to the main function of the runner script.

The `docs/` directory holds documentation; ideally, we should have separate documentation for every internal sub-module.

The `data/` directory holds files that might be useful for testing. It is a location for files that the application will ingest or produce.
