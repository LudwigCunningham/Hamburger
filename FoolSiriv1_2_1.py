#Тупой ассистент v1.2
import time
llogin = []
lpassword = []
print('Здравствуй!')
authorization = input("Вы хотите Войти или Reg? : ")
f = open('Login.txt', 'r')
print(f)
for list in f:
    llogin.append(list)
f = open('Password.txt', 'r')
for list in f:
    lpassword.append(list)
if authorization == 'Reg':
    login = input("Введите Логин: ")
    password = input("Введите Пароль: ")
    llogin.append(login)
    lpassword.append(password)
    print(llogin)
    print(lpassword)
    f = open('Login.txt', 'a')
    for index in llogin:
        f.write(index + " ")
    f.close()
    # f = open('Login.txt', 'r')
    # llogin = [line.strip() for line in f]
    # print(llogin)
    # f.close()
    f = open('Password.txt', 'a')
    for index in lpassword:
        f.write(index + " ")
    f.close()
    # f = open('Password.txt', 'r')
    # lpassword = [line.strip() for line in f]
    # print(lpassword)
    # f.close()
    print ("Вы удачно зарегестрировались! Приятного пользования... \n")

print(llogin)
print(lpassword)


login = input ("Введите Логин: ")
password = input ("Введите Пароль: ")
# print(llogin.index(login))
# print(lpassword.index(password))

if llogin.index(login) == lpassword.index(password):
    print("Доступ разрешен!")
    print('Здравствуй, {}! Я ТупаяСири, ваш тупойассистент. Единственное что я могу делать, это говорить время.\n Что бы узнать время, скажите мне время")'.format(login))
    operation = input ("Что мне сделать?\n ")
    if operation == "время" or "Время":
        print (time.ctime())
    else:
        print("Я так не умею")
"""
else:
    print("В доступо отказано")
"""
