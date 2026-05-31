from googletrans  import Translator, constants
import time
import re
import argparse

# date: 2022-12-22 

translator = Translator()

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--start", help = "Starting line")
parser.add_argument("-s", "--source", help = "input file")
parser.add_argument("-t", "--target", help = "target file")
parser.add_argument("-tl", "--targetlang", help = "target language")
args = parser.parse_args()


subtitle = open(args.source,'r')
translation = open(args.target,'a')

if args.start:
    for _ in range(int(args.start)):
        next(subtitle)

for line in subtitle:
    # ignoring timestamps, numbering and blanklines
    if re.search("^$", line) or re.search("^[0-9\:\->, ]+$",line):
        translation.write(line)
        continue

    a = translator.translate(line, dest=args.targetlang)
    translation.write(a.text+"\n")
    time.sleep(3)

subtitle.close()
translation.close()
