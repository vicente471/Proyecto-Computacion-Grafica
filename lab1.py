#
# Programa: lab1.py implementación del algoritmo de Bresenham
# Autores : Vicente Santos 
#           Cristobal Gallardo         
# Fecha   : 22/10/2024

# Importar bibliotecas necesarias
from graphics import *

# Definir funciones
def draw_pixel_grid(window, width, height, pixel_size):
    # Dibuja una cuadrícula de píxeles con el origen en el centro
    half_width = width // 2
    half_height = height // 2
    
    for x in range(-half_width, half_width, pixel_size):
        for y in range(-half_height, half_height, pixel_size):
            rect = Rectangle(Point(x, y), Point(x + pixel_size, y + pixel_size))
            rect.setOutline("lightgray")
            rect.draw(window)

    # Dibuja los ejes X e Y
    x_axis = Line(Point(-half_width, 0), Point(half_width, 0))  # Eje X
    y_axis = Line(Point(0, -half_height), Point(0, half_height))  # Eje Y
    x_axis.setFill("black")
    y_axis.setFill("black")
    x_axis.draw(window)
    y_axis.draw(window)

def draw_pixel(x, y, window, pixel_size, color="black"):
    # Dibuja un píxel grande en la ventana, ajustando para el origen centrado
    rect = Rectangle(Point(x, y), Point(x + pixel_size, y + pixel_size))
    rect.setFill(color)
    rect.draw(window)

def PlotPoint(xc, yc, x, y, win, pixel_size):
    # Dibuja los puntos simétricos
    draw_pixel(xc + x, yc + y, win, pixel_size)
    draw_pixel(xc - x, yc + y, win, pixel_size)
    draw_pixel(xc + x, yc - y, win, pixel_size)
    draw_pixel(xc - x, yc - y, win, pixel_size)
    draw_pixel(xc + y, yc + x, win, pixel_size)
    draw_pixel(xc - y, yc + x, win, pixel_size)
    draw_pixel(xc + y, yc - x, win, pixel_size)
    draw_pixel(xc - y, yc - x, win, pixel_size)

def LineaBresenham():
    print("\nEntrando a Unir 2 puntos con una Recta")  
    # Tamaño de la ventana y tamaño del píxel
    width = 1000
    height = 1000
    pixel_size = 25  # Tamaño de cada píxel en la retícula
    
    print("\nPunto 1:")
    x1 = leer_variable("Ingrese la coordenada x: ")
    y1 = leer_variable("Ingrese la coordenada y: ")
    print("\nPunto 2:")
    x2 = leer_variable("Ingrese la coordenada x: ")
    y2 = leer_variable("Ingrese la coordenada y: ")

    # Crear ventana y definir el sistema de coordenadas con el origen en el centro
    win = GraphWin("Bresenham Line Drawing with Pixel Grid", width, height)
    win.setCoords(-width // 2, -height // 2, width // 2, height // 2)  # Centrar el origen
    draw_pixel_grid(win, width, height, pixel_size)

    draw_pixel(0, 0, win, pixel_size, color="blue")
    # Algoritmo de Bresenham
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    # Inicializar parámetro de decisión p
    if dx > dy:  # Si la línea es más horizontal que vertical
        p = 2 * dy - dx
        incE = 2 * dy
        incNE = 2 * (dy - dx)

        x, y = x1, y1
        while x != x2 or y != y2:
            draw_pixel(x * pixel_size, y * pixel_size, win, pixel_size)
            if x == x2 and y == y2:  # Chequeo de finalización
                break
            x += sx
            if p < 0:
                p += incE
            else:
                y += sy
                p += incNE
    else:  # Si la línea es más vertical que horizontal
        p = 2 * dx - dy
        incE = 2 * dx
        incNE = 2 * (dx - dy)

        x, y = x1, y1
        while x != x2 or y != y2:
            draw_pixel(x * pixel_size, y * pixel_size, win, pixel_size)
            if x == x2 and y == y2:  # Chequeo de finalización
                break
            y += sy
            if p < 0:
                p += incE
            else:
                x += sx
                p += incNE

    # Esperar a que el usuario cierre la ventana
    if not win.isClosed():
        win.getMouse()
    win.close()

def CircleBresenham():
    print("\n\tEntrando a Dibujar un Circulo")
    # Tamaño de la ventana y tamaño del píxel
    width = 1000
    height = 1000
    pixel_size = 25

    print("\nPunto Centro y el radio")
    x1 = leer_variable("Ingrese la coordenada x: ")
    y1 = leer_variable("Ingrese la coordenada y: ")
    r = leer_variable("Ingrese el radio: ")

    # Inicializar la ventana
    win = GraphWin("Bresenham Circle Drawing with Pixel Grid", width, height)
    win.setCoords(-width // 2, -height // 2, width // 2, height // 2)

    # Dibujar la cuadrícula de píxeles
    draw_pixel_grid(win, width, height, pixel_size)
    draw_pixel(0, 0, win, pixel_size, color="blue")
    x = 0
    y = r
    p = 1 - r

    # Dibuja el primer punto
    PlotPoint(x1 * pixel_size, y1 * pixel_size, x * pixel_size, y * pixel_size, win, pixel_size)
    
    # Repite hasta trazar el octante
    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1
        PlotPoint(x1 * pixel_size, y1 * pixel_size, x * pixel_size, y * pixel_size, win, pixel_size)


    # Esperar a que el usuario haga clic antes de cerrar la ventana
    if not win.isClosed():
        win.getMouse()
    win.close()

def Representacion_Elipse():
    print("\nEntrando a Representacion de la Elipse")   
    width = 1000
    height = 1000
    pixel_size = 25

    print("\nPunto 1:")
    xc = leer_variable("Ingrese la coordenada x: ")
    yc = leer_variable("Ingrese la coordenada y: ")

    print("\nPunto 2:")
    a = leer_variable("Ingrese la coordenada a: ")
    b = leer_variable("Ingrese la coordenada b: ")

    # Inicializar la ventana
    win = GraphWin("Elipse Drawing", width, height)
    win.setCoords(-width // 2, -height // 2, width // 2, height // 2)

    draw_pixel_grid(win, width, height, pixel_size)
    draw_pixel(0, 0, win, pixel_size, color="blue")
    # Algoritmo de Bresenham para la elipse
    points = []
    x = 0
    y = b
    p1 = b**2 - a**2 * b + 0.25 * a**2

    # Primer segmento
    while (b**2 * x) < (a**2 * y):
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))
        
        if p1 < 0:
            x += 1
            p1 += 2 * b**2 * x + b**2
        else:
            x += 1
            y -= 1
            p1 += 2 * b**2 * x - 2 * a**2 * y + b**2

    p2 = b**2 * (x + 0.5)**2 + a**2 * (y - 1)**2 - a**2 * b**2

    # Segundo segmento
    while y > 0:
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))
        
        if p2 > 0:
            y -= 1
            p2 -= 2 * a**2 * y + a**2
        else:
            y -= 1
            x += 1
            p2 += 2 * b**2 * x - 2 * a**2 * y + a**2

    for (px, py) in points:
        draw_pixel(px * pixel_size, py * pixel_size, win, pixel_size)

    # Esperar a que el usuario haga clic antes de cerrar la ventana
    if not win.isClosed():
        win.getMouse()
    win.close()
                 

def Representacion_Parabola():
    print("\nEntrando a Representación de la Parabola")   
    # Tamaño de la ventana y tamaño del píxel
    width = 1000
    height = 1000
    pixel_size = 25  # Tamaño de cada píxel en la retícula

    # Crear ventana y definir el sistema de coordenadas con el origen en el centro
    win = GraphWin("Bresenham Line Drawing with Pixel Grid", width, height)
    win.setCoords(-width // 2, -height // 2, width // 2, height // 2)  # Centrar el origen
    draw_pixel_grid(win, width, height, pixel_size)
    x = 0 
    y = 0 
    p = 1

    draw_pixel(x * pixel_size, y * pixel_size, win, pixel_size)
    draw_pixel(x * pixel_size, -y * pixel_size, win, pixel_size)

    while(x < 100):
        x += 1
        if (p > 0):
            y += 1
            p = p - 2 * y + 1
        else:
            p += 1
        draw_pixel(x * pixel_size, y * pixel_size, win, pixel_size)
        draw_pixel(x * pixel_size, -y * pixel_size, win, pixel_size)

    # Esperar a que el usuario haga clic antes de cerrar la ventana
    if not win.isClosed():
        win.getMouse()
    win.close()

def salir():
    print('\n Saliendo...')

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def leer_variable(nombre):
    while True:
        a = input(f'{nombre} ')
        try:
            a = int(a)
            return a
        except ValueError:
            print('La variable no es un número entero, vuelva a intentarlo.')

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla


# Función principal
def main():
    # Inicialización de variables

    # LLamar al menu
    print("\n\tBienvenidos al Programa de Representaciones Graficas")
    print("\nAutores : \n  Vicente Santos\n  Cristobal Gallardo")
    print("\n\n")
    print("El punto (0,0) se mostrara en azul")
    input("\n\nPresiona Enter para continuar...")
    print("\n\nMenu:")
    opciones = {
        '1': ('Dibujar la recta entre dos puntos',LineaBresenham),
        '2': ('Dibujar una circunferencia',CircleBresenham),
        '3': ('Representar y Dibujar una Elipse',Representacion_Elipse),
        '4': ('Representar y Dibujar una Parabola', Representacion_Parabola),
        '5': ('Salir', salir)
    }
    generar_menu(opciones, '5')

# Comprobar si este script se está ejecutando directamente

main()