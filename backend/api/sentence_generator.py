from . import words as word_generator
import random

words = word_generator.generate(count=2000)


def generate(nSentences):
    """ Generate n random sentences with word count rangin from 3-20 inclusive """

    return [" ".join(random.sample(words, random.randrange(3, 21))) for _ in range(nSentences)]