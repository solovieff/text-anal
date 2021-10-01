import pprint
from unittest import TestCase

from analysis import get_tone, frequency

bad = "Демон очень плохой демон плохой демон хуже человека"
neutral = "Человек бывает разный человек не плохой и не хороший человек не лучше человека"
good = "Ангел очень хороший ангел не плохой ангел лучше человека"


class TestAnalysis(TestCase):
    def test_frequency(self):
        text = bad + good + neutral

        counter = frequency(text)
        print(counter.most_common(2))

    def test_tone(self):
        lst = [bad, good, neutral]
        for text in lst:
            tone_result = get_tone(text * 10)
            pprint.pprint("====")
            pprint.pprint(text)
            pprint.pprint(tone_result)
