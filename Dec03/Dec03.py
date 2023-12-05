def read_file(txt_file):
    file = open(txt_file)
    data = file.readlines()
    file.close()
    return(data)

path = 'Dec03_Sample.txt'
data = read_file(path)
special_chars = ['@', '#', '$', '%', '/', '*', '+']
product_list = []

def left_horizontal_check(symbol_location, line_schematics):
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
    
def right_horizontal_check(symbol_location, line_schematics):
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

def lower_horizontal_check(symbol_location, lower_line_schematics):
    print(f'{symbol_location}')
    print(f'{lower_line_schematics}')

def find_special_char(engine_schematics):
    for line_number, line in enumerate(engine_schematics):
        for char_number, char in enumerate(line):
            if char in special_chars:
                right_horizontal_check(char_number, line)
                left_horizontal_check(char_number, line)
                #print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                #print(lower_horizontal_check(line_number, engine_schematics))


find_special_char(data)
sum_of_product = sum(product_list)
print(sum_of_product)