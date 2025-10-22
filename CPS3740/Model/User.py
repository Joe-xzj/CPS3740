import json
import hashlib
import os

USER_FILE = 'users.json'

def hash_password(password: str) -> str:
    """使用 SHA256 哈希密码"""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """从文件加载用户信息"""
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_users(users):
    """保存用户信息到文件"""
    with open(USER_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

def register():
    """用户注册"""
    users = load_users()
    username = input("请输入用户名: ").strip()
    
    if username in users:
        print("该用户名已存在，注册失败。")
        return
    
    password = input("请输入密码: ").strip()
    users[username] = hash_password(password)
    save_users(users)
    print("注册成功！")

def login():
    """用户登录"""
    users = load_users()
    username = input("请输入用户名: ").strip()
    password = input("请输入密码: ").strip()
    
    hashed = hash_password(password)
    if username in users and users[username] == hashed:
        print(f"登录成功，欢迎 {username}！")
    else:
        print("用户名或密码错误，登录失败。")

def main():
    while True:
        print("\n=== 用户系统 ===")
        print("1. 注册")
        print("2. 登录")
        print("3. 退出")
        choice = input("请选择功能: ").strip()
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("已退出系统。")
            break
        else:
            print("输入有误，请重新选择。")

if __name__ == "__main__":
    main()
