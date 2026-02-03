print ("%" * 40)
print (" Analisis educativo " )
print ("%" * 50)


estudiante1 = ("Juan Gabriel ", 50, " Ingenieria ")
estudiante2 = (" Ricardo arjona ", 55, " Arquitectura ")
estudiante3 = (" Luis  Miguel ", 58, " Quimica ")


nombre1 , edad1 , carrera1 = estudiante1
nombre2 , edad2 , carrera2 = estudiante2
nombre3 , edad3 , carrera3 = estudiante3

print (f"\n{ nombre1 }, { edad1 } a o s , { carrera1 }")
print (f"{ nombre2 }, { edad2 } a o s , { carrera2 }")
print (f"{ nombre3 }, { edad3 } a o s , { carrera3 }")


matematica = {"Pedro ", " Juan ", " Patricia "}
programacion = {"Pedro ", " Patricia "}
fisica = {" Juan ", " Patricia "}

print ("\n" + "%" * 30)
print (" CURSOS :")


ambos = matematica . intersection ( programacion )
print (f"En Matematica y Programacion : { ambos }")

todos = matematica . union ( programacion , fisica )
print (f" Total estudiantes : {len ( todos )}")


print ("\n" + "%" * 40)
print (" VALIDACIONES :")

consulta = "Pedro "

en_mat = consulta in matematica
en_prog = consulta in programacion
puede_graduarse = en_mat and en_prog

print (f"{ consulta } en Matematica : { en_mat }")
print (f"{ consulta } en Programacion : { en_prog }")
print (f" Puede graduarse : { puede_graduarse }")

es_mayor_edad = edad1 >= 18
es_ingenieria = carrera1 == " Ingenieria "
print (f"\n{ nombre1 } es mayor de edad : { es_mayor_edad }")
print (f"{ nombre1 } estudia Ingenieria : { es_ingenieria }")

print ("\n" + "%" * 40)
