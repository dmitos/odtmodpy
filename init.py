from os import sys, system


tipo = {}


def pantalla(tipo):
    pass


def LimPant():
    if sys.platform == 'linux':
        system('clear')
    elif sys.platform == 'win32':
        system('cls')


def eleccion():
    LimPant()
    print('1 * PREVENTIVO')
    print('2 * OTRO')
    prev = input('Seleccione tipo de preventivo / baja')
    if prev == '1':
        preventivo()
    elif prev == '2':
        otros()
    elif prev == '':
        salir()


def preventivo():
    pass


def salir():
    pass


def otros():
    pass


eleccion()
