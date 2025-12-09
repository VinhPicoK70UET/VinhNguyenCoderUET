#W4A1
n = int(input("Nhập số nguyên n: "))
total = 0 
for i in range (1, n +1):
    total += i
print("Tổng từ 1 đến", n, "là:", total)

#W4A2 
# Nhập số
n = int(input("Nhập một số nguyên bất kỳ: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương.")
else: 
    def nguyento(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        limit = int(n**0.5) + 1
        for i in range(3, limit, 2):
            if n % i == 0:
                return False
        return True
    # Gọi hàm và in kết quả
    if nguyento(n):
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")
#W4A3
n = int(input("Nhập số nguyên n: "))
if n <= 0 or n >= 100:
    print("giá trị không hợp lệ, vui lòng nhập số trong khoảng từ 1 đến 99.")
else: 
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i 
    print (f"Giai thừa của {n} là: {factorial}")

#W4A4
n = int(input("Nhập số nguyên n: "))
n = abs(n)

if n == 0:
    count = 1
else: 
    count = 0 
    while n > 0: 
        n = n // 10
        count += 1
print(f"Số chữ số của số nguyên là: {count}")

#W4A5
n = int(input("Nhập số nguyên n: "))
dayso = list(map(int, input("Nhập thành dãy số cách nhau bằng dấu cách: ").split()))

timso42 = False
for i in dayso:
    if i == 42:
        timso42 = True
        break
if timso42: 
    print(" I've found the meaning of life!")
else: 
    print("It's a joke")

#W4A6:
def is_prime(n):
    if n <2:
        return False
    if n ==2: 
        return True
    if n % 2 ==0: 
        return False
    i = 3
    while i * i <= n:
        if n % i ==0:
            return False
        i +=2 
    return True

a, b = map(int, input("Nhập hai số nguyên a và b: ").split())
total = 0 
for x in range(a, b + 1):
    if is_prime(x):
        total += x
print(f"Tổng các số nguyên tố trong khoảng từ {a} đến {b} là: {total}")

#W4A7
n = int(input("Nhập số nguyên n (n>=2): "))
largest_prime = -1

while n % 2 == 0:
    largest_prime = 2
    n //= 2 

i = 3
while i * i <= n:
    while n % i == 0:
        largest_prime = i 
        n //= i
    i += 2 

if n > 2: 
    largest_prime = n 
print("Ước số nguyên tố lớn nhất là:", largest_prime)
#W2A8
n = int(input("Nhập số nguyên dương n: "))
def reverse_number(n):
    return int("".join(reversed(str(n))))

def is_palindrome(n):
    return n == reverse_number(n)
steps = 0
while not is_palindrome(n):
    if n == is_palindrome(n):   # nếu n là palindrome
        break
    else: 
        n += is_palindrome(n)
        steps += 1

print("Số bước cần thực hiện để n trở thành số đối xứng là:", steps, "và số palindrome là:", n)

#W4A9: 
import math
n = int(input("Nhập số nguyên dương n: "))
results = []
for i in range(1, int(math.sqrt(n)) + 1):
    s = i*i
    s_str = str(s)
    if len (s_str) == len(set(s_str)):
        results.append(s)

if results: 
    print(*results)

if not results:
    print("no number found")

#W4A10: 
import math

def daysocollatz(n):
    length = 1
    while n != 1: 
        if n % 2 ==0:
            n = n // 2
        else:
            n = 3 * n +1 
        length += 1
    return length 

n = int(input("Nhập số nguyên dương n: "))

max_length = 1 
max_number = 1

for i in range(1, n + 1):
    L = daysocollatz(i)
    if L > max_length or (L == max_length and i > max_number):
        max_length = L
        max_number = i

print(f"Số có chuỗi Collatz dài nhất là: {max_number} với độ dài chuỗi là: {max_length}")

#W2A11:
n = int(input("Nhập số nguyên dương n:"))

if n % 2 == 0: 
    print("Không có ước chẵn")
else: 
    m = n // 2
    count = 0
    for i in range(1, int(math.sqrt(m)) +1):
        if m % i ==0: 
            j = m // i 
            if i != j: 
                count +=2 
            else: 
                count +=1
    print(count) 

#W4A12: 
X = int(input("Nhap so tien gui ban dau: "))
N = int(input("Nhap so thang gui: "))

S = X * (1 + 0.007) ** N
S = int(S)  # Bỏ phần lẻ thập phân

print("So tien nhan duoc sau", N, "thang la:", S)
#W4A13: 
def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

a = int(input())
b = int(input())

if sum_of_divisors(a) == b and sum_of_divisors(b) == a:
    print("true")
else:
    print("false")

#W4A14:
import math

m = int(input())
n = int(input())

print(math.gcd(m, n))


#W4A15:
def chicken_and_dog(total_animals, total_legs):
    # Gọi:
    # g = số gà
    # c = số chó
    # g + c = total_animals
    # 2g + 4c = total_legs
    
    # Từ hệ:
    # c = (total_legs - 2*total_animals) / 2
    # g = total_animals - c

    if (total_legs - 2 * total_animals) % 2 != 0:
        return "invalid"

    c = (total_legs - 2 * total_animals) // 2
    g = total_animals - c

    if g < 0 or c < 0:
        return "invalid"

    return g, c


# Ví dụ:
n, m = map(int, input("Nhập số lượng động vật và số chân (cách nhau bởi dấu cách): ").split())
result = chicken_and_dog(n, m)
print(result)


#W4A16: 
for i in range (1, 100):
    if i % 3 ==0 and i % 2 ==0: 
        print(i)

#W4A17:
a = int(input("Nhập số nguyên a: "))
for i in range (1,11):
    i = a * i 
    print(f"{a} x {i//a} = {i}")

#W4A18:
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

def gcd(a,b):
    if a < b: 
        for i in range (1, a + 1):
            if a % i == 0 and b % i == 0:
                gcd = i
                print (gcd)
    else:
        for i in range (1, b + 1):
            if a % i == 0 and b % i == 0:
                gcd = i 
                print (gcd)
    return gcd
print("Ước chung lớn nhất của", a, "và", b, "là:", gcd(a,b))

#W4A19: 
n = int(input("Nhập số nguyên n: "))
i = 2 
while i <= n: 
    print (i, end = " ")
    i +=2 

#W4A20: 
n = int(input("Nhập số nguyên n: "))
if n < 0: 
    print("Số này không phải là số nguyên dương")
else:
    while n % 2 == 0:
        n //= 2

if n == 1:
    print("Số này là lũy thừa của 2")
else: 
    print("Số này không phải là lũy thừa của 2")
    
#W4A21:
n = int(input("Nhập số nguyên n: "))
tong = 0
for i in n: 
    tong += int(i)

print("Tổng các chữ số của n là:", tong)

#W4A22: 
n = int(input("Nhập n: "))

chan = 0
le = 0

for ch in str(n):
    if int(ch) % 2 == 0:
        chan += 1
    else:
        le += 1

print("Số chữ số chẵn:", chan)
print("Số chữ số lẻ:", le)

#W4A23: 
n = float(input("Nhập số n: "))

total = 0.0
k = 0
while total < n:
    k += 1
    total += k

# lúc này total >= n, k là chỉ số đầu tiên khiến total >= n
k_correct = k - 1
sum_correct = total - k

print("k lớn nhất thỏa S(k) < n là:", k_correct)
print("S(k) =", sum_correct)

#W4A24:
A = float(input("Nhập số A: "))
sum = 0.0
n = 0
while sum < A:
    n += 1
    sum += 1/n 

print("Giá trị nhỏ nhất của n để tổng lớn hơn hoặc bằng A là:", n)

#W4A25:
def tim_min_max():
    nums = []
    while True: 
        try: 
            a = str(input("Nhập số nguyên (hoặc nhập 'x' để kết thúc): "))
            if a == "-1":
                break
            nums.append(a)
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ")
    if len(nums) == 0: 
        print("Không có số nào để tìm max/min.")
    else:
        print("Số lớn nhất:", max(nums))
        print("Số nhỏ nhất:", min(nums))

tim_min_max()

#W4A26:
def fibonacci(A):
    f1 = 1 
    f2 = 1
    while f1 + f2 < A:
        fnext = f1 + f2 
        f1 = f2 
        f2 = fnext 
    print(f"Số Fibonacci lớn nhất không vượt quá {A} là: {f2}")

try: 
    so_a = int(input("Nhập số nguyên dương A: "))
    if so_a <= 0:
        print("Vui lòng nhập số nguyên dương.")
    else:
        fibonacci(so_a)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ")

#W4A27: 

def dem_sotu():
    chuoi = str(input("Nhập chuỗi ký tự: "))
    dodai = 0
    for _ in chuoi:
        dodai += 1
    demtu = 0
    
    for i in range(dodai):
        kytuhientai = chuoi[i]
        if kytuhientai != " ":
            if i == 0 or chuoi[i -1] == " ":
                demtu += 1 
    
    print(f"Số từ trong chuỗi là: {demtu} và số ký từ là: {dodai}")

dem_sotu() 

#W4A28: 
def in_sodau ():
    chuoi = str(input("Nhập chuỗi ký tự: "))
    dodai = 0
    for _ in chuoi:
        dodai += 1
    dagapchu = False 
    tudautien = ""
    for i in range (dodai):
        kytu = chuoi[i]
        if kytu != " ":
            tudautien += kytu
            dagapchu = True
        else: 
            if dagapchu == True: 
                break
    print("Từ đầu tiên trong chuỗi là:", tudautien)

in_sodau()

#W4A29: 
# Cách an toàn, dễ hiểu
line = input("Nhập (ví dụ: 3, 12, 15): ").strip()

# Tách theo dấu phẩy và loại khoảng trắng xung quanh
parts = [p.strip() for p in line.split(',')]

if len(parts) != 3:
    print("Dữ liệu không hợp lệ — phải nhập đúng 3 số, cách nhau bằng dấu phẩy.")
else:
    try:
        a, b, c = map(int, parts)   # chuyển từng phần về int
        total = a + b + c
        print("Tổng:", total)
    except ValueError:
        print("Dữ liệu không hợp lệ — các thành phần phải là số nguyên.")


#W4A30: 
s = input("Nhập chuỗi: ")

upper = 0   # chữ in hoa
lower = 0   # chữ in thường
digit = 0   # chữ số

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1

print("Ký tự in hoa:", upper)
print("Ký tự in thường:", lower)
print("Ký tự số:", digit)

#W4A31: 

def tinhtongchuoi():
    chuoi = str(input("Nhập chuỗi ký tự số: ")) 
    tong = 0
    for kytu in chuoi:
        if kytu.isdigit():
            tong += int(kytu)
    print("Tổng các chữ số trong chuỗi là:", tong)

tinhtongchuoi()

#W4A32:

def kiemtramatkhau():
    matkhau = str(input("Nhập mật khẩu: "))
    if len(matkhau) < 6:
        print("Mật khẩu yếu: Quá ngắn")
        return 
    chuinhoa = False
    chuinthuong = False
    chuso = False
    chudacbiet = False

    for kytu in matkhau: 
        if kytu.isupper():
            chuinhoa = True
        elif kytu.islower():
            chuinthuong = True
        elif kytu.isdigit():
            chuso = True
        else:
            chudacbiet = True
    
    if chuinhoa and chuinthuong and chuso and chudacbiet:
        print("Mật khẩu mạnh")
    else:
        if not chuinhoa:
            print("Mật khẩu yếu: Thiếu chữ in hoa")
        if not chuinthuong:
            print("Mật khẩu yếu: Thiếu chữ in thường")
        if not chuso:
            print("Mật khẩu yếu: Thiếu chữ số")
        if not chudacbiet:
            print("Mật khẩu yếu: Thiếu ký tự đặc biệt")
    
kiemtramatkhau()

#W4A33: 
def chuoi():
    kytu = int(input("Nhập số ký tự: "))
    a = str(kytu)
    count = 0
    result = ""
    for i in range(len(a)-1, -1, -1):
        result += a[i]
        count += 1
        if count == 3 and i != 0: 
            result += "."
            count = 0
    print("Chuỗi sau khi đảo ngược và thêm dấu chấm là:", result)

chuoi()

#W4A34:
a = input("Nhập chuỗi a: ")
b = input("Nhập chuỗi b: ")

result = ""
i = 0

while i < len(a):
    # kiểm tra xem tại vị trí i chuỗi b có xuất hiện không
    if a[i:i+len(b)] == b:
        i += len(b)    # bỏ qua đoạn giống chuỗi b
    else:
        result += a[i]
        i += 1

print("Chuỗi sau khi xóa:", result)
