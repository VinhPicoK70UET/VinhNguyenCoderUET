#W6A1
dayso = list(map(int,input("Nhập dãy số nguyên: ").strip().split()))
results = []
seen = set(results)

for x in dayso: 
    if x not in seen: 
        results.append(x)
        seen.add(x)
    
print (results)

#W6A2:
dayso = list(map(int,input("Nhập dãy số nguyên: ").strip().split()))
results = []
sumnow = 0

for x in dayso:
    sumnow += x 
    results.append (sumnow)

print (results)

#W6A3: 
t = tuple(map(int, input().split()))
k = int(input())

k = k % len(t) if t else 0   # phòng trường hợp k > độ dài hoặc tuple rỗng

t_moi = t[k:] + t[:k]

print(t_moi)


#W6A4: 
pairs = input().split()
d = {}
for p in pairs:
    key, value = p.split(":")
    if key not in d:
        d[key] = []
    d[key].append(value)
print(d)


#W6A5:
nums = list(map(int,input("Nhập dãy số nguyên: ").strip().split()))
results = {'positives':0, 'negatives': 0, 'zeros': 0}

for x in nums:
    if x > 0:
        results['positives'] += 1 
    if x < 0:
        results['negatives'] += 1
    if x == 0:
        results['zeros'] += 1 
    
print (results)


#W6A6:
dayso = list(map(int, input("Nhập dãy số nguyên: ").strip().split()))
results = []
tong = 0

for x in dayso: 
    tong +=x 

print(tong)

#W6A8: 
items = input("Nhập ký tự: ").strip().split()
counts = {}

for x in items: 
    if x in counts: 
        counts[x] += 1
    else:
        counts[x] = 1

print(counts)
#W6A9: 
chuoi1 = int(input("Nhập chuỗi 1: ").strip())
dict1 = {}
for i in range (1, len(chuoi1), 2):
    key = chuoi1[i]
    value = chuoi1[i+1]
    dict1[key] = value 

chuoi2 = int(input("Nhập chuỗi 2: ").strip())
dict2 = {}
for i in range (1, len(chuoi2), 2):
    key = chuoi2[i]
    value = chuoi2[i+1]
    dict2[key] = value 
ketqua = {}
for key in dict1: 
    ketqua[key] = dict1[key]
for key in dict2:
    if key in ketqua: 
        ketqua[key] += dict2[key]
    else: 
        ketqua[key] = dict2[key]
print (ketqua)



#W6A10: 
lst = list(map(int, input().split()))
k = int(input())
result = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == k:
            result.append((lst[i], lst[j]))
print(result)

#W6A11:
t = tuple(map(int, input("Nhập dãy số nguyên: ").strip().split()))
chan = []
le = []
for x in t: 
    if t % 2 == 0: 
        chan.append(x)
    else:
        le.append(x)
print (tuple(chan))
print (tuple(le))   


#W6A12:

dayso = list(map(int, input("Nhập dãy số nguyên: ").strip().split()))

max_count = 0
result = dayso[0]

for x in dayso:
    count = dayso.count(x)
    if count > max_count or (count == max_count and  x < result):
        max_count = count
        result = x 

print (result)

#W6A13:
d = eval(input("Nhập dictionary: ").strip())
result = {}
for k, v in d.items():
    result[v] = k 

print (result)

#W6A14:
a = list(map(int, input("Nhập dãy số nguyên a: ").split()))
b = list(map(int, input("Nhập dãy số nguyên b: ").split()))
result = []
for x in a:
    if x in b and x not in result:
        result.append(x)

print (result)

#W6A15:
tokens = input().split()
k = int(input())

d = {}
for i in range(0, len(tokens), 2):
    key = tokens[i]
    value = int(tokens[i + 1])
    d[key] = value

result = {}
for key in d:
    if d[key] > k:
        result[key] = d[key]

print(result)



#W6A16:
n, m = map(int, input().split())
a = []
for i in range (n):
    a.append (list(map(int, input().split())))

for i in range (n):
    for j in range (m):
        print (f"{a[i][j]:>4}", end = '')
    print ()

#W6A17:
n = int(input())
a = []
for i in range (n): 
    dong = list(map(int, input().split()))
    a.append(dong)

cheo_chinh = 0
for i in range (n):
    cheo_chinh += a[i][i]

cheo_phu = 0
for i in range (n):
    cheo_phu += a[i][n - 1 - i]

print (cheo_chinh)
print (cheo_phu)
    
#W6A18: 
n, m, k = map(int, input().split())
a = []
for i in range(n):
    dong = list(map(int, input().split()))
    a.append(dong)

# Tính tổng cột k
tongcot = 0
for i in range(n):
    tongcot += a[i][k]

# Tính tổng hàng k
tonghang = 0
for j in range(m):
    tonghang += a[k][j] 

print(tongcot)
print(tonghang)

#W6A19:
def maxindex (nums: list[int]) -> int:
    if not nums:
        return -1
    
    maxvalue = nums[0]
    maxindex = 0
    for i in range(len(nums)):
        if nums[i] > maxvalue:
            maxvalue = nums[i]
            maxindex = i 
    return maxindex

nums = list(map(int, input("Nhập dãy số nguyên: ").strip().split()))


print (maxindex(nums))

#W6A20: 
def first_index_of_k(nums, k):
    for i in range(len(nums)):
        if nums[i] == k:
            return i
    return -1

#W6A21: 
s = input().split()
d = {}
for word, i in enumerate(s):
    d.setdefault(word, []).append(i)

for k in d: 
    d[k] = tuple(d[k])

print (d)

#W6A22: 
def index_of_max(nums):
    max_index = 0          # giả sử phần tử đầu tiên là lớn nhất

    for i in range(1, len(nums)):
        if nums[i] > nums[max_index]:
            max_index = i  # cập nhật vị trí lớn nhất mới

    return max_index





    


