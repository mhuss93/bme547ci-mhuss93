import pytest


@pytest.mark.parametrize("input, expected", [
    ("   !.tachycardia  ", "tachycardia"),
    (" TACHYCARDIA  ", "tachycardia"),
    ("TaChYc@rd1a...!   ", "tachyc@rd1a"),
    (".  Tachycardia .", "tachycardia"),
])
def test_simplify_string(input, expected):
    from tachycardia import simplify_string
    output = simplify_string(input)

    assert output == expected
