'''
Esta modulo agrupa los validadores de parametros utilizados en el modulo
andreani.

Todos los validadores son decoradores de metodos de objetos.
'''
from gettext import gettext as _


class gt(object):
    '''
    Validador "mayor que".
    '''

    def __init__(self, attr_name, value):
        '''
        copia los parametros del decorador.
        '''
        self.attr_name = attr_name
        self.value = value

    def __call__(self, f):
        '''
        Valida que el parametro es correcto y lanza ValueError en caso
        contrario.
        '''
        def wrapped_f(*args, **kwargs):
            # valido que cumpla el requisito mayor que
            if float(kwargs.get(self.attr_name)) <= self.value:
                raise ValueError(_("%s debe ser mayor a %d" %
                                   (self.attr_name, self.value)))
            # retorno el llamado de la funcion
            return f(*args, **kwargs)
        return wrapped_f
