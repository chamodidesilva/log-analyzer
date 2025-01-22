import re
from datetime import datetime

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


def filter_by_time_range(start, end):
    line_list = read_file(full_path)
    line_match_count = 0
    timestamp_format = "%H:%M:%S"
    start_obj = datetime.strptime(start, timestamp_format)
    end_obj = datetime.strptime(end, timestamp_format)
    for line in line_list:
        timestamp = re.search('\d{2}:\d{2}:\d{2}', line)
        if timestamp:
            timestamp_obj = datetime.strptime(timestamp.group(), timestamp_format)
            if start_obj <= timestamp_obj <= end_obj:
                print(line)
                line_match_count += 1
    print("matching lines: ", line_match_count)

#file_type = input("Enter log file type to analyze - ")
#full_path = "/var/log/" + file_type

full_path = "/var/log/syslog"

print("Enter a time range in form HH:MM:SS")
start_time = input("Start time: ")
end_time= input("End time: ")
filter_by_time_range(start_time, end_time)

#add error handling (now or later?)