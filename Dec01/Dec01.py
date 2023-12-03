true_values = []

def convert_to_string(txt_files):
    file = open(txt_files)
    data = file.readlines()
    for line in data:
        grab_input_line(line)
    file.close()
    return()

def grab_input_line(calib_value):
    new_list = []
    for character in calib_value:
        if character.isdigit() == True:
            new_list += character
    return(first_and_last(new_list))

def first_and_last(num_list):
    true_values.append(num_list[0] + num_list[-1])
    return()

def process_true_values(values_list):
    final_value = 0
    for num in values_list:
        final_value += int(num)
    return(final_value)

path_to_file = 'Dec01_Input.txt'
convert_to_string(path_to_file)
print(process_true_values(true_values))