import datetime

boleta = {}     #Diccionario
rut_cliednte = input("Ingrese rut del Cliente, para asociarlo a sus puntos:")
correo_cliente = input("Ingrese correo del cliente para su boleta virtual:")
fecha_actual = datetime.date.today()
boleta['rut_cliente'] = rut_cliednte
boleta['correo_cliente'] = correo_cliente
boleta['fecha_actual'] = fecha_actual

print(boleta)