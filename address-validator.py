import pytest

def validate_zip(zip_code):
    if len(zip_code) != 5:
        raise ValueError("Zip code must be exactly 5 characters long")
    if not zip_code.isdigit():
        raise ValueError("Zip code must only contain digits")
    return

def test_normal_zip():
    validate_zip("12345")

def test_empty_zip():
    with pytest.raises(ValueError):
        validate_zip("")

def test_short_zip():
    with pytest.raises(ValueError):
        validate_zip("1234")

def test_long_zip():
    with pytest.raises(ValueError):
        validate_zip("123456")

def test_alpha_zip():
    with pytest.raises(ValueError):
        validate_zip("1234e")
