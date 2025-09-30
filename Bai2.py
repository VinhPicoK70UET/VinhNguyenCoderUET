a = int(input("Nhập số n bất kì "))
b = int(input("Nhập số m bất kì "))
print ("2 số đầu vào là: ", a, "và", b)
a = a ^ b
b = a ^ b
a = a ^ b
print ("2 số sau khi hoán đổi là: ", a, "và", b)