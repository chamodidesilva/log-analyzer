def read_file(file_path):
    try:
        fhand = open(file_path)
    except:
        print("File not found")
        exit()
    for line in fhand:
        line = line.rstrip()
        print(line)

inp = input("Enter file name to analyze - ")
read_file(inp)