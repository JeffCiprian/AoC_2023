def read_file(txt_file):
    file = open(txt_file)
    data = file.readlines()
    file.close()
    return(data)

path = 'Dec03/Dec03_Sample.txt'
data = read_file(path)
special_chars = ['@', '#', '$', '%', '/', '*', '+']
product_list = []

def right_horizontal_check(symbol_location, line_schematics):
    num = ''
    if line_schematics[symbol_location+1].isdigit():
        if line_schematics[symbol_location+2].isdigit():
            if line_schematics[symbol_location+3].isdigit():
                num = line_schematics[symbol_location+1] + line_schematics[symbol_location+2] + line_schematics[symbol_location+3]
            else:
                num = line_schematics[symbol_location+1] + line_schematics[symbol_location+2]
        else:
            num = line_schematics[symbol_location+1]
        return(product_list.append(int(num)))
    
def left_horizontal_check(symbol_location, line_schematics):
    num = ''
    if line_schematics[symbol_location-1].isdigit():
            if line_schematics[symbol_location-2].isdigit():
                if line_schematics[symbol_location-3].isdigit():
                    num = line_schematics[symbol_location-3] + line_schematics[symbol_location-2] + line_schematics[symbol_location-1]
                else:
                    num = line_schematics[symbol_location-2] + line_schematics[symbol_location-1]
            else:
                num = line_schematics[symbol_location-1]
            return(product_list.append(int(num)))
    else:
        pass

def lower_horizontal_check(symbol_index, lower_line_schematics):
    clean_line = lower_line_schematics.strip()
    line_length = len(clean_line)
    iterator = symbol_index - 1
    num = lower_line_schematics[symbol_index] if lower_line_schematics[symbol_index].isdigit() else ''
    while iterator >= 0:
        if lower_line_schematics[iterator].isdigit():
            num = lower_line_schematics[iterator] + num
        elif iterator == symbol_index - 1:
            break
        iterator -= 1
    
    iterator = symbol_index + 1
    while iterator < line_length:
        if lower_line_schematics[iterator].isdigit():
            num += lower_line_schematics[iterator]
        elif iterator == symbol_index + 1:
            break
        iterator += 1
    return(num)

    
    #if line_length >= 
    #for n in lower_line_schematics[symbol_location-3:lower_line_schematics+3]:
        #if n.isdigit():
            #num += 

    # if lower_line_schematics[symbol_location-1].isdigit():
    #         if lower_line_schematics[symbol_location-2].isdigit():
    #             if lower_line_schematics[symbol_location-3].isdigit():
    #                 num = lower_line_schematics[symbol_location-3] + lower_line_schematics[symbol_location-2] + lower_line_schematics[symbol_location-1]
    #             else:
    #                 num = lower_line_schematics[symbol_location-2] + lower_line_schematics[symbol_location-1]
    #         else:
    #             num = lower_line_schematics[symbol_location-1]
    #         return(product_list.append(int(num)))
    #else:
        #pass


def find_special_char(engine_schematics):
    for line_number, line in enumerate(engine_schematics):
        for char_number, char in enumerate(line):
            if char in special_chars:
                right_horizontal_check(char_number, line)
                left_horizontal_check(char_number, line)
                if (line_number + 1) <= (len(engine_schematics) - 1):
                    lower_horizontal_check(char_number, engine_schematics[line_number + 1])

find_special_char(data)
# sum_of_product = sum(product_list)
# print(sum_of_product)