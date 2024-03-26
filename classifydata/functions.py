#!/usr/bin/python3

def copy_lines(input_file_name, output_file_name, keywords):
    with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
        lines = input_file.readlines()
        for i in range(len(lines)):
            line = lines[i]
            for word in keywords:
                if word in line:
                    if i+2 < len(lines):  # Ensure there are next two lines available
                        next_line1 = lines[i+1]
                        next_line2 = lines[i+2]
                        output_file.write(word + '\n')  # Write the keyword
                        output_file.write(next_line1)  # Write the next line
                        output_file.write(next_line2)  # Write the next line

def create_keygroups(inputkeyfile):
    keyword_group = []
    with open(inputkeyfile, 'r') as inputkey:
        for line in inputkey:
            lineclean = line.strip()  # Use strip() to remove newline characters
            keyword_group.append(lineclean)
    return keyword_group