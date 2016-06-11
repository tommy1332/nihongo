# Berechnet den Zeilenweise Schnitt zweier Textdateien
import sys

if len(sys.argv) != 3:
  print("Wrong number of arguments")
  print("Usage: python3 intersection.py file1.txt file2.txt")
  exit()

lines = set()
with open(sys.argv[1]) as f:
  for line in f:
    lines.add(line.strip())

with open(sys.argv[2]) as f:
  for line in [line.strip() for line in f]:
    if line in lines:
      print(line)
