from enum import Enum

'''
Clase para representar los estados que pueden tener las casillas
Cada estado esta representado por un identificador y un numero
Esta clase hereda de la clase Enum, que esta definida en el paquete enum importado antes
Esta herencia se usa para que la clase quede definida como un Enum y no una clase normal
'''
class TileStates(Enum):
    # Estado por defector de las casillas
    Empty = 1
    # Estados para las casillas de disparo
    MissedShot = 2
    HitShot = 3
    # Estados para las casillas donde hay un barco, uno para cada tipo de barco
    Carrier = 5
    Battleship = 6
    Cruiser = 7
    Submarine = 8
    Destroyer = 9
    # Estado para las casillas donde hay un barco el cual fue impactado
    HitCarrier = 10
    HitBattleship = 11
    HitCruiser = 12
    HitSubmarine = 13
    HitDestroyer = 14