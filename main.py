import random

Beleborda = "_-<>,.~`#@%$abcdefghigklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Long = int(input('Длинна пароля:'))
Password = ''
for i in range (Long):
    Password += random.choice(Beleborda)
print(Password)
