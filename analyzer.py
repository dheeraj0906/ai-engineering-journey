import re
#old version is counting number of error occurences in a log file
pattern = re.compile(r"Batch (\d+) processed in (\d+)ms")
error_count = 0
max_time = None
slowest_batch = None
malformed_count = 0
with open("sample.log", "r") as file:
    for line in file:
        if "ERROR" in line: 
            error_count += 1
        match = pattern.search(line)
        if "processed in" in line and not match:
            malformed_count += 1
        if match:
            batch_number = int(match.group(1))
            time_value = int(match.group(2))
            if max_time is None or time_value > max_time:
                slowest_batch = batch_number
                max_time = time_value
print(f"Errors: {error_count}")
if slowest_batch is not None:
    print(f"Slowest batch: Batch {slowest_batch} ({max_time}ms)")
else:
    print("Slowest batch: none found") 
print(f"Malformed batch lines: {malformed_count}")  
         
