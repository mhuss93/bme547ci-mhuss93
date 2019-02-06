import pytest


@pytest.mark.parametrize("input, expected", [
    ("   !.tachycardic  ", True),
    (" TACHYCARDIC  ", True),
    ("TaChYc@rd1c...!   ", False),
    (".  Tachycardic .", True),
    (". . . taCHycardic", True),
    ("tachycardc", False)
])
def test_is_tachycardic(input, expected):
    from tachycardia import is_tachycardic
    output = is_tachycardic(input)

    assert output == expected
