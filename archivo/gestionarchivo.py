#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import pandas.io.excel

#pasar un diccionario en el constructor
#https://stackoverflow.com/questions/42579427/use-from-dict-to-initialize-a-subclass-of-pandas-dataframe/42580274#42580274

#crear propiedades en una clase existente
#https://stackoverflow.com/questions/22155951/how-to-subclass-pandas-dataframe

#instalar paquetes en una version diferente de python
#https://stackoverflow.com/questions/34803040/how-to-run-pip-of-different-version-of-python-using-python-command

def convertExcelToDict(file):
    datos = pd.ExcelFile(file)
    df = datos.parse(datos.sheet_names[0])
    return df.to_dict()

class excelpandas(pd.DataFrame, pd.ExcelFile):
    @property
    def _constructor(self):
        return excelpandas

    # @property
    # def _constructor_sliced(self):
    #     return excelpandas

    def __init__(self, diccionario):
        super(excelpandas, self).__init__(diccionario)

    def recorrercolumnas(self):
        pass


    def ubicarcolumns(self):
        print(type(self.loc[:,self.columns[3]]))


















