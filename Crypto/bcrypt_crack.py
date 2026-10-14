import bcrypt

target = b"$2y$10$h2JGq8MxzVKwSSXqOA//CeaXvKwBiBJpbLXZDyAaYzhn/JdgODyje"
# 常用的CTF弱口令字典
passwords = ["admin", "123456", "password", "flag", "qwerty", "admin123", "root", "12345678", "swpu", "ctf", "123", "1", "admin888"]

for pwd in passwords:
    if bcrypt.checkpw(pwd.encode('utf-8'), target):
        print(f"【破译成功！】密码是: {pwd}")
        break
else:
    print("字典没跑出来，试着多加几个密码。")