#!/usr/bin/env python
# -*- coding: utf-8 -*-
from validacion import metodos, valores
import unittest


class testMall(unittest.TestCase):

    def test_validar_solo_caracteres(self):
        self.assertTrue(metodos.verificarSoloCaracteres('35'))


    def test_validarnumero(self):
        self.assertTrue(metodos.validarSoloNumeros('10'))

    def test_validarEntero(self):
        self.assertTrue(metodos.validarEntero(10))

    def test_validar_rango(self):
        self.assertTrue(metodos.validarRango(0,20000,10))

    def test_validarfecha(self):
        self.assertTrue(metodos.validarFormatoFecha('1799-01-01'))

    def test_validarvalor(self):
        self.assertTrue(metodos.validarValorRespuesta(2, valores.dict_Etnia))

    def test_validarsegundonombre(self):
        self.assertTrue(metodos.validarSegundoNombre("carlos jose"))

    def test_validarfechacodifo(self):
        self.assertTrue(metodos.validarFechaCodigos('1799-01-01'))

    def test_validarfechalista(self):
        self.assertTrue(metodos.validarFechaSinDato('1799-01-01'))

    def test_validarSoloNumeroSincomas(self):
        self.assertTrue(metodos.validarSoloNumeros(3.5))

    def test_validarFechaDefecto(self):
        self.assertTrue(metodos.validarFechaPorDefecto('1999-01-01', '1799-01-01'))

    def test_fechaActual(self):
        self.assertTrue(metodos.validarFechaActual('2017-11-01'))



if __name__ == '__main__':
    unittest.main()