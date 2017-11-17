from archivo import gestionarchivo
import pandas as pd
import unittest

class testArchivoGestion(unittest.TestCase):

    def test_cargaarchivo(self):
        df = gestionarchivo.convertExcelToDict('CAC Artritis.xlsx')
        self.assertIsInstance(gestionarchivo.excelpandas(df), gestionarchivo.excelpandas)
        datafra = gestionarchivo.excelpandas(df)
        datafra.ubicarcolumns()


if __name__ == '__main__':
    unittest.main()
