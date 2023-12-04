import time
start = time.perf_counter()
answer = 0
path_to_file = 'Dec02\Dec02_Input.txt'


def read_input_file(txt_files):
    file = open(txt_files)
    data = file.readlines()
    file.close()
    return(data)

def split_input_game(text_input):
    game_index = text_input.split(':')
    return(game_index[0])

def split_input_colours(text_input):
    game_index = text_input.split(':')
    return(game_index[1])

def get_game_index(lines):
    game_id = str()
    for n in lines:
        if n.isdigit() == True:
            game_id += n
    return(int(game_id))

def comma_split(text_input):
    colour_event = text_input.split(',')
    return(colour_event)

def colour_breakdown(lines):
    colour_seperator = lines.split(';')
    #colour_seperator2 = colour_seperator.split(',')
    return(colour_seperator)

def success_check(event_input):
    check_event = event_input.split(' ')
    if check_event[1] == 'red':
        if int(check_event[0]) > 12:
            return(False)
    elif check_event[1] == 'blue':
        if int(check_event[0]) > 14:
            return(False)
    elif check_event[1] == 'green':
        if int(check_event[0]) > 13:
            return(False)

data = read_input_file(path_to_file)

for line in data:
    event_failure = False
    for event in colour_breakdown(split_input_colours(line)):
        for event2 in comma_split(event):
            check_event = event2.strip()
            if success_check(check_event) == False:
                event_failure = True
    if event_failure == False:
        answer += get_game_index(split_input_game(line))
    else:
        event_failure = False

print(answer)
end = time.perf_counter()
print(end - start)