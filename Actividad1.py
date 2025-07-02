Lista_Estudiantes =[] #Lista vacia de estudiantes

class Estudiante:
    def __init__(self, nombre, nota1, nota2, nota3, prom):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.promedio = prom

    def calcularProm(self):
        self.promedio = (self.nota1 + self.nota2 + self.nota3)/3

    def presentar(self):
        print(f'Nombre: {self.nombre} promedio: {self.promedio}')


def ingresoDatos():
    numero_Estudiantes = 0
    not1=0
    not2 =0
    not3=0

    numero_Estudiantes = int(input('Cuantos estudiantes desea agregar: '))
    for x in range(1, numero_Estudiantes+1, 1):
        print('\r\n')
        nombre_Tmp = input('Ingrese el nombre del estudiante')
        not1 = int(input('Ingrese la nota del primer curso: '))
        not2 = int(input('Ingrese la nota del segundo curso: '))
        not3 = int(input('Ingrese la nota del tercer curso: '))
        estudianteTmp = Estudiante(nombre_Tmp, not1, not2, not3,0)
        estudianteTmp.calcularProm()
        Lista_Estudiantes.append(estudianteTmp) #se añade un estudiante temporal al listado

def mostrarResultado():

    for tmp in Lista_Estudiantes:
        tmp.presentar()


fin=True

while fin:
    print('\r\t\r\t===Menu estudiantes===')
    opcion=1
    opcion = int(input('1.Ingresar estudiantes y sus calificaciones \r\n2.Mostrar Resultados \r\n3.Salir \r\n'))

    match opcion:
        case 1:
            ingresoDatos()
        case 2:
            if len(Lista_Estudiantes) == 0:
                print('Esta vacia la lista')
            else:
                mostrarResultado()
        case 3:
            print('Gracias por usar el programa')
            fin =False
        case _:
            print('Error esta opcion no existe')



