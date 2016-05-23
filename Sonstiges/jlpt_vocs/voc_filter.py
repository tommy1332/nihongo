#!/usr/bin/python3

import sys
import re

# arg1 = gyou n ∈ {0,1,...,10}
# arg2 = dakuten (Y/N)
# arg3 = maximale JLPT-Level
# hiragana katakana offset: 96

arg_count = len(sys.argv)
if arg_count != 5:
  exit()

gyou = int(sys.argv[1])
dakuten = sys.argv[2]
level = int(sys.argv[3])
output = sys.argv[4]

# indeces 0-10 (but off by one)
kana_list = ["あいうえお", "かきくけこ:がぎぐげご", "さしすせそ:ざじずぜぞ", "たちつてと:だぢづでど", "なにぬねの", "はひふへほ:ばびぶべぼぱぴぷぺぽ", "まみむめも", "やゆよ", "らりるれろ", "わをん", "っゃゅょー"]

kana_list = kana_list[:gyou]
chars = "" # string containing allowed chars
for elem in kana_list:
  if not (dakuten == "Y" or dakuten == "y" or dakuten == "yes"):
    if ":" in elem:
      elem = elem[:5]
  chars += elem

vocab_list = []
reading_list = []
kanji_list = []

re_in_bracket = re.compile("\(([^\)]*)\)")
re_kana_word = re.compile("([^:]*)")

for i in range(5, level - 1, -1):
  filename = "n" + str(i) + ".txt"
  with open(filename) as f:
    for line in f:
      # extract reading
      if "): " in line:
        reading = re_in_bracket.search(line).groups(1)[0]
      else:
        reading = re_kana_word.search(line).groups(1)[0]
      if all((char in chars) for char in reading):
        vocab_list.append(line)
        reading_list.append(reading)
        # append kanji + reading
        kanji_list.append(re_kana_word.search(line).groups(1)[0])

if output == "r" or output == "reading":
  for elem in reading_list:
    print(elem)
elif output == "v" or output == "vocab":
  for elem in vocab_list:
    print(elem)
elif output == "k" or output == "kanji":
  for elem in kanji_list:
    print(elem)
