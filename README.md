# python-library-template

[cookiecutter](https://github.com/audreyr/cookiecutter) template for a python library that
relies on docker-ci/docker-ci-python [TBD] for basic development activities.

## Install cookiecutter (if not installed)

    pip install cookiecutter

## Init Python project

    cookiecutter git@github.com:nephilim-solutions/python-library-template.git

## Working with the code

Requirements:

- unix*
- make
- docker 17+

Enter make help:

    cd %PROJECT%
    make

It might take a bit of time while Docker downloads the image for the first time.
Though since Alpine linux is used as a base it should not take too long.

## Magic

There is actually quite a bit of stuff that a single `make` command does
here for you:

1. Creates a docker container based on
   [docker-ci-python](https://hub.docker.com/r/nephilimsolutions/docker-ci-python/) image.
1. Installs all the requirements defined in `setup.yml`:
    - `install_requires`
    - `setup_requires`
    - `tests_require`
1. Runs pep8, pyflakes and pylint checks on your code (note: it is intentionally very strict)
1. Runs unit tests and docs tests and measures code coverage (fails if not 100%)
1. Produces a **wheel** package ready for publication to e.g a PyPi repo
    1. Takes all dependencies from `requirements.txt` - no need to worry about that
    1. Takes the version from `CHANGES` file (topmost line of the file is treated as such)
    1. Takes meta information from `setup.yml` and adds it to the distribution. The mapping
       between **yaml** fields and **setup** parameters is one to one.
       E.g. `author_email` is `author_email` not `author-email`.
       Supports `entry_points` definitions.
1. Produces code documentation (i.e. it parses the docstrings of all public modules):
    1. The documentation has **.rst** files in `gen-docs` folder thus you may produce documentation
       in other formats if you desire so.
    1. Readymade API documentation in HTML is built as well - thus you may publish it to external
       storage (e.g. GitHub pages). Open `gen-docs/html/index.html`
    1. All docstrings support inclusion of UML diagragms thanks to [plantuml](http://plantuml.com/)

One of the distinct features of `docker-ci` based toolchain is a complete build environment
isolation. This also applies to the way the toolchain caches all Python dependencies. Base
image has `ONBUILD` steps to install the dependencies `setup.yml` Thus as long as you don't
update those - you may be sure that you will not waste time refetching,
recompiling and reinstalling build and runtime dependencies.

`make` command executes `make all` behind the scenes. Which includes several steps that can
be executed independently on their own:

### clean

Remove all the previously produced build artifacts:

    make clean

### static-checks

Run pep8, pyflakes and pylint:

    make static-checks

### tests

Run unit tests:

    make tests

### build

Create a **wheel** package:

    make build

### build-docs

Generate code documentation both in **html** and **rst** format:

    make build-docs

### help

Show quick reference for the available make targets (with the exception of `update-base`)

    make help

## More magic

Apart from the toolchain mainly oriented for regular CI tasks there are extra commands to simplify
developer's work.

### repl

Run ipython inside a docker container with you repo mounted as a docker volume and available at
a python path:

    make repl

### connect

Connect to a terminal session inside a docker container to debug the build:

    make connect

### reformat

Reformat the code using [yapf](https://github.com/google/yapf)

    make reformat

### update-base

Update **docker-ci-python** image:

    make update-base

## Directory structure

The tool aim to eliminate most of the boilerplate actions and files when it comes to defining a
library. In order to do so it enforces a set of rules that need to be followed otherwise the
toolchain does not function correctly:

### setup.yml

All meta information must be in `setup.yml`. This is done to eliminate the need to include a
bunch of boilerplate imports for the `setup.py` file or face the limitations of `setup.cfg` file
such as inability to denote `entry_points`.

### requirements.txt

All runtime dependencies should go here. For the sake of build correctness do not put them to
`setup.yml`. Otherwise the toolchain will not be able to install those with `OBUILD` docker steps.

### requirements-dev.txt

Same as for `requirements.txt`. Keep development dependencies here. Not in `setup.yml`

### CHANGES

A changelog file with a minimalistic structure:

    MAJOR.MINOR.PATCH

        * Change description

Use [semantic version](https://semver.org/).

### tests/

All plain unit tests should go to this directory.

### %PACKAGE-NAME%

The library module itself should stay in the root of the repo. No `src` or `lib` directories are
supported.

*Flat is better than nested*
