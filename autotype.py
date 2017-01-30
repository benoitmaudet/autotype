#!/usr/bin/env python

# title           :autoType.py
# description     :This script auto type a string or text.
# author          :Benoit MAUDET
# date            :20170130
# version         :0.1
# usage           :python autoType.py
# note            :keyboard layout must be qwerty

# https://pyautogui.readthedocs.io
import pyautogui
import time
import argparse
import os.path

parser = argparse.ArgumentParser(description='Auto type string or file')
parser.add_argument('string', help='auto type string')

args = parser.parse_args()

TEMPO = 2
time.sleep(TEMPO)

if not os.path.isfile(args.string):
    charList = list(args.string)
else:
    fileToRead = open(args.string)
    charList = list(fileToRead.read())

for char in charList:
    pyautogui.press(char)
