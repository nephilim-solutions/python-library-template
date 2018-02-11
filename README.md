# python-library-template

[cookiecutter](https://github.com/audreyr/cookiecutter) template for a python-library that
relies on docker-ci/docker-ci-python [TBD] for basic development activities.

## Init Python project

    cookiecutter gh:nephilim-solutions/python-library

## Working with the code

Requirements:

- unix*
- make
- docker 17+

Enter make help:

    cd %PROJECT%
    make help

It might take a bit of time while Docker downloads the image for the first time.
Though since Alpine linux is used as a base it should not take too long.

Afterwards use `make help` output as a guide for your project work.
