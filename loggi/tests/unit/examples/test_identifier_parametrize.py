from examples.identifier import Identifier
import pytest


def test_case_00():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('a')

    assert is_valid is True


def test_case_01():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('ab')

    assert is_valid is True


def test_case_02():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('abcde')

    assert is_valid is True


def test_case_03():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('abcdef')

    assert is_valid is True


def test_case_04():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('abcdefg')

    assert is_valid is False


def test_valid_cases():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('abcdef')

    assert is_valid is True

@pytest.mark.parametrize('idn', [
    'a',
    'A',
    'z',
    'Z',
    'aZ',
    'az',
    'aA',
    'aa',
    'a0',
    'a1',
    'a8',
    'a9'
])
def test_case_06(idn):
    identifier = Identifier()

    assert identifier.validate_identifier(idn)
