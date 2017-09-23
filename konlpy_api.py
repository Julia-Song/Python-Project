#!__*__coding:utf-8__*__
from konlpy.tag import Twitter


class MyKonlpy(object):
    def __init__(self):
        self.t = Twitter()

    def get_nouns(self, text):
        result = self.t.nouns(text)
        return result


if __name__ == "__main__":
    test_text = "동해물과 백두산이 마르고 닳도록. 아버지가 방에 들어가신다. 오늘은 좋은 날씨입니다. 방에 먼지가 가득하네요."
    t = MyKonlpy()
    result = t.get_nouns(test_text)
    print(result)