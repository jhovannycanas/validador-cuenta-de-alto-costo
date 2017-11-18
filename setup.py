#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

build_exe_options = {"includes": ["Tkinter", "pandas","openpyxl"]}
#con esto se arregla lo del acceso directo https://stackoverflow.com/questions/24195311/how-to-set-shortcut-working-directory-in-cx-freeze-msi-bundle
base = None
if sys.platform == "win32":
    base = "Win32GUI"
#
# executables = [
#     Executable("/home/jhovanny/Documentos/malla_validadora/app_malla_validadora/view/presentacionmain.py",
#                appendScriptToExe=True,
#                )
# ]

#buildOptions = dict(create_shared_zip=False)


includefiles = ["images"]
setup(name="Malla Validadora Artritis",
author="Jhovanny Cañas -> jhovannycanas@gmail.com",
      version="0.1",
      description="Aplicativo para validar la cuenta de alto costo de artritis",
      options = {"build_exe": {"packages": ["Tkinter", "pandas","PIL", "numpy", "openpyxl","tooltip"] , 'include_files':includefiles}},
      executables=[Executable(script="view/presentacionmain.py", base=base,
                              targetName="validador.exe",shortcutName="Malla Validadora",
            shortcutDir="DesktopFolder",)]
      )