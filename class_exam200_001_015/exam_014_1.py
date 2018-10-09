x = 1
total = 0
while 1:
    total += x
    if total > 100000:
        print(x)
        print(total)
        break
    x += 1
