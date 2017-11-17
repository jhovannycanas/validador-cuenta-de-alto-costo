import sys
from cx_Freeze import setup, Executable

build_exe_options = {"includes": ["Tkinter", "pandas"]}

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

setup(name="Malla Validadora Artritis",
      version="0.1",
      description="Aplicativo para validar la cuenta de alto costo de artritis",
      options = {"build_exe": {"packages": ["Tkinter", "pandas","PIL"], "include_files":
          ["validacion/constansts.py", "validacion/metodos.py","validacion/valores.py",
            "archivo/gestionfile.py","view/images/excel.png","view/images/export.png","view/images/plain.png",
          "view/images/process.png"]}},
      executables=[Executable(script="view/presentacionmain.py", base=base,
                              targetName="validador.exe")]
      )