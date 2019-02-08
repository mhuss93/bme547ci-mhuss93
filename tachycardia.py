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


def levenshtein_distance(s, t, costs=(1, 1, 1)):
    """ Computes the levenshtein distance between strings s and t.

        The Levenshtein distance computes a difference between two
        strings based on the number of deletions, insertions, and/or
        substitutions required to transform one to the other and the
        costs associated with each of these transformations.

        costs: a tuple or a list with three integers (d, i, s)
               where d defines the costs for a deletion
                     i defines the costs for an insertion and
                     s defines the costs for a substitution

        This implementation is found here:
        https://www.python-course.eu/levenshtein_distance.php
    """
    rows = len(s)+1
    cols = len(t)+1
    deletes, inserts, substitutes = costs

    dist = [[0 for x in range(cols)] for x in range(rows)]
    # source prefixes can be transformed into empty strings
    # by deletions:
    for row in range(1, rows):
        dist[row][0] = row * deletes
    # target prefixes can be created from an empty source string
    # by inserting the characters
    for col in range(1, cols):
        dist[0][col] = col * inserts

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = substitutes
            dist[row][col] = min(dist[row-1][col] + deletes,
                                 dist[row][col-1] + inserts,
                                 dist[row-1][col-1] + cost)  # substitution
    for r in range(rows):
        print(dist[r])

    return dist[row][col]
