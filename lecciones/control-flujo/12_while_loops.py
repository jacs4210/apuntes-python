"""
Lección 12: Bucles While (while loops)

Descripción:
Esta lección cubre el uso del bucle while en Python. Aprenderás a repetir instrucciones mientras se 
cumpla una condición, cómo controlar el ciclo con un contador y cómo evitar bucles infinitos.

Objetivos:
- Comprender cómo funciona el bucle while
- Usar un contador para controlar la repetición
- Evitar bucles infinitos
- Escribir programas que repitan acciones hasta que se cumpla una condición

Conceptos Clave:
- while: Repite un bloque mientras la condición sea True
- Contador: Variable que cambia en cada iteración
- break: Sale del bucle antes de que la condición sea False (opcional)
- continue: Salta a la siguiente iteración (opcional)

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/controlflow.html#while-statements
- Tutorial de bucles: https://realpython.com/python-while-loop/

Autor: Jairo Cuartas
Fecha: 2025-07-20
"""

# =============================================================================
# EJEMPLO 1: Bucle while básico con contador
# =============================================================================
# Se define un contador que garantiza que el ciclo se detenga cuando la condición sea False.
i = 1

while i <= 5:
    print(i)
    i += 1  # El contador aumenta en 1 para que la condición eventualmente sea False
# Salida esperada:
# 1
# 2
# 3
# 4
# 5

print('Hecho')  # Salida esperada: Hecho

# =============================================================================
# EJEMPLO 2: Bucle while con break
# =============================================================================
contador = 1
while True:
    print(f"Iteración {contador}")
    if contador == 3:
        print("¡Se alcanzó el límite, saliendo del bucle!")
        break
    contador += 1
# Salida esperada:
# Iteración 1
# Iteración 2
# Iteración 3
# ¡Se alcanzó el límite, saliendo del bucle!

# =============================================================================
# EJEMPLO 3: Bucle while con continue
# =============================================================================
numero = 0
while numero < 5:
    numero += 1
    if numero == 3:
        continue  # Salta la impresión cuando numero es 3
    print(f"Número: {numero}")
# Salida esperada:
# Número: 1
# Número: 2
# Número: 4
# Número: 5

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Escribe un programa que imprima los números del 10 al 1 usando while
# 2. Escribe un programa que sume los números del 1 al 100 usando while
# 3. Escribe un programa que pida al usuario un número y repita hasta que ingrese 0

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. El bucle while repite mientras la condición sea True
2. Es fundamental modificar la variable de condición dentro del bucle
3. break permite salir del bucle antes de que la condición sea False
4. continue salta a la siguiente iteración
5. Cuidado con los bucles infinitos (condición nunca se vuelve False)
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# i = 10
# while i > 0:
#     print(i)
#     i -= 1
# print('Cuenta regresiva finalizada')