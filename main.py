import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

numero = int(input("Introduce la longitud de la contraseña: "))

password = ""
for _ in range(numero):

    password += random.choice(characters)

print("Contraseña generada:", password)