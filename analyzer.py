file = open("./sample.log.txt", "r")
content = file.read()
errorcount = content.count("ERROR")

print(f"Errors: {errorcount}")
file.close()