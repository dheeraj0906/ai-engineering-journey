import re
#old version is counting number of errors in a log file
pattern = re.compile(r"Batch (\d+) processed in (\d+)ms")
error_count=0
slowest_time = float('inf')
with open("sample.log", "r") as file:
    for line in file:
        if "ERROR" in line: 
            error_count+= 1
        match = pattern.search(line)
        if match:
            batch_number = int(match.group(1))
            time_value = int(match.group(2))
            if time_value<slowest_time:
                slowest_time = time_value
                batch_number = batch_number
print(f"slowest batch is {batch_number}")            
print(f"Errors: {error_count}")