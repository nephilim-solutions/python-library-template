from {{cookiecutter.python_name}}.app import get_some_magic


def test_the_magic():
    assert get_some_magic() == "Magic!!"
