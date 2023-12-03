red = 12
green = 13
blue = 14


def read_input_file(txt_files):
    file = open(txt_files)
    data = file.readlines()
    file.close()
    return(data)

def split_input_game(text_input):
    game_index = line.split(':')
    return(game_index[0])

def get_game_index(lines):
    game_id = str()
    for n in lines:
        if n.isdigit() == True:
            game_id += n
    print(int(game_id))

path_to_file = 'Dec02\Dec02_Input.txt'
data = read_input_file(path_to_file)
for line in data:
    get_game_index(split_input_game(line))
