print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print ("=== CALCULADORA DE COMISIONES === ")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print ()


nombre = input (" Nombre del vendedor : ")
ventas = float ( input (" Venas mensuales : Q."))


comision = ventas * 13 / 100


print ()
print (f" Nombre del Vendedor : { nombre }")
print (f" Ventas totales : Q.{ ventas :.2f}")
print (f" Comisiones (13 %): Q.{ comision :.2f}")