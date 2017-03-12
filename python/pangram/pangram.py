import re

def is_pangram(phrase):
    normalized_phrase = re.sub(r'[^a-z]', '', phrase.lower())
    phrase_ascii_chars = get_ascii(set(list(normalized_phrase)))
    phrase_ascii_chars.sort() 
    return phrase_ascii_chars == (range(97, 123))

def get_ascii(characters):
    return list(map(lambda x: ord(x), characters))

