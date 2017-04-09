def is_isogram(phrase):
    isogram = True
    phrase = phrase.lower()

    for word in phrase:
        if phrase.count(word) > 1 and phrase.isalpha():
            isogram = False
            break

    return isogram
