#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: test_sequence_functions.py
@time: 2016/10/13 21:36
"""

import random
import unittest_example


class TestSequenceFunctions(unittest_example.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        """make sure the shuffled sequence does not lose any elements"""
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        self.assertEqual(self.seq, range(5)) #case不能通过

        """should raise an exception for an immutable sequence"""
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


if __name__ == '__main__':
    unittest_example.main()
