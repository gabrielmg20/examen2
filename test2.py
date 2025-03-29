# test2.py

# Pedir el tamaño de la lista
tamaño = int(input("¿Cuántos nombres de alumnos deseas ingresar? "))

# Crear la lista vacía
nombres = []

# Ingresar los nombres
for i in range(tamaño):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nombres.append(nombre)

# Mostrar resultados
print(f"\nTamaño final de la lista: {len(nombres)}")
print("Nombres ingresados:")
for nombre in nombres:
    print(nombre)