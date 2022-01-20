a = "1010"
b = "1011"

print(int(a, 2))
print(bin(int(a, 2) + int(b, 2)).replace("0b", ""))
