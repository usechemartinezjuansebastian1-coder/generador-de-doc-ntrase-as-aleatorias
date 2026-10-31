print ("generador de contraseñas")
letrasminuculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letrasmayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

todosloscaracteres = letrasminuculas + letrasmayusculas + numeros + simbolos
longitud = int(input("ingrese la longitud de la clave: "))
contraseñafinal = ""

for i in range(longitud):
    posicionaleatoria = (i *7+3) % len(todosloscaracteres)
    contraseñafinal = contraseñafinal + todosloscaracteres[posicionaleatoria]

print (f"\n su contraseña es: {contraseñafinal} con longitud {longitud}")
