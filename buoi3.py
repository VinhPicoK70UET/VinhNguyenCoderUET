#Bai1
a = int(input("Nhập số a bất kì: "))
a_daonguoc = int(str(a)[::-1])
print("Số đảo ngược cho ra kết quả của a là: ", a_daonguoc)

#Bai2
a = 5
b = 10
print("Trước khi hoán đổi: a =", a, "b =", b)
a = a ^ b
b = a ^ b
a = a ^ b
print("Sau khi hoán đổi: a =", a, "b =", b)

#Bai3
