#!/usr/bin/env python3

from typing import ForwardRef
import unittest
from start import Advent1
from start import Advent2
from start import Advent3

class Test1(unittest.TestCase):
  def test_count_increases(self):
    TEST_INPUT = [
      199,
      200,
      208,
      210,
      200,
      207,
      240,
      269,
      260,
      263]
    
    a1 = Advent1()
    self.assertEqual(a1.count_increases(TEST_INPUT), 7)

class Test2(unittest.TestCase):
  def test_parse_input(self):
    TEST_INPUT = [
      "forward 5",
      "down 5",
      "forward 8",
      "up 3",
      "down 8",
      "forward 2"
    ]

    a2 = Advent2()
    parsed_input = a2.parse_input(TEST_INPUT)
    self.assertEqual(len(parsed_input), 6)
    self.assertEqual(parsed_input[5][0], a2.FORWARD)
    self.assertEqual(parsed_input[5][1], 2)

    (h, d) = a2.follow_path(parsed_input)
    self.assertEqual(h, 15)
    self.assertEqual(d, 10)

    (h2, d2) = a2.follow_path_2(parsed_input)
    self.assertEqual(h2, 15)
    self.assertEqual(d2, 60)

class Test3(unittest.TestCase):
  def test_compute_gamma_epsilon(self):
    TEST_INPUT = [
      "00100",
      "11110",
      "10110",
      "10111",
      "10101",
      "01111",
      "00111",
      "11100",
      "10000",
      "11001",
      "00010",
      "01010" 
    ]

    a3 = Advent3()
    (gamma, epsilon) = a3.compute_gamma_epsilon(TEST_INPUT)

    self.assertEqual(gamma, 22)
    self.assertEqual(epsilon, 9)


if __name__ == '__main__':
  unittest.main()
