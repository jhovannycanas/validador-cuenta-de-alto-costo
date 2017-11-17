import unittest
import pandas as pd
from archivo import gestionfile

class testfile(unittest.TestCase):

    def test_dataframe(self):
        #self.assertIsInstance(gestionfile.filevalidation('CAC Artritis.xlsx').data, pd.DataFrame)
        df = gestionfile.filevalidation('CAC Artritis.xlsx')
        #print(df.validarCaracteresEspeciales())
        # for k in df.errores.values():
        #     print k
        #print(df.validarCaracteresEspeciales())

        self.assertTrue(df.validarCamposNulos())
        df.validar_EPS()
        df.validar_Regimen()
        #print(df.validarSecuenciaColumnas())
        print(df.dfvalidacion)
        print(df.errores)


if __name__ == '__main__':
    unittest.main()