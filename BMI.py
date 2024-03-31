# Nhập cân nặng và chiều cao từ người dùng
can_nang = float(input("Nhập cân nặng của bạn (kg): "))
chieu_cao = float(input("Nhập chiều cao của bạn (m): "))

# Tính chỉ số BMI
bmi = can_nang / (chieu_cao ** 2)

# In ra chỉ số BMI
print("Chỉ số BMI của bạn là:", bmi)

# Phân loại và diễn giải chỉ số BMI
if bmi < 16:
    print("Gầy cấp độ III")
elif 16 <= bmi < 17:
    print("Gầy cấp độ II")
elif 17 <= bmi < 18.5:
    print("Gầy cấp độ I")
elif 18.5 <= bmi < 25:
    print("Bình thường")
elif 25 <= bmi < 30:
    print("Thừa cân")
elif 30 <= bmi < 35:
    print("Béo phì cấp độ I")
elif 35 <= bmi < 40:
    print("Béo phì cấp độ II")
else:
    print("Béo phì cấp độ III")
