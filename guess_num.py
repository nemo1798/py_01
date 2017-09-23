#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@file: guess_num.py.py
@time: 9/23/17 1:37 PM
"""
import random

num = random.randint(1, 9999)

guess_num = int(raw_input("\nInput one number(1~9999):"))

while guess_num != num:
    if  guess_num > num:
      print "Sorry, It's Higher\n"
      guess_num = int(raw_input("\nInput one number(1~9999):"))
    if guess_num < num:
      print "Sorry, It's Lower\n"
      guess_num = int(raw_input("\nInput one number(1~9999):"))
    if guess_num == num:
      print "That's Right!"
      break;
print "Game will exit..."