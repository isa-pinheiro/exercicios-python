val = []
count = 0

for i in range(5):
    var = int(input('insira um número: '))
    if i == 0 or var > val[-1]:
        val.append(var)
    else:
        pos = 0
        while pos < len(val):
            if var <= val[pos]:
                val.insert(pos, var)
                break
            pos += 1

print(val)
