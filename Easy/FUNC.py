# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:44:50 2018

@author: 599798
"""

def handle_one():
  print("one")

def handle_two():
  print("two")

def handle_three():
  print("three")

def try1(option):
    {'one': handle_one, 
     'two': handle_two, 
     'three': handle_three}[option]()
try1('one')
