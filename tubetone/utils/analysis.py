from collections import Counter

import pymorphy2 as pymorphy2


def frequency(text_to_analyse):
    wordlist = text_to_analyse.split()

    morph = pymorphy2.MorphAnalyzer()

    normal_form_words = map(to_normal_form, wordlist)
    cntr = Counter(normal_form_words)

    for word in list(cntr):
        if is_crap_word(word):
            del cntr[word]
    # print(cntr.most_common(20))
    return cntr


def to_ascii(s):
    try:
        s = s.replace("'", '').replace("-", '').replace("|", '')
        return s.decode('utf-8').encode("ascii", errors="ignore").decode()
    except:
        return ''


def is_crap_word(s):
    return (is_functor(s) or is_too_common_word(s))


def is_asciiword(s):
    ascii_word = to_ascii(s)
    return len(ascii_word) > 2

def is_too_common_word(s):
    words_to_skip = {'быть', 'этот', 'тот', 'такой', 'какой-то', 'весь', 'который', 'раз'}
    return (s in words_to_skip)


def is_functor(s):
    functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP', 'NPRO', 'ADVB'}
    return (pos(s) in functors_pos)


def pos(word, morth=pymorphy2.MorphAnalyzer()):
    return morth.parse(word)[0].tag.POS

def to_normal_form(word, morph = pymorphy2.MorphAnalyzer()):
    return morph.parse(word)[0].normal_form
