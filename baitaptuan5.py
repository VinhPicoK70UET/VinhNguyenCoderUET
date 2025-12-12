#W5A1:
a, b = map(int, input("Nhập hai số nguyên a và b: ").split())
def max_of_two (a,b) -> int:
    if a > b:
        return a
    if b > a:
        return b
print("Số giá trị lớn hơn là: ", max_of_two(a,b))

#W5A2:
a, b = map(int, input("Nhập 2 số nguyên a và b: ").split())
def swap(a, b) -> tuple[int, int]: 
    return (b, a)

print (swap(a,b))

#W5A3:
n = int(input("Nhập số nguyên n:"))
def songuyento(n):
    if n < 2: 
        return False
    if n == 2: 
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
    
if songuyento(n): 
    print ("Số này là số nguyên tố")
else:
    print ("Số này không phải là số nguyên tố")

#W5A4: 
def is_perfect(n: int) -> bool:
    if n <= 1:
        return False

    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i

    return tong == n

n = int(input("Nhập số n: "))
if is_perfect(n):
    print("YES, số hoàn hảo")
else:
    print("NO, không phải số hoàn hảo")


#W5A5:
def find_first_index (nums: list[int], k: int) -> int:
    for i in range (len(nums)):
        if nums[i] == k: 
           return i
    return -1 

nums = list(map(int, input("Nhập dãy số nguyên n cách nhau: ").split()))
k = int(input("Nhập số nguyên k: "))

print (find_first_index(nums, k))

#W5A6:
import math
n = int(input("Nhập số nguyên n: "))
results = math.factorial(n)
print(results)

#W5A7: 
def maytinh_botui (num1: float, num2: float, oper: str) -> float:
    if oper == "+":
        results = num1 +num2
    elif oper == "-":
        results = num1 -num2
    elif oper == "*":
        results = num1 * num2
    elif oper == "/":
        if num2 = 0:
            return None
        else: 
            results = num1 / num2
    else: 
        return None
    return results
num1 = float(input("Nhập giá trị cần điền"))
num2 = float(input("Nhập giá trị cần điền"))
print ("Giá trị kết quả là", maytinh_botui())

#W5A8: 
def hamming_distance(x: int, y: int) -> int:
    return bin(x ^ y).count("1")

#W5A9:
def tongchuso(n: int) -> int:
    tong = 0
    while n > 0:
       tong += n % 10 
       n //= 10
    return tong
n = int(input("Nhập số nguyên n: "))
print("Tổng chữ số trong số nguyên n là: ", (tongchuso(n)))

#W5A10:
def is_anhxa(a: str, b: str) -> bool:
    map_a_to_b = {}
    map_b_to_a = {}
    for ch1, ch2 in zip(a,b):
        if ch1 in map_a_to_b: 
            if map_a_to_b[ch1] != ch2:
                return False
        else:
            map_a_to_b[ch1] = ch2
        
        if ch2 in map_b_to_a:
            if map_b_to_a[ch2] != ch1:
                return False
        else:
            map_b_to_a[ch2] = ch1
    
    return True
a, b = str(input("Nhập 2 chữ a và b: ")).split()
print(is_anhxa(a,b))





