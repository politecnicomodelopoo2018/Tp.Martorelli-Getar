import json
from datetime import datetime

class jsonayuda(object):

    def decodificar(self):
        list_aux_vuelos = []
        list_aux_servicio = []
        list_aux_aviones = []
        list_aux_pasajeros = []

        f = open("datos.json","r")
        dic_aux = json.loads(f.read())
        f.close
        for item in dic_aux["Aviones"]:
            a = aviones()
            a.json(item)
            list_aux_aviones.append(a)
        for item in dic_aux["Personas"]:
            if item["tipo"] == "Pasajero":
                a = pasajero()
                a.json(item)
                list_aux_pasajeros.append(a)
            if item["tipo"] == "Servicio":
                a = servicio()
                a.json(item)
                list_aux_servicio.append(a)
            if item["tipo"] == "Piloto":
                a = pilotos()
                a.json(item)
                list_aux_servicio.append(a)
        for item in dic_aux["Vuelos"]:
            a = vuelo()
            a.json(item)
            list_aux_vuelos.append(a)

        for item in list_aux_servicio:
            list_aux_para_aviones_modelo = []
            for item2 in item.aviones:
                for item3 in list_aux_aviones:
                    if item2 == item3.modelo:
                        list_aux_para_aviones_modelo.append(item3)
            item.aviones = list_aux_para_aviones_modelo

        for item in list_aux_vuelos:
            list_aux_para_tripulacion_dni = []
            for item2 in item.tripulacion:
                for item3 in list_aux_servicio:
                    if item3.dni == int(item2):
                        list_aux_para_tripulacion_dni.append(item3)
            item.tripulacion = list_aux_para_tripulacion_dni

            list_aux_para_pasajeros_dni = []
            for item2 in item.pasajeros:
                    for item3 in list_aux_pasajeros:
                        if item3.dni == int(item2):
                            list_aux_para_pasajeros_dni.append(item3)
            item.pasajeros = list_aux_para_pasajeros_dni

            for item2 in list_aux_aviones:
                if item.avion == item2.modelo:
                    item.avion = item2
        return list_aux_vuelos

class persona(object):
        dni = None
        nombre = None
        apellido = None
        fecha_Nac = None

class pasajero(persona):
        vip = None
        especial = None

        def diferente(self):

            if self.vip == 1:
                return True
            if self.especial is not None:
                return True
            return False

        def json(self,item):
            self.dni = int(item["dni"])
            self.nombre = item["nombre"]
            self.apellido = item["apellido"]
            self.fecha_Nac = datetime.strptime(item["fechaNacimiento"], '%Y-%m-%d').date()
            self.vip = int(item["vip"])
            self.especial = None
            try:
                self.especial = item["solicitudesEspeciales"]
            except KeyError:
                pass

class pilotos(persona):
        pass

        def __init__(self):
            self.aviones=[]

        def vuelos_Autri(self,avion):
            if avion not in self.aviones:
                    return False
            return True

        def json(self,item):
            self.dni = int(item["dni"])
            self.nombre = item["nombre"]
            self.apellido = item["apellido"]
            self.fecha_Nac = datetime.strptime(item["fechaNacimiento"], '%Y-%m-%d').date()
            self.aviones = item["avionesHabilitados"]

class servicio(persona):
        pass

        def __init__(self):
            self.aviones = []
            self.idiomas = []

        def vuelos_Autri(self,avion):
            if avion not in self.aviones:
                    return False
            return True

        def json(self,item):
            self.dni = int(item["dni"])
            self.nombre = item["nombre"]
            self.apellido = item["apellido"]
            self.fecha_Nac = datetime.strptime(item["fechaNacimiento"], '%Y-%m-%d').date()
            self.aviones = item["avionesHabilitados"]
            self.idiomas = item["idiomas"]

class aviones(object):
        modelo = None
        cant_pasa = None
        cant_trip = None

        def json(self,item):
            self.modelo = item["codigoUnico"]
            self.cant_pasa = item["cantidadDePasajerosMaxima"]
            self.cant_trip = item['cantidadDeTripulacionNecesaria']

class vuelo(object):
        avion = None
        fecha = None
        hora = None
        origen = None
        destino = None

        def __init__(self):
            self.tripulacion = []
            self.pasajeros = []

        def json(self,item):
            self.avion = item["avion"]
            self.dia = datetime.strptime(item["fecha"], '%Y-%m-%d').date()
            self.hora = datetime.strptime(item["hora"],'%H:%M')
            self.origen = item["origen"]
            self.destino = item["destino"]
            self.tripulacion = item["tripulacion"]
            self.pasajeros = item["pasajeros"]

        def personas_En_Vuelo(self):

            l = []
            l.append(self.destino)
            list_aux = l + self.pasajeros
            return list_aux
        #2
        def menor_Pasajero(self):
            menor = self.pasajeros[0]
            for item in self.pasajeros:
                if item.fecha_Nac > menor.fecha_Nac:
                    menor = item
            return menor

        #3
        def tripulacion_Min(self):
            if self.avion.cant_trip > len(self.tripulacion):
                return "No puede volar"
            return "Puede volar"

        #4
        def trip_No_Autori(self):
            for item in self.tripulacion:
                if not item.vuelos_Autri(self.avion):
                        return False
            return True

        #6
        def vip_Esp(self):
            list_aux=[]
            for item in self.pasajeros:
               if item.diferente():
                   list_aux.append(item)
            return list_aux

        #7

        def Idiomas(self):
            list_aux=[]
            for item in self.tripulacion:
                tipo = item.__class__.__name__
                if 'servicio' == tipo:
                    for idiomas_dentro_lista in item.idiomas:
                        if not idiomas_dentro_lista in list_aux:
                            list_aux.append(idiomas_dentro_lista)
            return list_aux


class object(object):

        vuelos = []

        def personas_en_vuelo(self,hora,dia):

            for item in self.vuelos:

                if hora == item.hora and item.dia == dia:
                     return  item.personas_En_Vuelo()

        def menor_pasajero(self,hora,dia):

            for item in self.vuelos:
                if hora == item.hora and item.dia == dia:
                    pasajero_mas_chico=item.menor_Pasajero()
                    return pasajero_mas_chico

        def tripulacion_min(self,hora,dia):

            for item in self.vuelos:
                if hora == item.hora and item.dia == dia:
                    cumple=item.tripulacion_Min()
                    return cumple

        def trip_no_autori(self,hora,dia):

            for item in self.vuelos:
                if hora == item.hora and item.dia == dia:
                    cumple = item.trip_No_Autori()
                    if cumple:
                        return "Toda la tripulacion esta autorizada"
                    return "No puede volar"


        def vip_esp(self,hora,dia):

            for item in self.vuelos:
                if hora == item.hora and item.dia == dia:
                    list_vip_esp = item.vip_Esp()
                    return list_vip_esp


        def idiomas(self,hora,dia):

            list_habla = []
            for item in self.vuelos:
                if hora == item.hora and item.dia == dia:
                    list_habla = item.Idiomas()
            return list_habla

        def rompe_regla(self):
            list_aux = []
            for item in self.vuelos:
                for item2 in self.vuelos:
                    if item.dia == item2.dia and item.origen is not item2.origen and item.destino is not item2.destino:
                        for item3 in item.tripulacion:
                            for item4 in item2.tripulacion:
                                if item4 == item3:
                                    if not item4 in list_aux:
                                        list_aux.append(item4)
            return list_aux
