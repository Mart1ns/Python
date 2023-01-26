# --> Ativador de Windows

import os as sistema
import time
import random as aleatorio


def limpar_terminal():
    time.sleep(3)
    sistema.system('cls')

def trocar_cor():
    #cod_cor = aleatorio.randint(0,10)
    for i in range(0,10):
        sistema.system(f'color {i} ')
        time.sleep(1)

def ativar(op=None):
    #sistema.system('slmgr/dlv')
    #sistema.system('slmgr/upk')
    limpar_terminal()
    print('--> Caso apresente algum erro, execute no modo administrador! <--')
    limpar_terminal()

    if op is not None:
        match op:
            case 1:
                sistema.system('cscript slmgr.vbs /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99')
                sistema.system('cscript slmgr.vbs /skms kms.lotro.cc')
                sistema.system('cscript slmgr.vbs /ato')
                limpar_terminal()
                print('--> Ativado com sucesso!')
                sistema.system('shutdown -r')
            case 2:
                sistema.system('cscript slmgr.vbs /ipk PVMJN-6DFY6-9CCP6-7BKTT-D3WVR')
                sistema.system('cscript slmgr.vbs /skms kms.lotro.cc')
                sistema.system('cscript slmgr.vbs /ato')
                limpar_terminal()
                print('--> Ativado com sucesso!')
                sistema.system('shutdown -r')

            case 3:
                sistema.system('cscript slmgr.vbs /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH')
                sistema.system('cscript slmgr.vbs /skms kms.lotro.cc')
                sistema.system('cscript slmgr.vbs /ato')
                limpar_terminal()
                print('--> Ativado com sucesso!')
                sistema.system('shutdown -r')   

            case 4:
                sistema.system('cscript slmgr.vbs /ipk 3KHY7-WNT83-DGQKR-F7HPR-844BM')
                sistema.system('cscript slmgr.vbs /skms kms.lotro.cc')
                sistema.system('cscript slmgr.vbs /ato')
                limpar_terminal()
                print('--> Ativado com sucesso!')
                sistema.system('shutdown -r')

            case 5:
                sistema.system('cscript slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
                sistema.system('cscript slmgr.vbs /skms kms.lotro.cc')
                sistema.system('cscript slmgr.vbs /ato')
                limpar_terminal()
                print('--> Ativado com sucesso!')
                sistema.system('shutdown -r')

            case 6:
                sistema.system('cscript slmgr.vbs /ipk MH37W-N47XK-V7XM9-C7227-GCQG9')
                sistema.system('cscript slmgr.vbs /skms kms.lotro.cc')
                sistema.system('cscript slmgr.vbs /ato')
                limpar_terminal()
                print('--> Ativado com sucesso!')
                sistema.system('shutdown -r')

            case 7:
                sistema.system('cscript slmgr.vbs /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43')
                sistema.system('cscript slmgr.vbs /skms kms.lotro.cc')
                sistema.system('cscript slmgr.vbs /ato')
                limpar_terminal()
                print('--> Ativado com sucesso!')
                sistema.system('shutdown -r')
            
            case 8:
                sistema.system('cscript slmgr.vbs /ipk  DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4')
                sistema.system('cscript slmgr.vbs /skms kms.lotro.cc')
                sistema.system('cscript slmgr.vbs /ato')
                limpar_terminal()
                print('--> Ativado com sucesso!')
                sistema.system('shutdown -r')

            case 9:
                sistema.system('cscript slmgr.vbs /ipk  NW6C2-QMPVW-D7KKK-3GKT6-VCFB2')
                sistema.system('cscript slmgr.vbs /skms kms.lotro.cc')
                sistema.system('cscript slmgr.vbs /ato')
                limpar_terminal()
                print('--> Ativado com sucesso!')
                sistema.system('shutdown -r')





limpar_terminal()
print('\n\n\n\n ██╗░░██╗███╗░░░███╗███████╗            ▄───▄')
print(' ██║░██╔╝████╗░████║╚════██║            █▀█▀█')                                    
print(' █████═╝░██╔████╔██║░░███╔═╝            █▄█▄█')
print(' ██╔═██╗░██║╚██╔╝██║██╔══╝░░            ─███──▄▄') 
print(' ██║░╚██╗██║░╚═╝░██║███████╗            ─████▐█─█')
print(' ╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝            ─████───█')
print('                                        ─▀▀▀▀▀▀▀ ')
trocar_cor()

limpar_terminal()


print('\n\n**********************')
print('** Escolha a versão **')
print('**********************')
print("\n\n |1 = Home/Core\n |2 = Home/Core (Country Specific)\n |3 = Home/Core (Single Language)\n |4 = Home/Core N\n |5 = Professional(Wind pro)\n |6 = Professional N(Wind pro N)\n |7 = Enterprise\n |8 = Enterprise N\n |9 = Education\n\n")
op = int(input('--> '))
ativar(op)