import re
#old version is counting number of errors in a log file
pattern = re.compile(r"Batch (\d+) processed in (\d+)ms")
error_count = 0
max_time = -1
slowest_batch = -1
with open("sample.log", "r") as file:
    for line in file:
        if "ERROR" in line: 
            error_count+= 1
        match = pattern.search(line)
        if match:
            batch_number = int(match.group(1))
            time_value = int(match.group(2))
            if time_value > max_time:
                slowest_batch = batch_number
                max_time = time_value
print(f"slowest batch is {slowest_batch}")            
print(f"Errors: {error_count}")