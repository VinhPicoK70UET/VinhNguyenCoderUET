#W2A3
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print ("Tổng là: ", a+b)
print ("Hiệu là:", a-b)
print ("Tích là:", a*b)
print ("Thương là:", a/b)
print ("Phần dư là:", a%b)
print ("Phần nguyên là:", a//b)

#W2A4
a1 = int(input("Nhập 3 điểm hệ số 1: "))
b1 = int(input("Nhập 3 điểm hệ số 1: "))
c1 = int(input("Nhập 3 điểm hệ số 1: "))

a2 = int(input("Nhập 2 điểm hệ số 2: "))
b2 = int(input("Nhập 2 điểm hệ số 2: "))

a3 = int(input("Nhập 1 điểm hệ số 3: "))

print ("Nhập điểm trung bình môn",((a1+b1+c1)+(a2+b2)*2+a3*3)/10)

#W2A5 
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print ("Kết quả", a, "^", b, "là:", a**b)

#W2A6
kytu = input("Nhập ký từ (a-z) bất kì:")
print ("Mã kí tự của chữ cái", kytu, "là:", ord(kytu))

kytuinhoa = chr(ord(kytu)-32)
print ("Chữ in hoa của chữ cái", kytu, "là:", kytuinhoa)
#W2A7
A = ((13 ** 2) * 3) + 5 
print (A)

B = ((12 ** 2) * 4) + 6
print (B)

#W2A8
C = float(input("Nhập độ C: "))
F = 9/5*C + 32
rounded = round(F, 2)
print ("Nhiệt độ F quy đổi ra là: ", rounded)

#W2A9
a = float(input("Nhập giá chiếc đồng hồ: "))
tien = a + 10 + 0.3*a + 0.1*a 
print ("Tổng số tiền phải trả là:", round(tien, 2), "USD")

#W2A11
a = int(input("Nhập số giờ cần điền: "))
b = int(input("Nhập số phút cần điền: "))
if a < 0 or b < 0 or b >60:
    print ("Giờ hoặc phút không hợp lệ")
else: 
    print ("Tổng số giây quy đổi ra là: ", a*3600 + b*60, "giây")

#W2A12
a = int(input("Nhập độ dài cạnh khối Rubik: "))
somiengdan = 6*(a**2)
print ("Số miếng dán cần dùng là:", somiengdan)

#W2A13
a = int(input("Nhập số a bạn cần điền: "))
b = int(input("Nhập số b bạn cần điền: "))
tich = a*b
hangdonvi = str(tich)[-1]
print ("Chữ số hàng đơn vị của tích hai số là:", hangdonvi) 

#W2A14
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

a = a + b
b = a - b
a = a - b

print("Sau khi hoán đổi: a =", a, ", b =", b)

#W2A15
n = int(input("Nhập số nguyên dương n: "))
sosao = 6 * n * (n - 1) + 1
print("Số sao thứ", n, "là:", sosao)