def asm2(param1, param2):
    var1 = param2
    var2 = param1

    while True:
        var1 += 1
        var2 += 128

        if var2 > 0x63F3:
            break

    return var1

result = asm2(param1=0xb, param2=0x2e)
print(result)

