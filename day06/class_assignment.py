import sys

text = "word and another word"
def count_number_of_each_word_using_default_dict(text):
    from collections import defaultdict
    words = text.split(" ")
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    return word_count
