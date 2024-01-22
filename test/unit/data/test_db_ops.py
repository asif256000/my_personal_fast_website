import pytest

from src.data import db_ops


def test_snake_to_camel_case():
    assert db_ops.snake_to_camel_case("hello_world") == "HelloWorld"
