print ("#" * 50)
print (" PRODUCTOS ")
print ("#" * 50)


tienda = {
      "producto1": {
           "nombre": "Laptop Dell",
           "precio": 1250.00 ,
           "stock": 8,
           "categoria": " Computadoras "
        },
      "producto2": {
            "nombre": "Mouse Logitech",
            "precio": 35.50 ,
            "stock": 25,
            "categoria": "Accesorios"
         },
       "producto3": {
             "nombre": "Monitor Samsung",
             "precio": 450.00 ,
             "stock": 12,
             "categoria": "Monitores"
        }
 }


valor_total_inventario = 0

print ("\n=== CATALOGO DE PRODUCTOS ===\ n")


prod1 = tienda ["producto1"]
valor1 = prod1 ["precio"] * prod1 ["stock"]
valor_total_inventario = valor_total_inventario + valor1

print (f"Producto : { prod1 ['nombre']}")
print (f"Categoria: {prod1 ['categoria']}")
print (f"Precio unitario: Q.{prod1 ['precio']:.2f}")
print (f"Stock disponible: {prod1 ['stock']} unidades ")
print (f"Valor total: Q.{valor1 :.2f}")


prod2 = tienda ["producto2"]
valor2 = prod2 ["precio"] * prod2 ["stock"]
valor_total_inventario = valor_total_inventario + valor2

print (f"\nProducto : { prod2 ['nombre']}")
print (f" Categoria : { prod2 ['categoria']}")
print (f" Precio unitario : Q.{ prod2 ['precio']:.2f}")
print (f" Stock disponible : { prod2 ['stock']} unidades ")
print (f" Valor total : Q.{ valor2 :.2f}")


prod3 = tienda ["producto3"]
valor3 = prod3 ["precio"] * prod3 ["stock"]
valor_total_inventario = valor_total_inventario + valor3

print (f"\ nProducto : { prod3 ['nombre']}")
print (f" Categoria : { prod3 ['categoria']}")
print (f" Precio unitario : Q.{ prod3 ['precio']:.2f}")
print (f" Stock disponible : { prod3 ['stock']} unidades ")
print (f" Valor total : Q.{ valor3 :.2f}")


print ("\n" + "=" * 50)
print (" RESUMEN DEL INVENTARIO ")
print ("=" * 50)
print (f" Total de productos : {len( tienda )}")
print (f" Valor total del inventario : Q.{ valor_total_inventario :.2f}")
print ("=" * 50)