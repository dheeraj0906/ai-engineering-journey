with open("sample.log", "r") as file:
    for line in file:
        content=line

print(type(content))
print(repr(content))