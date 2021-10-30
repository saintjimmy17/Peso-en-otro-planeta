peso = int(input("Cual es tu peso?: "))
planeta = input("Elige que planeta quiere. 1 es Marte y 2 es Jupiter: ")
g_tierra = 9.8
g_marte = 3.7
g_jupiter = 24.8

if planeta == "1":
    peso_final = peso * g_marte / g_tierra
    print("Tu peso en Marte es: ", round(peso_final, 2))
elif planeta == "2":
    peso_final = peso * g_jupiter / g_tierra
    print("Tu peso en Jupiter es: ", round(peso_final, 2))
else:
    print("No has elegido un planeta valido")
