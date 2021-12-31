#!/usr/bin/env python3

import os
from typing import ForwardRef

# Global utilities
def read_file_into_list(file_name):
  with open(file_name) as f:
    lines = f.read().splitlines()
  return lines

def strings_to_list_of_ints(string_list):
  int_list = [int(l) for l in string_list]
  return int_list

def pp(index, answer):
  print("\nAdvent %d answer: %s\n" % (index, str(answer)))

class Advent1:
  def count_increases(self, int_list):
    increase_count = 0
    prev = int_list[0]
    for i in int_list[1:]:
      if i > prev:
        increase_count += 1
      prev = i
    return increase_count

  def run(self):
    input_int_list = strings_to_list_of_ints(read_file_into_list("input1.txt"))
    return self.count_increases(input_int_list)


class Advent2:
  FORWARD = 0
  UP = 1
  DOWN = 2

  def parse_input(self, input_lines):
    inputs = []
    
    for l in input_lines:
      line_items = l.split()
      assert(len(line_items) == 2)
      assert(line_items[1].isnumeric())

      direction = -1
      if line_items[0] == "forward":
        direction = self.FORWARD
      elif line_items[0] == "down":
        direction = self.DOWN
      elif line_items[0] == "up":
        direction = self.UP
      else:
        raise AssertionError("Invalid input.")

      inputs.append((direction, int(line_items[1])))

    return inputs

  def follow_path(self, inputs):
    horizontal_pos = 0
    depth = 0
    for i in inputs:
      if i[0] == self.FORWARD:
        horizontal_pos += i[1]
      elif i[0] == self.DOWN:
        depth += i[1]
      elif i[0] == self.UP:
        depth -= i[1]
    
    return (horizontal_pos, depth)

  def follow_path_2(self, inputs):
    horizontal_pos = 0
    depth = 0
    aim = 0

    for i in inputs:
      if i[0] == self.FORWARD:
        horizontal_pos += i[1]
        depth += aim * i[1]
      elif i[0] == self.DOWN:
        aim += i[1]
      elif i[0] == self.UP:
        aim -= i[1]
    
    return (horizontal_pos, depth)

  def run(self):
    input_lines = read_file_into_list("input2.txt")
    inputs = self.parse_input(input_lines)

    (h, d) = self.follow_path(inputs)
    (h2, d2) = self.follow_path_2(inputs)
    return (h * d, h2 * d2)


class Advent3:
  def parse_input_to_ints(self, lines):
    # This might not be needed actually..
    parsed_input = []
    for l in lines:
      assert(l.isnumeric())
      parsed_input.append(int(l, 2))
    return parsed_input

  def compute_gamma_epsilon(self, string_list):
    input_length = len(string_list)
    assert(input_length)
    input_width = len(string_list[0])
    assert(input_width)
    
    bit_counts = [0 for i in range(0,input_width)]
    for l in string_list:
      for c in range(0, input_width):
        if l[c] == '1':
          bit_counts[c] += 1
    
    threshold = input_length / 2
    gamma = 0
    epsilon = 0
    for count in bit_counts:
      if count > threshold:
        gamma += 1
      else:
        epsilon += 1
      
      gamma = gamma << 1
      epsilon = epsilon << 1
    
    # last iteration overshoots, shift back
    gamma = gamma >> 1
    epsilon = epsilon >> 1

    return (gamma, epsilon)

  def run(self):
    input = read_file_into_list("input3.txt")
    (gamma, epsilon) = self.compute_gamma_epsilon(input)  
    return gamma * epsilon

if __name__ == "__main__":
  os.chdir(os.path.dirname(__file__))
  
  pp(1, Advent1().run())
  pp(2, Advent2().run())
  pp(3, Advent3().run())