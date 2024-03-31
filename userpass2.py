# Kiểm tra user và mật khẩu
user = input("Nhập tên người dùng: ")
password = input("Nhập mật khẩu: ")

# Nếu user là admin và mật khẩu là 123456@Abc
if user == "admin" and password == "123456@Abc":
    print("Welcome!")
else:
    print("Wrong password and username.")
