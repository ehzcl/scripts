# extract notes from a single file
# author: Ewerton Lima
# date: 2020-08-13
# This script receives a file with the format of
# compress_notes.py and returns the files to it's original
# content


from sys import argv

if len(argv) == 2:
    input_filename = argv[1]    
else:
    input_filename = input("Please enter the name of the file to generate notes\n")

input_file = open(input_filename + '.txt', 'r')

for line in input_file:
    first_colon = line.index(':')

    output_filename = line[0:first_colon]
    
    output_file_content = line[first_colon + 1:]

    output_file = open(output_filename + '.txt', 'w')
    
    out_content = output_file_content.rstrip('\n')
    out_content = out_content.rsplit(';')

    for i in out_content:
        output_file.write(i + '\n')

    output_file.close()

input_file.close()
