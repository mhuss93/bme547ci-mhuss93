import pytest


@pytest.mark.parametrize("s, t, expected", [
    ("tachycardic", "tachycardic", 0),
    ("t@chycardic", "tachycardic", 1),
    ("tachycardic", "tachycard1c", 1),
    ("tachycrdic", "tachycardc", 2),
    ("abc", "xyzz", 4),
])
def test_is_tachycardic(s, t, expected):
    from tachycardia import levenshtein_distance
    output = levenshtein_distance(s, t)

    assert output == expected
