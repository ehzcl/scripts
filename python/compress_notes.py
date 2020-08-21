# convert multiple files in a single one
# author: Ewerton Lima
# date: 2020-07-13
# This script function is to store multiple notes on a single file for 
# places like Pastebin, which gives you limited amount of unlisted notes for free

# This script uses the following format
# each line starts with the name of the note followed by ':'
# ';' is used to represent newlines (so it's not for source code)
 
import os

files = os.popen(f"ls *.txt").read().split('\n')

if '' in files:
    files.remove('')

output_filename = input("Output file: ")
if output_filename == "":
    output_filename = "out.txt"

out_file = open(output_filename,"a")

for f in files:
     tmp_file = open(f, "r")
     filename = f[:-4]
     file_content = tmp_file.read()
     file_content = file_content.replace('\n', ';')
     out_string = filename + ":" + file_content + '\n'
     out_file.write(out_string)
     tmp_file.close()

out_file.close()

