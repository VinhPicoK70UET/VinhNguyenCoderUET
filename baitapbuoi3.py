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
a = int(input("Nhập số n bất kì: "))
if a > 0 and (a & (a - 1)) == 0: 
    print ("Số n là luỹ thừa của 2")
else: 
    print ("Không phả là luỹ thừa của 2 ")

#Bai4
import math
m = float(input("Nhập số m bất kì: "))
n = float(input("Nhập số n bất kì: "))
print ("Kết quả làm tròn xuống của m/n là: ", math.floor(m/n))

#Bai5
m = float(input("Nhập số m bất kì: "))
n = float(input("Nhập số n bất kì: "))
print ("Kết quả làm tròn xuống của m/n là: ", round(m/n))

#Bai6 
x = int(input("Nhập số x bất kì: "))
if x % 2 == 0 and x > 0:
    print("Số x là số chẵn dương")
elif x % 2 != 0 and x > 0:
    print("Số x là số lẻ dương")
else: 
    print("Số x không hợp lệ")

#Bai7
a = int(input("Nhập số a bất kì: "))
b = int(input("Nhập số b bất kì: "))
if a < 0 and b < 0: 
    print ("Yes")
else: 
    print ("No")

#Bai8:
a = input("Nhập kí tự a bất kì: ")
b = input("Nhập kí tự b bất kì: ")
if len(a) > len(b):
    print("True")
else: 
    print("False")

#Bai9:
a = float(input("Nhập số a bất kì: "))
b = float(input("Nhập số b bất kì: "))
c = float(input("Nhập số c bất kì: "))
if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
    print("3 số a, b, c là 3 cạnh của tam giác")
else: 
    print("3 số a, b, c không phải là 3 cạnh của tam giác")

#Bai10:
a, b, c, d = map(int, input("Nhập 4 số nguyên, cách nhau bằng dấu cách: ").split())
lonnhat = max(a, b, c, d)
print (lonnhat)

#Bai11: 
a, b, c = map(int, input("Nhập 3 số nguyên, cách nhau bằng dấu cách: ").split())
if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
    print ("3 số tạo thành 1 tam giác hợp lệ")
    if a == b == c: 
        print ("Tam giác đều")
    elif a == b or a == c or b == c:
        print ("Tam giác cân")
    else: 
        print ("Tam giác thường")
else: 
    print ("3 số không tạo thành 1 tam giác hợp lệ")

#Bai12:
n = int(input("Nhập số nguyên n bất kì: "))
if n % 4 == 0 and n % 100 !=0 or n % 400 == 0:
    print (n, "là năm nhuận")
else: 
    print (n, "không phải là năm nhuận")

#Bai13: 
n = int(input("Nhập số nguyên kWh bất kì: "))
if 0 < n <=50:
    tien = n * 1500
    print ("Số tiền điện phải trả là: ", tien, "đồng")
elif 50<n<=100:
    tien = 50 * 1500 + (n - 50) * 2000
    print ("Số tiền điện phải trả là: ", tien, "đồng")
elif n > 100: 
    tien = 50 * 1500 + 50 * 2000 + (n - 100) * 3000
    print ("Số tiền điện phải trả là: ", tien, "đồng")
else:
    print ("Số kWh không hợp lệ")

#Bai14:
a = float(input("Nhập số a bất kì: "))
b = float(input("Nhập số b bất kì: "))
print ("Phương trình bậc nhất có dạng: ", a, "x +", b, "= 0")
if a == 0 and b == 0:
    print ("Phương trình có vô số nghiệm")
elif a == 0 and b != 0:
    print ("Phương trình vô nghiệm")
else:
    print ("Phương trình có nghiệm duy nhất: x =", round(-b/a, 2))
    
#Bai15:
a = float(input("Nhập điểm trung bình các môn: "))
if a >= 8.0: 
    print ("Học sinh giỏi")
elif a>=6.5:
    print ("Học sinh khá")
elif a>=5.0:
    print ("Học sinh trung bình")
elif a<5.0 and a>=0:
    print ("Học sinh yếu")
else: 
    print ("Điểm không hợp lệ")

#Bai16: 
a = float(input("Nhập số a bất kì: "))
lamtronxuong = a // 1

if a == int(a):
    lamtronlen = int(a)
elif a > 0: 
    lamtronlen = a // 1 + 1
else: 
    lamtronlen = a // 1

gannhat = a - int(a)
if a > 0:
    gannhat1 = int(a) + (1 if gannhat >= 0.5 else 0)
else: 
    gannhat1 = int(a) - (1 if abs(gannhat) >= 0.5 else 0)

print(int(lamtronxuong), int(lamtronlen), int(gannhat1))

#Bai17: 
a, b, c = map(int, input("Nhập 3 cạnh a, b, c: ").split())

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")