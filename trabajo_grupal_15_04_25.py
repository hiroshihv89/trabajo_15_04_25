import numpy as np

# Función para pedir vectores al usuario
def pedir_vector(nombre):
    entrada = input(f"Ingrese los elementos del vector {nombre} separados por comas: ")
    return np.array([int(x) for x in entrada.split(',')])

# Pedimos al usuario ingresar los vectores
print("=== Verificación de Propiedades con NumPy ===\n")
a = pedir_vector('a')
b = pedir_vector('b')
c = pedir_vector('c')
id = np.zeros_like(a)  # Vector identidad del mismo tamaño que 'a'

print("\nVectores ingresados:")
print("a =", a)
print("b =", b)
print("c =", c)
print()

# 1. Propiedad Conmutativa
print("Propiedad Conmutativa:")
print("a + b == b + a:", np.array_equal(a + b, b + a))
print("a * b == b * a:", np.array_equal(a * b, b * a))
print()

# 2. Propiedad Asociativa
print("Propiedad Asociativa:")
print("(a + b) + c == a + (b + c):", np.array_equal((a + b) + c, a + (b + c)))
print()

# 3. Propiedad Distributiva
print("Propiedad Distributiva:")
print("a * (b + c) == a * b + a * c:", np.array_equal(a * (b + c), a * b + a * c))
print()

# 4. Propiedad de Identidad
print("Propiedad de Identidad:")
print("a + 0 == a:", np.array_equal(a + id, a))
print()

# 5. Propiedad del Inverso
print("Propiedad del Inverso:")
print("a + (-a) == 0:", np.array_equal(a + (-a), id))
print()
