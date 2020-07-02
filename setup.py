# este código não constitui parte efetiva do projeto, é um CÓDIGO ABERTO fornecido pela ferramenta cx_freeze
# que possibilita a criação de um arquivo executável, evitando a necessidade da instalação do Python 3.8 e
# do módulo pygame na máquina do usuário.
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"],}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "As_Aventuras_de_Gary",
        version = "0.1",
        description = "as_aventuras_de_Gary",
        options = {"build_exe": build_exe_options},
        executables = [Executable("As_Aventuras_de_Gary.py", base=base)])