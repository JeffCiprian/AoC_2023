#WIP

import time
true_values = []

def convert_to_string(txt_files):
    file = open(txt_files)
    data = file.readlines()
    for line in data:
        grab_input_line(line)
    file.close()
    return()

def grab_input_line(calib_value):
    digit_list = []
    digit_position = []
    for position in range(len(calib_value)):
        if calib_value[position].isdigit() == True:
            digit_list += digit_list
            digit_position = position
    return(first_and_last(new_list))

def first_and_last(num_list):
    true_values.append(num_list[0] + num_list[-1])
    return()

def process_true_values(values_list):
    final_value = 0
    for num in values_list:
        final_value += int(num)
    return(final_value)

start = time.perf_counter()

path_to_file = 'Dec01_Input.txt'

convert_to_string(path_to_file)
print(process_true_values(true_values))
end = time.perf_counter()
print(end - start)

#Need to read the line to see if one etc. are present
#convert the words into the number it represents

