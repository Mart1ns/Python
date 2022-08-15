'''
--> automatizar tarefa
'''

# Importar bibliotecas
import numbers
import os
from platform import system
from PySimpleGUI import *
import PySimpleGUI as sg 


interface = [ # --> Criar a interface
    
    [sg.Text('Informe a temperatura em Celsius:', font='Arial',  text_color='Black', background_color='#3065ac')],
    [sg.Input('', key='number')],
    [sg.Button('Fahrenheit', font='Arial'), sg.Button('Kelvin', font='Arial')]
 
]

# Criar e modificar janela

janela = sg.Window('Conversor', interface, icon=r'ter.png')
janela.BackgroundColor='#3065ac'
janela.ElementJustification='center'

# --> Começo do programa

while True:
    
    tarefas, valores = janela.read()
    if tarefas == sg.WIN_CLOSED:
        break
    if tarefas == 'Fahrenheit':
        janela['number'].update((int(valores['number'])* 9/5) + 32)
    if tarefas == 'Kelvin':
        janela['number'].update(float(valores['number']) + 273.15)
        
        
    