def read_file(txt_file):
    file = open(txt_file)
    data = file.readlines()
    file.close()
    return(data)

path = 'Dec05\Dec05_Sample.txt'
data = read_file(path)