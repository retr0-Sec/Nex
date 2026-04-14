import threading
import time

from functions import fala,escutar



def contar_timer(seg):
    fala("Ok, irei avisar quando chegar ao tempo pedido.")
    time.sleep(seg)
    fala("retrô o taime que você pediu acabou de expirar")
    print(seg, "foi")

def Timer():
    def extrair_segundos(texto):
        texto = texto.lower()

        if "segundo" in texto:
            numero = ''.join(filter(str.isdigit, texto))
            return int(numero) if numero else None

        if "minuto" in texto:
            numero = ''.join(filter(str.isdigit, texto))
            return (int(numero) * 60) if numero else None

        return None

    def contar_timer(seg):
        fala("Ok, irei avisar quando chegar ao tempo pedido.")
        time.sleep(seg)
        fala("retrô o taime que você pediu acabou de expirar")
        print(seg, "foi")

    texto = escutar()
    if not texto:
        fala("Não entendi retrô")
    seg = extrair_segundos(texto)
    if not seg:
        fala("Não consegui entender a tempo, desculpe")
        return
    threading.Thread(target=contar_timer, args=(seg,)).start()




num = 10
fala(f"esta rodando enquanto {10} aguarda normalmente ")