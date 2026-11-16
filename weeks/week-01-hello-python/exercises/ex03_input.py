"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
input_name=input("Nhap ten cua ban: ");
print("Xin chao,",input_name,"!");

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
input_age=int(input("Nhap tuoi: "));
print("Nam sinh cua ban la: ",2026-input_age);

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
input_num1=int(input("Nhap so thu nhat: "));
input_num2=int(input("Nhap so thu hai: "));
print("Tong:",input_num1,"+",input_num2,"=",input_num1+input_num2);

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
input_name=input("Nhap Ten: ");
input_adj=input("Nhap tinh tu: ");
input_animal=input("Nhap con vat: ");
input_number=input("nhap so luong: ");
print("|Xin Chao ban",input_name,"! Hom nay la mot ngay",input_adj,".Ban da thay mot con",input_animal,"tren duong va ban da dem duoc co",input_number,"con|");