#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import datetime

SOLO_CARACTERES = re.compile("^[A-Za-z 0-9_-]*$")
SOLO_TEXTO= re.compile("^[A-Za-z -]*$")
dict_mensajes = {1: "El texto ingresado contiene caracteres especiales: %s en la columna %s en la fila %s;"
                    "tambien puede deberse a que ingreso un numero con comas o puntos",
                 2: "El texto ingresado no corresponde a un numero: %s en la columna %s en la fila %s",
                 3: "El texto ingresado no corresponde a una fecha valida que cumpla el siguiente formato:"
                    "(AAAA-MM-DD) o la fecha ingresada es menor a 1900: %s en la columna %s en la fila %s",
                 4: "El valor ingresado no es una respuesta valida: %s en la columna %s en la fila %s; "
                    "por favor verificar el dato ingresado que si corresponda al esperado",
                 5:"El valor ingresado no corresponde a un segundo nombre: %s en la columna %s en la fila %s;"
                   "por favor verificar si el valor ingresado corresponde al esperado, o si contiene mas de dos "
                   "espacios en blanco",
                 6: "El valor ingresado no corresponde a una fecha validad o una fecha admisible: %s en la columna %s en la fila %s",
                 7: "El campo no puede ser nulo o vacio: %s en la columna %s en la fila %s",
                 8:"La ubicación del nombre  de la columna: %s , no corresponde al orden esperado, "
                   "se esperaba el siguiente nombre para la columna: %s ,en su lugar",
                9:"El valor ingresado no corresponde a un tipo de documento para regimen subsidiado: %s en la columna %s en la fila %s;"
                   "por favor verificar si el valor ingresado corresponde al esperado"}


fechas_convertir = [9, 15, 16, 17, 18, 39, 42, 44, 49, 93, 97, 106, 141, 144,146]
fechas_por_defecto = [16,17, 18,39,42, 44,49,93,97,106,141, 144,146]
mayusculas_noespacio =[3,4,5,6]
numeros_convertir = [2,8,11,13,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,
                     40,41,43,45,46,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,
                     66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,
                     90,91,92,94,95,96,98,99,100,101,102,103,104,105,107,108,109,110,111,112,
                     113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,
                     132,133,134,135,136,137,138,142,143,145,147,148,149,150,151]

def validarEntero(numero):
        return not isinstance(numero, float)

def verificarSoloCaracteres(texto):
    if isinstance(texto,int):
        return True
    if isinstance(texto,float):
        return False
    if isinstance(texto, datetime.datetime):
        return (True, None)
    if isinstance(texto, long):
        return True
    return SOLO_CARACTERES.match(texto) is not None

def validarsolotexto(texto):
    if validarSoloNumeros(texto):
        return False
    return SOLO_TEXTO.match(texto) is not None

def validarSoloNumeros(numero):
    try:
        int(numero)
        return True
    except Exception:
        return False

def validarRango(intervaloInferior, intervaloSuperior, numero):
    if validarSoloNumeros(numero) and validarEntero(numero):
        return intervaloInferior <= numero <= intervaloSuperior


# def validarFormatoFecha(fecha):
#     try:
#         if isinstance(fecha, datetime.datetime):
#              datetime.datetime.strftime(fecha, '%Y-%m-%d')
#             return True
#     except Exception as e:
#         print(e.message)
#         return False

def validarFormatoFecha(fecha):
    try:
        if isinstance(fecha, unicode):
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
        if isinstance(fecha, str):
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
        if isinstance(fecha, datetime.datetime):
            if fecha.year <= 1900:
                pass
            else:
                datetime.datetime.strftime(fecha, '%Y-%m-%d')
        return True
    except Exception as e:
        print(e.message)
        return False

def validarValorRespuesta(valor, valores):
    return valor in valores.keys()

def validarEspacio(nombre):
    return not len(nombre.split(' ')) > 2

def validarSegundoNombre(nombre):
    if nombre == "NONE":
        return True
    if not validarsolotexto(nombre):
        return False
    return validarEspacio(nombre)


def validarFechaCodigos(fecha):
    fechaCuenta = datetime.datetime.strptime(fecha, '%Y-%m-%d')
    if fechaCuenta.year <= 1822:
        return True
    return False

def validarFechaSinDato(fecha):
    if fecha.year <= 1822:
        listafechas = ['1799-01-01','1800-01-01','1811-01-01','1822-01-01']
        fechas_defectos = [datetime.datetime.strptime(x, '%Y-%m-%d').date() for x in listafechas]
        print(fecha in fechas_defectos)
        return fecha in fechas_defectos
    return True


def validarPrimerNombre(nombre):
    return not len(nombre.split(' ')) > 1

def validarSegundoApellido(apellido):
    if apellido == "NOAP":
        return True
    return validarPrimerNombre(apellido)

def validarRangoSinDato(intervaloInferior, intervaloSuperior,sinDato, numero):
    if not validarSoloNumeros(numero):
        return False
    if numero == sinDato == 300:
        return True
    if not validarEntero(numero):
        return False
    return intervaloInferior <= numero <= intervaloSuperior

def validar_SindecimalesSinComas(numero):
    if isinstance(numero, float):
        return False
    return validarSoloNumeros(numero)

def validarFechaPorDefecto(fecha, fechasindato):
    if fecha == datetime.datetime.strptime(fechasindato,'%Y-%m-%d'):
        return True
    return validarFormatoFecha(fecha)

def validarInconsistenciaColumna(df, columna):
    return False in df[columna].values

def generarMensajeInconsistencia(df, dfData, columna, tipoerror, tipo):
    mensajes = []
    for i, row in df[columna].iteritems():
        if row == False:
            mensajes.append(dict_mensajes.get(tipoerror) % (dfData.get_value(i, columna),columna, i + tipo))
    return mensajes


def validarOrdenColumnas(datos, columnasMalla):
    columnasErroneas = []
    for columnaDato in datos.columns:
        indiceColumna =  datos.columns.get_loc(columnaDato)
        if columnasMalla.get(indiceColumna) is not None:
            if columnasMalla.get(indiceColumna).decode('utf-8') != columnaDato.replace("\n"," "):
                columnasErroneas.append(indiceColumna)
    return columnasErroneas


def validarFechaActual(fecha):
    fecha = datetime.datetime.strptime(fecha,'%Y-%m-%d')
    return fecha.date() <= datetime.datetime.today().date()


def resaltar_error(dato):
    return ['background-color: yellow' if dato is True else '']


def ajustarfecha(fecha):
    if isinstance(fecha,datetime.date):
        if fecha.year<=1900:
            #fecha = fecha - datetime.timedelta(days=1)
            return fecha
        else:
            return fecha
    else:
        return fecha


########################################################################

def validartipoidentitifacion(row):
    if row[1]!='S':
        if (row[7] =='MS' or row[7] =='AS'):
            return False
    return True