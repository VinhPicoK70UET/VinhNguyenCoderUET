#W1A1
a = 7 
b = 5 
c = a - b 
print(c) 

#W1A2 
#Đoạn code #W1A2 khai báo biến city và year, sau đó in ra tên thành phố và năm bằng hàm print.
city = "Hà Nội" 
year = 2025 
print("Thành phố: ", city, " - Năm: ", year)

#W1A3
# Đoạn code #W1A3 khai báo biến n và t, dùng vòng lặp cộng dồn các số từ 1 đến n vào t, rồi in tổng ra màn hình.#
n = 4 
t = 0 
for i in range(1, n+1): 
    t += i 
print(t) 

#W1A4
#Đoạn code #W1A4 duyệt qua từng số trong danh sách numbers, kiểm tra số đó là chẵn hay lẻ bằng phép chia dư, rồi in kết quả ra màn hình.
numbers = [1, 2, 3, 4] 
for x in numbers: 
    if x % 2 == 0: 
        print(x, "là số chẵn") 
    else: 
        print(x, "là số lẻ") 

#W1A5

animals = ["cat", "dog", "cat", "bird"] 
count = 0 
for a in animals: 
    count += 1 
print("Số phần tử trong danh sách là:", count) 

#W1A6
#Chương trình này hiển thị menu với ba lựa chọn: phân tích cảm xúc, dự báo thời tiết, hoặc thoát. Khi người dùng nhập lựa chọn, chương trình sẽ thực hiện chức năng tương ứng (phân tích cảm xúc, dự báo thời tiết, hoặc kết thúc chương trình). Kết quả có được là do chương trình kiểm tra lựa chọn của người dùng và thực hiện hành động phù hợp với từng lựa chọn.

#W1A7 sai 
num = input("Nhập số: ") #Hàm input() trả về kiểu chuỗi, cần chuyển sang số nguyên bằng int().
if num % 2 = 0: #Toán tử so sánh phải là ==, không phải =
print("Số chẵn") 
else #Thiếu thụt lề bên trong khối lệnh else, thiếu dấu : sau else.
print("Số lẻ") 

#W1A7 đúng
num = int(input("Nhập số: "))
if num % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")

#W1A8:
#  Đoạn code #W1A8 sẽ in ra:
#AI đang học lần 1
#AI đang học lần 2
#AI đang học lần 3
#Huấn luyện xong!

for i in range(3): 
    print("AI đang học lần", i + 1) 
print("Huấn luyện xong!") 
#Vòng lặp for i in range(3) chạy 3 lần với i từ 0 đến 2. Mỗi lần lặp, chương trình in ra dòng "AI đang học lần" kèm số lần học (i + 1). Sau khi vòng lặp kết thúc, chương trình in "Huấn luyện xong!" để báo quá trình học đã hoàn thành.

#W1A9: 
#Đoạn code #W1A9 sẽ in ra:
#Dự đoán con vật: cat   
#Dự đoán con vật: dog   
#Dự đoán con vật: fish
for x in ["cat", "dog", "fish"]: 
    print("Dự đoán con vật:", x)
#Vòng lặp for x in ["cat", "dog", "fish"] duyệt qua từng phần tử trong danh sách. Mỗi lần lặp, chương trình in ra dòng "Dự đoán con vật:" kèm tên con vật tương ứng.

#W1A10 sai:
# Simple menu
print "=== AI Prediction System ==="  #Thiếu dấu ngoặc đơn sau hàm print
print("1) Sentiment analysis"  # Thiếu dấu đóng ngoặc đơn
print("2) Weather forecast")) 
print('3) Exit'  # Thiếu dấu đóng ngoặc đơn
print("Please choose an option:")  

#W1A10 đúng: 
print("=== AI Prediction System ===")
print("1) Sentiment analysis")
print("2) Weather forecast")
print("3) Exit")
print("Please choose an option:")