import random
symwols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passlen = int(input('Введите длину пароля: '))
password =" "
for i in range(passlen):
    password += random.choice(symwols)
print(password)
