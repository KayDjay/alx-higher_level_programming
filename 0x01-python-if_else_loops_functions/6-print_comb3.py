#!/usr/bin/python3
for a in range(10):
    for n in range(a + 1, 10):
        if a * 10 + n < 89:
            print("{:02d}".format(a * 10 + n), end=', ')

print("{:02d}".format(89), end='')
print()
