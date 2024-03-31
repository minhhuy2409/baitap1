# Kiểm tra user và mật khẩu
user = input("Nhập tên người dùng: ")

# Nếu user là admin
if user == "admin":
    password = input("Nhập mật khẩu: ")
    # Kiểm tra mật khẩu
    if password == "123456@Abc":
        print("Welcome!")
    else:
        print("Mật khẩu sai.")
else:
    print("Tên người dùng sai.")
