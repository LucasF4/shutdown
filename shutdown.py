import os
import datetime

verificador = False
print("Script Rodando")

hora = input("Qual horário você pretende desligar seu computador: ")

print("\n\nSucesso!\nSeu computador foi programado para desligar às " + hora + " horas.")

def verify():
    data = datetime.datetime.now()
    if data.hour == int(hora):
        return True
    else:
        return False

while verificador == False:
    
    verificador = verify()

print("O computador será desligado!")
os.system('shutdown -s')