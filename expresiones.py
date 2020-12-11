from enum import Enum



class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''


class ExpresionIdentificador(ExpresionNumerica) :
    '''
        Esta clase representa un identificador.
    '''

    def __init__(self, id = "") :
        self.id = id