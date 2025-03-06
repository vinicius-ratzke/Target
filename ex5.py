def inverter_string(texto):
    resultado = ""
    for caractere in texto:
        resultado = caractere + resultado
    return resultado


entrada = input("Digite uma string: ")
print("String invertida:", inverter_string(entrada))
