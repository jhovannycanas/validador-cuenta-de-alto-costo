#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import datetime

SOLO_CARACTERES = re.compile("^[A-Za-z 0-9_-]*$")
dict_mensajes = {1: "El texto ingresado contiene caracteres especiales: %s en la columna %s en la fila %s",
                 2: "El texto ingresado no corresponde a un numero: %s en la columna %s en la fila %s",
                 3: "El texto ingresado no corresponde a una fecha valida que cumpla el siguiente formato:"
                    "(AAAA-MM-DD) o la fecha ingresada es menor a 1900: %s en la columna %s en la fila %s",
                 4: "El valor ingresado no es una respuesta valida: %s en la columna %s en la fila %s",
                 5:"El valor ingresado no corresponde a un segundo nombre: %s en la columna %s en la fila %s",
                 6: "El valor ingresado no corresponde a una fecha validad o una fecha admisible: %s en la columna %s en la fila %s",
                 7: "El campo no puede ser nulo o vacio: %s en la columna %s en la fila %s",
                 8:"La ubicación del nombre  de la columna: %s , no corresponde al orden esperado, "
                   "se esperaba el siguiente nombre para la columna: %s ,en su lugar"}

fechas_convertir = [9, 15, 16, 17, 18, 39, 42, 44, 49, 93, 97, 106, 141, 144,146]
fechas_por_defecto = [16,17, 18,39,42, 44,49,93,97,106,141, 144,146]

def validarEntero(numero):
        return not isinstance(numero, float)

def verificarSoloCaracteres(texto):
    if isinstance(texto,int):
        return True
    if isinstance(texto,float):
        return False
    if isinstance(texto, datetime.datetime):
        return (True, None)
    return SOLO_CARACTERES.match(texto) is not None


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
    if validarSoloNumeros(sinDato) and sinDato == 300:
        return True
    if validarSoloNumeros(numero) and validarEntero(numero):
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

def generarMensajeInconsistencia(df, dfData, columna, tipoerror):
    mensajes = []
    for i, row in df[columna].iteritems():
        if row == False:
            mensajes.append(dict_mensajes.get(tipoerror) % (dfData.get_value(i, columna),columna, i ))
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
            fecha = fecha - datetime.timedelta(days=1)
            return fecha
        else:
            return fecha
    else:
        return fecha


