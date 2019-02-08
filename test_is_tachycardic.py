import pytest


@pytest.mark.parametrize("input, expected", [
    ("   !.tachycardic  ", True),
    (" TACHYCARDIC  ", True),
    ("TaChYc@rd1c...!   ", True),
    (".  Tachycardic .", True),
    (". . . taCHycardic", True),
    ("tachycardc", True),
    ("   .thycardc", False),
    ("Taaachyccardic", False),
])
def test_is_tachycardic(input, expected):
    from tachycardia import is_tachycardic
    output = is_tachycardic(input)

    assert output == expected
