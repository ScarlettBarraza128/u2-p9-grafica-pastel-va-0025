# Emily Barraza NC = 0025

import matplotlib.pyplot as plt

# 1 y 2. Datos: 5 materias con sus respectivas calificaciones
materias = ['Matemáticas', 'Física', 'Química', 'Programación', 'Inglés']
calificaciones = [95, 88, 75, 100, 90]

# Crear la gráfica de pastel (Pie Chart)
plt.pie(calificaciones, labels=materias, autopct='%1.1f%%', startangle=140)

# 3 y 4. Título, xlabel e ylabel
plt.title("Distribución de calificaciones NC = 0025")
plt.xlabel("Materias evaluadas")
plt.ylabel("")

# Guardar la imagen para el leeme.md
plt.savefig("grafica_pastel.png", bbox_inches='tight')

# Mostrar la gráfica
plt.show()

# 6. Imprimir al final el nombre completo y número de control
print("Emily Barraza NC 0025")