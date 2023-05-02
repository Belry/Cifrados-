import os

from ps4a import *
from ps4b import *
from ps4c import *

def get_archivo_string(url):
    f = open(url, "r")
    archivo = str(f.read())
    f.close()
    return archivo

def menu():
    print('Bienvenido. Seleccione una de las siguientes opciones: \n')

while True:
    menu()
    op = int(input('1. - Encriptar un archivo de texto\n2. - Desencriptar un archivo de texto\n\nOpción: '))
    if op == 1:
        url = input('\nIngrese la dirección del archivo que desea encriptar: ')
        print('Seleccione el método de encriptación:\n')
        op2 = int(input('1. - Cifrado César\n2. - Cifrado por sustitución\n\nOpción: '))
        if op2 == 1:
            k = int(input('\nIgrese el valor de corrimineto "k" (recuerde que debe ser un número entero positivo): '))
            archivo = get_archivo_string(url)
            plaintext = PlaintextMessage(archivo, k)
            print('\nEl texto encriptado es:', plaintext.get_message_text_encrypted())
            opcionMenu2 = input("\nSi desea volver al menu principal coloque 1. Si no desea volver al menu principal coloque 2. \nColoque una opción: ")
            if opcionMenu2=="2":
                break
        if op2 == 2:
            archivo = get_archivo_string(url)
            message = SubMessage(archivo)
            permutation = input('Ingrese el esquema de sustitución (recuerde escribir las 5 vocales): ')
            enc_dict = message.build_transpose_dict(permutation)
            print("El mensaje encriptado es:", message.apply_transpose(enc_dict))
            opcionMenu2 = input("\nSi desea volver al menu principal coloque 1. Si no desea volver al menu principal coloque 2. \nColoque una opción: ")
            if opcionMenu2=="2":
                break
        else:
            input('Presione cualquier tecla para regresar al menú principal \n')
    if op == 2:
        url = input('Ingrese la dirección del archivo que desea desencriptar: ')
        archivo = get_archivo_string(url)
        print(archivo)
        enc_message = EncryptedSubMessage(archivo)
        if enc_message.decrypt_message() is None:
            ciphertext = CiphertextMessage(archivo)
            print('El mensaje desencriptado es:', ciphertext.decrypt_message())
        else:
            print("El mensaje desencriptado es:", enc_message.decrypt_message())
        opcionMenu2 = input("\nSi desea volver al menu principal coloque 1. Si no desea volver al menu principal coloque 2. \nColoque una opción: ")
        if opcionMenu2=="2":
            break