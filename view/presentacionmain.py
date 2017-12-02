#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import datetime
import os
import sys
import tkFont
import tkMessageBox
from tkFileDialog import askopenfilename, asksaveasfilename

import PIL.Image
import PIL.ImageTk

from Tooltip.tooltip import ToolTips
from archivo import gestionfile
from validacion import constansts

sys.path.append('view/')

#https://stackoverflow.com/questions/40879085/open-excel-file-in-tkinter-and-plot-graphs
#https://stackoverflow.com/questions/40295587/how-can-i-use-tkinter-to-prompt-users-to-save-a-dataframe-to-an-excel-file

class presentacion(tk.Frame):

    def __init__(self, parent= None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        parent.minsize(width=750, height=450)
        parent.maxsize(width=900, height=500)
        self.archivo = None
        self.init()
        self.centrar()

    def imprimir(self):
        print ("exitoso")


    def init(self):

        self.parent.title("Validador de la cuenta de alto costo artritis")
        self.lblresultados = tk.Label(self.parent, text ="Resultados")
        self.lblresultados.grid(row=0, columnspan=4)
        self.widgets = []
        self.tooltip_text = []

        font_obj = tkFont.Font(family="Courier", size=12)

        self.area = tk.Text(self.parent, wrap=tk.CHAR)
        self.area.grid(row= 1, column = 0, columnspan = 2, rowspan = 4,padx=5,
                       sticky=tk.E + tk.W + tk.S + tk.N)
        self.widgets.append(self.area)
        self.tooltip_text.append("Consola de resultados de la carga de archivos")

        self.columnconfigure(3, pad=7)
        im = PIL.Image.open("images/excel.png")
        im = im.resize((64, 64), PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(im)
        self.btncargarexcel = tk.Button(self.parent,  text = "subir excel",image = photo,
                                        command= self.loadArchivo)
        self.widgets.append(self.btncargarexcel)
        self.tooltip_text.append("Cargar un archivo excel para validación")

        self.btncargarexcel.image = photo
        self.btncargarexcel.grid(row= 1, column = 3,padx=(0,0), pady=(0,0),sticky=tk.E + tk.W + tk.S + tk.N )

        implain = PIL.Image.open("images/plain.png")
        implain = implain.resize((64, 64), PIL.Image.ANTIALIAS)
        photoplain = PIL.ImageTk.PhotoImage(implain)
        self.btncargartxt = tk.Button(self.parent,image = photoplain, text = "subir txt",
                                      command= self.loadArchivotxt)
        self.btncargartxt.image = photoplain
        self.btncargartxt.grid(row= 2, column = 3,padx=(0,0), pady=(0,0),sticky=tk.E + tk.W + tk.S + tk.N)

        self.widgets.append(self.btncargartxt)
        self.tooltip_text.append("Cargar un archivo plano para validación")

        improcess = PIL.Image.open("images/process.png")
        improcess =improcess.resize((64,64),PIL.Image.ANTIALIAS)
        photoprocess = PIL.ImageTk.PhotoImage(improcess)
        self.btnvalidar = tk.Button(self.parent, text = "validar",image = photoprocess, state=tk.DISABLED,
                                    command=self.validarArchivo)
        self.btnvalidar.image = photoprocess
        self.btnvalidar.grid(row= 3, column = 3,padx=(0,0), pady=(0,0),sticky=tk.E + tk.W + tk.S + tk.N)

        self.widgets.append(self.btnvalidar)
        self.tooltip_text.append("Realizar validación de cada campo del archivo")

        imexport = PIL.Image.open("images/export.png")
        imexport = imexport.resize((64, 64), PIL.Image.ANTIALIAS)
        photoexport = PIL.ImageTk.PhotoImage(imexport)

        self.btnreporte = tk.Button(self.parent, image = photoexport,text = "generar reporte",
                                    command = self.generararchivo, state=tk.DISABLED)
        self.btnreporte.image = photoexport
        self.btnreporte.grid(row= 4, column = 3,padx=(0,0), pady=(0,0),sticky=tk.E + tk.W + tk.S + tk.N)

        self.widgets.append(self.btnreporte)
        self.tooltip_text.append("Generar el reporte de la cuenta de alto costo")

        imhelp = PIL.Image.open("images/help.png")
        imhelp = imhelp.resize((64, 64), PIL.Image.ANTIALIAS)
        photohelp = PIL.ImageTk.PhotoImage(imhelp)

        self.btnayuda = tk.Button(self.parent,text="ayuda",image = photohelp, command = self.help)
        self.btnayuda.image = photohelp
        self.btnayuda.grid(row = 5, column = 0)

        self.widgets.append(self.btnayuda)
        self.tooltip_text.append("Sobre la aplicación")

        self.bterrores = tk.Button(self.parent,text="Exportar errores a Excel",
                                   command = self.generararchivoerrores,state=tk.DISABLED)
        self.bterrores.grid(row = 5,  column = 1,padx=5, pady=5)

        imsalir = PIL.Image.open("images/salir.png")
        imsalir = imsalir.resize((64, 64), PIL.Image.ANTIALIAS)
        photosalir = PIL.ImageTk.PhotoImage(imsalir)

        self.btnsalir =  tk.Button(self.parent, text = "salir",image = photosalir, command= self.quit)
        self.btnsalir.grid(row= 5, column = 3,padx=(0,0), pady=(0,0),sticky=tk.E + tk.W + tk.S + tk.N)
        self.btnsalir.image = photosalir

        self.widgets.append(self.btnsalir)
        self.tooltip_text.append("Salir de la aplicación")

        tooltip_obj = ToolTips(self.widgets, self.tooltip_text)


    def centrar(self):
        self.w = 650
        self.h = 600
        self.sw = self.parent.winfo_screenwidth()
        self.sh = self.parent.winfo_screenheight()
        x = (self.sw - self.w) / 2
        y = (self.sh - self.h) / 2
        self.parent.geometry('%dx%d+%d+%d' %(self.w, self.h, x, y))

    def help(self):
        top = tk.Toplevel()
        top.title("Sobre la malla validadora")
        top.geometry("300x150+120+120")

        msg = tk.Message(top, text="MALLA VALIDADORA PARA FACILITAR EL REPORTE DE INFORMACION DE ARTRITIS "
                                   "DE ACUERDO CON LO DISPUESTO EN LA RESOLUCION 1393 DE 2016")
        msg.pack()

        button = tk.Button(top, text="Cerrar", command=top.destroy)
        button.pack()


    def loadArchivo(self):
        self.limpiarCampos()
        self.desabilitarBotones()
        self.nombre = askopenfilename(filetypes=[('Excel', ('*.xls', '*.xlsx'))])
        if self.nombre:
            self.validararupload(self.nombre)

    def loadArchivotxt(self):
        self.limpiarCampos()
        self.desabilitarBotones()
        self.nombre = askopenfilename(filetypes=[('text files', '*.txt')])
        if self.nombre:
            self.validararupload(self.nombre)

    def validararupload(self, nombre):
        self.archivo = nombre
        nombrearchivo, extension = os.path.splitext(nombre)
        self.secuencia = True
        self.cargaarchivo = False
        if extension in (".xls", ".xlsx"):
            self.datos = gestionfile.filevalidation(self.archivo, constansts.ARCHIVO_EXCEL)
        if extension == ".txt":
            self.datos = gestionfile.filevalidation(self.archivo, constansts.ARCHIVO_CSV)
        if not self.datos.validarLongitudColumnas():
            self.cargaarchivo = True
            self.mostrarAlertaCargaArchivo("El numero de columnas del archivo no corresponde a las esperadas")
            self.area.insert(tk.END,
                             "El numero de columnas del archivo no es igual a lo estipulado en la resolucion, por favor"
                             "verificar las columnas del archivo")

        self.datos.validarfechas()
        if extension != ".txt":
            if not self.datos.validarSecuenciaColumnas():
                self.secuencia = False
                self.mostrarAlertaCargaArchivo("El archivo que intenta validar presenta varias inconsistencias"
                                               ", por favor verificar segun el reporte en la consola.")
        if self.secuencia:
            if not (self.datos.validarCamposNulos()):
                self.mostrarAlertaCargaArchivo("El archivo que intenta validar presenta varias inconsistencias"
                                               ", por favor verificar segun el reporte en la consola.")

        if self.secuencia:
            if (self.datos.validarFiltroTexto()):
                self.mostrarAlertaCargaArchivo("El archivo que intenta validar presenta varias inconsistencias"
                                               ", por favor verificar segun el reporte en la consola.")
        if self.secuencia:
            if self.datos.validarunicovalor():
                self.cargaarchivo = True
                self.mostrarAlertaCargaArchivo("El codigo de la EAPB debe ser unico para el reporte")
                self.area.insert(tk.END,
                                 "La columna APEB presenta dos o mas codigos para el presente informe,por favor "
                                 "verificar")
        if len(self.datos.errores) > 0 or self.cargaarchivo:
            self.bterrores['state'] = 'normal'
            self.mostrarAlertaCargaArchivo("El archivo que intenta validar presenta varias inconsistencias"
                                           ", por favor verificar segun el reporte en la consola.")

            for error in self.datos.errores:
                for detalle in error:
                    self.area.insert(tk.END, "\n")
                    self.area.insert(tk.END, detalle)


        else:
            self.datos.ajustarfechastimestamp()
            self.datos.convertirafechas()
            self.btnvalidar['state'] = 'normal'
            self.mostrarAviso("El archivo se cargo exitosamente")
            print(self.datos.data.shape)
            self.area.insert(tk.END, "Se cargaron de forma exitosa %s registros o filas y %s columnas." % (self.datos.data.shape))

    def validaridentificacion(self):
        if self.datos is not None:
            self.datos.validar_Regimen()
            self.datos.validar_EPS()
            self.datos.validar_grupopobalcional()
            self.datos.validar_PrimerNombre()
            self.datos.validar_SegundoNombre()
            self.datos.validar_PrimerApellido()
            self.datos.validar_SegundoApellido()
            self.datos.validar_tipoidentificacion()
            self.datos.validar_Identificacion()
            self.datos.validar_FechaNacimiento()
            self.datos.validar_sexo()
            self.datos.validar_etnia()
            self.datos.validar_DireccionResidencia()
            self.datos.validar_Telefono()
            self.datos.validar_CodigoMunicipio()
            self.datos.validar_FechaAfiliacionEAPB()

    def validardiagnosticotratamiento(self):
        if self.datos is not None:
            self.datos.validar_FechaInicioSintomas()
            self.datos.validar_FechaPrimeraVisitaAr()
            self.datos.validar_FechaDiagnosticaAr()
            self.datos.validar_Talla()
            self.datos.validar_PesoInicial()
            self.datos.validar_Radiografiamanos()
            self.datos.validar_Radiografia_Pies()
            self.datos.validar_VSGInicial()
            self.datos.validar_PCRInicial()
            self.datos.validar_Factor_Reumatoideo_Inicial()
            self.datos.validar_HemglobinaInicial()
            self.datos.validar_Leucocitos()
            self.datos.validar_Creatina()
            self.datos.validar_TFGInicial()
            self.datos.validar_Parcial_Orina_Inicial()
            self.datos.validar_ALT_Inicial()
            self.datos.validar_Anti_CCP()
            self.datos.validar_HTA()
            self.datos.validar_DM()
            self.datos.validar_ECV()
            self.datos.validar_ERC()
            self.datos.validar_Osteoporosis()
            self.datos.validar_Sindrome_Sjogren()
            self.datos.validar_FechaPrimerDAS()
            self.datos.validar_Profesional_DAS()
            self.datos.validar_ResultadoPrimerDas()
            self.datos.validar_FechaHAQ()
            self.datos.validar_HAQ()
            self.datos.validar_FechaDMARD()
            self.datos.validar_Analgesicos_No_Opioides()
            self.datos.validar_Analgesicos_Opioides()
            self.datos.validar_AINES()
            self.datos.validar_Corticoides()
            self.datos.validar_FechaTratamientoDMARD()
            self.datos.validar_Tamizaje_TB()
            self.datos.validar_Antecedente_linfoma()
            self.datos.validar_Azatioprina()
            self.datos.validar_Ciclosporin()
            self.datos.validar_Ciclofosfamida()
            self.datos.validar_Cloroquina()
            self.datos.validar_D_penicilaimina()
            self.datos.validar_Etanercept()
            self.datos.validar_Leflunomida()
            self.datos.validar_Metotrexate()
            self.datos.validar_Rituximab()
            self.datos.validar_Sulfasalazina()
            self.datos.validar_Abatacept()
            self.datos.validar_Adalimuma()
            self.datos.validar_Certolizumab()
            self.datos.validar_Golimumab()
            self.datos.validar_Hidroxicloroquina()
            self.datos.validar_Infliximab()
            self.datos.validar_Sales_oro()
            self.datos.validar_Tocilizumab()
            self.datos.validar_Tofacitinib()
            self.datos.validar_Anakinrab()
            self.datos.validar_MedicamentoNoPos1()
            self.datos.validar_MedicamentoNoPos2()
            self.datos.validar_MedicamentoNoPos3()
            self.datos.validar_MedicamentoNoPos4()

    def validartratamientoactual(self):
        if self.datos is not None:
            self.datos.validar_pesoUltimo()
            self.datos.validar_Radiografia_manos_Ultima()
            self.datos.validar_Radiografia_pies_Ultima()
            self.datos.validar_PCRUltimo()
            self.datos.validar_VSGUltimo()
            self.datos.validar_HemoglobinaUltimo()
            self.datos.validar_LecocitosUltimo()
            self.datos.validar_CreatininaUltimo()
            self.datos.validar_TFGULtimo()
            self.datos.validar_Parcial_Orina_ultimo()
            self.datos.validar_ALT_ultimo()
            self.datos.validar_HTA_Actual()
            self.datos.validar_DM_Actual()
            self.datos.validar_ECV_Actual()
            self.datos.validar_ERC_Actual()
            self.datos.validar_Osteoporosis_Actual()
            self.datos.validar_Sindrome_Sjogren_Actual()
            self.datos.validar_FechaUltimaDAS()
            self.datos.validar_Profesional_DAS_Ultimo()
            self.datos.validar_TFGULtimo()
            self.datos.validar_Estado_AR()
            self.datos.validar_FechaUltimaHAQ()
            self.datos.validar_HAQUltimo()
            self.datos.validar_Analgesicos_No_Opioides_Dos()
            self.datos.validar_Analgesicos_Opioides_Dos()
            self.datos.validar_AINES_Do()
            self.datos.validar_Corticoides_Dos()
            self.datos.validar_glucocorticoides_dosis()
            self.datos.validar_Calcio()
            self.datos.validar_Vitamina_D()
            self.datos.validar_FechaINicioDMARD()
            self.datos.validar_Azatioprina_Dos()
            self.datos.validar_Ciclosporina_Dos()
            self.datos.validar_Ciclofosfamida_Dos()
            self.datos.validar_Cloroquina_DOS()
            self.datos.validar_D_penicilaimina_Dos()
            self.datos.validar_Etanercept_Dos()
            self.datos.validar_Leflunomida_Dos()
            self.datos.validar_Metotrexate_Dos()
            self.datos.validar_Rituximab_Dos()
            self.datos.validar_Sulfasalazina_Dos()
            self.datos.validar_Abatacept_Dos()
            self.datos.validar_Adalimumab_Dos()
            self.datos.validar_Certolizumab_Dos()
            self.datos.validar_Golimumab_Dos()
            self.datos.validar_Hidroxicloroquina_Dos()
            self.datos.validar_Infliximab_Dos()
            self.datos.validar_Sales_oro_dos()
            self.datos.validar_Tocilizumab_Dos()
            self.datos.validar_Tofacitinib_Dos()
            self.datos.validar_Anakinra_Dos()
            self.datos.validar_OtroMedicamentoNoPos1()
            self.datos.validar_OtroMedicamentoNoPos2()
            self.datos.validar_OtroMedicamentoNoPos3()
            self.datos.validar_OtroMedicamentoNoPos4()
            self.datos.validar_numeroReumatologo()
            self.datos.validar_numeroInternistaAr()
            self.datos.validar_numeroConsultasMedicoAR()
            self.datos.validar_Reemplazo_articular_1_por_AR()
            self.datos.validar_Reemplazo_articular_2_por_AR()
            self.datos.validar_Reemplazo_articular_3_por_AR()
            self.datos.validar_Reemplazo_articular_4_por_AR()
            self.datos.validar_numeroHospitalizacionesAR()
            self.datos.validar_CodigoHailitacion()
            self.datos.validar_CodigoMunicipio()
            self.datos.validar_fechaIngresoIPS()
            self.datos.validar_Atencion_Clinica_AR()
            self.datos.validar_Novedad_Paciente_Reporte_Anterior()
            self.datos.validar_FechaDesafiliacion()
            self.datos.validar_TrasladoPaciente()
            self.datos.validar_FechaMuerte()
            self.datos.validar_CausaMuerte()
            self.datos.validar_CostoDMARDPOS()
            self.datos.validar_CostoDMARDNoPOS()
            self.datos.validar_costoAnulaAR()
            self.datos.validad_costoAnualIncapacidad()


    def validarArchivo(self):
        self.limpiarCampos()
        del self.datos.errores[:]
        if self.datos is not None:
            self.validaridentificacion()
            self.validardiagnosticotratamiento()
            self.validartratamientoactual()

        if len(self.datos.errores) > 0:
            self.bterrores['state'] = 'normal'
            self.mostrarAlertaCargaArchivo("El archivo que intenta validar presenta varias inconsistencias"
                                           ", por favor verificar segun el reporte en la consola.")
            for error in self.datos.errores:
                for detalle in error:
                    self.area.insert(tk.END, "\n")
                    self.area.insert(tk.END, detalle)

        else:
            self.btnreporte['state'] = 'normal'
            self.mostrarAviso("El archivo cumple con todos los requisitos para generar el archivo")

    def generararchivo(self):
        if self.datos is not None:
            fechareporte = datetime.datetime.today().date()
            hora = datetime.datetime.now().time().strftime('%H-%M')
            nombrearchivo = "%s_%s_ARTRITIS_%s.txt" %(fechareporte.strftime('%Y-%m-%d'), self.datos.obtenerEAPB(),hora)
            rutasalida = os.path.dirname(self.nombre)
            rutaexporta= os.path.join(rutasalida,nombrearchivo)
            self.datos.removerespacios_convertmayuscula()
            self.datos.data.to_csv(rutaexporta, header=None, index=None, sep='\t', line_terminator='\r', mode='a')
            self.mostrarAviso("Se ha generado de forma exitosa el archivo de reporte")
            self.area.insert(tk.END, "El archivo resultado se encuentra ubicado en: " + rutaexporta)
            self.area.insert(tk.END, "\n")


    def generararchivoerrores(self):
        savefile = asksaveasfilename(filetypes=(("Excel files", "*.xlsx"),
                                                ("All files", "*.*")))
        if savefile:
            self.limpiarCampos()
            nombrearchivo, extension = os.path.splitext(savefile)
            if not extension in (".xls", ".xlsx"):
                savefile = savefile + ".xlsx"
            self.datos.crearexcelerrores(savefile)
            self.mostrarAviso("Se ha generado de forma exitosa el archivo de reporte de errores")
            self.area.insert(tk.END, "Favor revisar el archivo de arrores generado en Excel")


    def mostrarAviso(self, mensaje):
        tkMessageBox.showinfo("Información", mensaje)

    def mostrarAlertaCargaArchivo(self, mensaje):
        tkMessageBox.showerror("Error al cargar el archivo", mensaje)

    def desabilitarBotones(self):
        self.btnvalidar['state']= tk.DISABLED
        self.btnreporte['state']=tk.DISABLED
        self.bterrores['state'] = tk.DISABLED


    def limpiarCampos(self):
        self.area.delete(1.0, tk.END)

    def quit(self):
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    #root.resizable(width=False, height=False)
    presentacion(root)
    root.mainloop()

