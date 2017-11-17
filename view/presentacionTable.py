#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
from pandastable import Table, TableModel

class mainAplicacion(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("hola mundo")
        self.parent.geometry('600x400+200+100')

        #se crea el grid para mostrar los datos

        f = tk.Frame(self.parent)
        f.pack(fill= tk.BOTH, expand=1)
        df = TableModel.getSampleData()
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=True, showstatusbar=True)

        pt.show()
        return

        def imprimir():
            print('hola mundo')
        self.boton = tk.Button(self.parent, text= "executar",command =imprimir)
        self.boton.grid(row=0, column=0)



if __name__ == '__main__':
    root = tk.Tk()
    mainAplicacion(root)
    root.mainloop()





