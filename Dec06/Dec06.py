def read_file(txt_file):
    file = open(txt_file)
    data = file.readlines()
    file.close()
    return(data)

path = 'Dec06\Dec06_Sample.txt'
data = read_file(path)

def clean_data(unclean_data):
    cleaned_time = []
    cleaned_distance = []
    for line in unclean_data:
        if "Time" in line:
            remove_heading = line.split(':')
            clean_heading = remove_heading[1:].split(' ')
            print(clean_heading)
            #cleaned_time.append(clean_heading)
    #print(cleaned_time)
clean_data(data)

# Formula:
# distance travelled = speed*(total time - time held)