def read_file(file_path):
    try:
        fhand = open(file_path)
    except:
        print("File not found")
        exit()
    line_list = []
    line_count = 0
    for line in fhand:
        line_count += 1
        line = line.rstrip()
        line_list.append(line)
    print("all lines: ", line_count)
    return line_list

#file_type = input("Enter log file type to analyze - ")
#full_path = "/var/log/" + file_type
#testing

full_path = "/var/log/syslog"

read_file(full_path)