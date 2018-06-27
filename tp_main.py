from clases import *

cargar_datos = jsonayuda()
listas_vuelos = cargar_datos.decodificar()
sistema = object()
sistema.vuelos = listas_vuelos

lista_de_persona_ej1 = []
lsita_de_persona_ej2 = []
lsita_de_persona_ej3 = []
lsita_de_persona_ej4 = []
lsita_de_persona_ej5 = []
lsita_de_persona_ej6 = []
lsita_de_persona_ej7 = []

for item in sistema.vuelos:
    lista_de_persona_ej1.append(sistema.personas_en_vuelo(item.hora,item.dia))
    lsita_de_persona_ej2.append(sistema.menor_pasajero(item.hora,item.dia))
    lsita_de_persona_ej3.append(sistema.tripulacion_min(item.hora,item.dia))
    lsita_de_persona_ej4.append(sistema.trip_no_autori(item.hora,item.dia))
    lsita_de_persona_ej5.append(sistema.vip_esp(item.hora,item.dia))
    lsita_de_persona_ej6.append(sistema.idiomas(item.hora,item.dia))
    lsita_de_persona_ej7.append(sistema.rompe_regla())

for item in lsita_de_persona_ej2:
    print(item.nombre)