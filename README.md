# bme547ci-mhuss93

`is_tachycardic` initially strips leading and trailing whitespace and punctuation from the input string and converts the resulting string to lowercase.

The Levenshtein distance is then calculated between the resulting string and "tachycardic". This counts the number of insertions, deletions, and/or substitutions required to convert the input string to "tachycardic". If the answer is 2 or less, the function returns `True`, otherwise it returns `False`.