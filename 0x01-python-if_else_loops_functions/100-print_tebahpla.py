#!/usr/bin/python3
s = ""
for i in range(65, 91):
    if i % 2 == 0:
        s += chr(i + 32)
    else:
        s += chr(i)
print("{}".format(s[::-1]), end="")
