"""Mini-project mức A: vẽ thẻ ASCII tĩnh bằng print(), chưa có đáp án."""

# TODO 1: In hàng viền trên bằng + và -.
# TODO 2: In lời chào giữa hai dấu |, giữ đúng độ rộng.
# TODO 3: In hàng viền dưới bằng hàng trên.
# TODO 4 (tự chọn): Thêm hình trang trí.
name=input("Nhap ten cua ban: ");
massage = "Xin Chao " + name + "!";
width = len(massage) + 2;

print("+" + "-" * width + "+");
print("| "+massage+" |");
print("+" + "-" *width + "+");