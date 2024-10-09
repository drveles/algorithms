import unittest
# from collections import deque
from bisect import bisect_left


class HitCounter:
    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        return len(self.hits) - bisect_left(self.hits, timestamp - 300)

class TestHitCounter(unittest.TestCase):
    def test_single_hit(self):
        counter = HitCounter()
        counter.hit(1)
        self.assertEqual(counter.getHits(1), 1)   # Один удар на 1-й секунде
        self.assertEqual(counter.getHits(2), 1)   # Все еще один удар на 2-й секунде

    def test_multiple_hits(self):
        counter = HitCounter()
        counter.hit(1)
        counter.hit(2)
        counter.hit(3)
        self.assertEqual(counter.getHits(4), 3)   # Три удара на 1, 2 и 3-й секунде

    def test_expired_hits(self):
        counter = HitCounter()
        counter.hit(1)
        counter.hit(100)
        counter.hit(200)
        counter.hit(300)
        counter.hit(301)
        self.assertEqual(counter.getHits(301), 4)  # Удары на 1, 100, 200, 300 остаются
        self.assertEqual(counter.getHits(600), 1)  # Удар на 301-й секунде остается


    def test_no_hits(self):
        counter = HitCounter()
        self.assertEqual(counter.getHits(1), 0)    # Нет ударов

    def test_hits_on_boundary(self):
        counter = HitCounter()
        counter.hit(1)
        counter.hit(300)
        self.assertEqual(counter.getHits(300), 2)  # Два удара (1 и 300)
        self.assertEqual(counter.getHits(301), 1)  # Удар на 1-й секунде выходит за границу, остается только удар на 300-й секунде


if __name__ == '__main__':
    unittest.main()