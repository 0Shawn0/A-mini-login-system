import pymysql

print("Welcom to Database login-system！")

db = pymysql.connect(host="localhost",
                     user="testuser",
                     password="testpwd",
                     db="testdb",
                     port=3306)

cursor = db.cursor()


def execute(s):
    cursor.execute(s)
    db.commit()


def get():
    return str(list(cursor.fetchone())[0])


def login():
    print("-------------*Login*-------------")

    username = input("Input username：")
    pwd = input("Input password: ")

    execute(f"select count(*) from user where username='{username}';")

    p1 = get()

    if p1 == '1':
        execute(f"select password from user where username='{username}';")

        p2 = get()

        if p2 == pwd:
            print("Sucessfully Login！")
        else:
            print("Wrong username or password！")
    else:
        print("Wrong username or password！")


def register():
    print("-------------*Register*-------------")
    username = input("Input username：")
    pwd1 = input("Input password: ")
    pwd2 = input("Input password again: ")
    if pwd1 != pwd2:
        print("Two different passwords!")
        return

    execute(f"INSERT INTO user VALUES('{username}','{pwd1}');")

    print("Sucessfully register!")


def change():
    print("-------------*Change Password*-------------")
    username = input("Input username：")
    pwd1 = input("Input old password: ")
    pwd2 = input("Input new password: ")
    execute(f"select count(*) from user where username='{username}';")
    p1 = get()
    if p1 == '1':
        execute(f"select password from user where username='{username}';")
        p2 = get()
        if p2 == pwd1:
            execute(f"update user set password = '{pwd2}' where username = '{username}';")
            print("Succesfully changed password!")
        else:
            print("Wrong username or password！")
    else:
        print("Wrong username or password！")


while True:
    op = int(input("Enter operation: 1-Login 2-Register 3-Change Password 4-Quit"))
    if op == 1:
        login()
    if op == 2:
        register()
    if op == 3:
        change()
    if op == 4:
        break
