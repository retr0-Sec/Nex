import os
from time import sleep
from functions import fala,capture_audio,normalizar,escutar
import subprocess


def desligar():
    fala("Confirma desligamento do sistema? ")
    escolha = escutar()

    if not escolha:
        fala("Cancelando desligamento.")
        return

    if escolha in ["sim", "s", "claro", "pode", "ok","desligar"]:
        fala("Beleza, desligando em 3 segundos")
        sleep(3)
        subprocess.Popen("Shutdowm")

desligar()