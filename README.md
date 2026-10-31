# Python's PHP Standard Recommendations

-------------

[![CI](https://github.com/alex-kalanis/pypsr/actions/workflows/ci.yml/badge.svg)](https://github.com/alex-kalanis/pypsr/actions/workflows/ci.yml)
![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)
![Dependencies: none](https://img.shields.io/badge/dependencies-none-brightgreen)

Port of [PHP Standard Recommendations](https://www.php-fig.org/psr/) to Python

This project contain basic port of implementations
of PHP's interfaces for sharing across the projects.
These interfaces are necessary for interoperability
across the libraries.

It contains just subset of classes - not everything
is need in Python (like coding style). Some of them
also contain a basic implementation.

| Number | About what                  | Available in |
|--------|-----------------------------|--------------|
| 1      | Basic Coding Standard       | -            |
| 3      | Logger Interface            | logger       |
| 4      | Autoloading Standard        | -            |
| 6      | Caching Interface           | cache        |
| 7      | HTTP Message Interface      | http         |
| 11     | Container Interface         | container    |
| 12     | Extended Coding Style Guide | -            |
| 13     | Hypermedia Links            | link         |
| 14     | Event Dispatcher            | dispatcher   |
| 15     | HTTP Handlers               | http         |
| 16     | Simple Cache                | simple_cache |
| 17     | HTTP Factories              | http         |
| 18     | HTTP Client                 | http         |
| 20     | Clock                       | clock        |

## Install

Full package, no extra dependencies, Python 3.9+. Use your
environment and `pip` down there:

```sh
pip install pypsr          # from PyPI
# or straight from source:
pip install git+https://github.com/alex-kalanis/pypsr
```

Then you can make the implementations of desired parts
or say that your project expects another packages which
provides implementations defined by these interfaces.

## Why this package

Python also has more ways to do things - like PHP. And
the Author needs to have some of these interfaces across
the multiple projects. And the basic setting is already
good thanks to the work of PHP-FIG. It just needs to be
ported, updated a bit and expect things the pythonic way. 

## Tests

```bash
python -m pytest
```

The package itself has no dependencies. Because it's
mainly about interfaces.

## Sources

- [PHP Standard Recommendations](https://www.php-fig.org/psr/)
