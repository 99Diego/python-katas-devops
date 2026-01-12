def nth_char(words: list[str]) -> str:
    result = ""

    for index, word in enumerate(words):
        result += word[index]

    return result
