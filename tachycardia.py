def simplify_string(s):
    """ Removes trailing punctuation and whitespace from single word string and
    converts to lower case

    :param s: single word string
    :return: lowercase string with trailing punctuation and whitespace removed
    """
    from string import punctuation
    simplified_string = s.replace(' ', '').strip(punctuation).lower()
    return simplified_string


def is_tachycardic(s):
    """ Check if single word string contains 'tachycardic'

    :param s: single word string
    :return: boolean
    """
    simp_s = simplify_string(s)
    return simp_s == "tachycardic"
