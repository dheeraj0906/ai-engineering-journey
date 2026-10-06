#old version is counting number of errors in a log file
error_count=0
with open("sample.log", "r") as file:
    for line in file:
        if "ERROR" in line: 
            error_count+= 1
print(f"Errors: {error_count}")