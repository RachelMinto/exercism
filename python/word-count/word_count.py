# -*- coding: utf-8 -*-
import re

def word_count(phrase):
    word_count = {}

    words = normalize(phrase).split(' ')

    for word in words:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

def normalize(phrase):
    phrase = re.sub('[\n\t_,]',' ', phrase)        
    phrase = re.sub('[^\w\s]', '', phrase)
    phrase = re.sub(' +',' ', phrase)

    # phrase = words.lower();
    return phrase.lower();