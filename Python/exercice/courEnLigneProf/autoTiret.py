num = "0800353637"
buff = ""
for i in range(1, len(num), 2):
    buff += str(num[i-1]) + str(num[i])
    if i+1 != len(num):
        buff += "-"

print(buff)