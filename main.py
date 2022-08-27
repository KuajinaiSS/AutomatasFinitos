import time
# Estado inicial 0
# Estados de aceptacion 1, 2, 3, 4, 5
# Funcion de transicion:
#  Estado | <letra> | <digito> | <operacion> | <especial> | <define> | "." | " "
#  ------------------------------------------------------------------
#    0    |    1    |     2    |      3      |      4     |          |  6  |  0  inicial
#    1    |    1    |     6    |      3      |      4     |          |  6  |  0  letra
#    2    |    6    |     2    |      3      |      4     |          |  5  |  0  digito
#    3    |    1    |     2    |      6      |      4     |          |  6  |  0  operacion
#    4    |    1    |     2    |      3      |      4     |          |  6  |  0  especial
#    5    |         |          |             |            |          |     |    define
#    6    |    6    |     5    |      6      |      6     |          |  6  |  0  decimal
#    7    |    6    |     6    |      6      |      6     |          |  6  |  6  trampa
# Estado 6: estado trampa (token desconocido)

dfa = {0: {'letra': 1, 'digito': 2, 'operacion': 3, 'especial': 4, 'decimal': 6, ' ': 0},  # inicial
       1: {'letra': 1, 'digito': 6, 'operacion': 3, 'especial': 4, 'decimal': 6, ' ': 0},  # letra
       2: {'letra': 6, 'digito': 2, 'operacion': 3, 'especial': 4, 'decimal': 5, ' ': 0},  # digito
       3: {'letra': 1, 'digito': 2, 'operacion': 6, 'especial': 4, 'decimal': 6, ' ': 0},  # operacion
       4: {'letra': 1, 'digito': 2, 'operacion': 3, 'especial': 4, 'decimal': 6, ' ': 0},  # especial
       5: {'letra': 6, 'digito': 5, 'operacion': 6, 'especial': 4, 'decimal': 6, ' ': 0},  # decimal
       6: {'letra': 6, 'digito': 6, 'operacion': 6, 'especial': 6, 'decimal': 6, ' ': 6}, }  # trampa

names = ['', '<id>', '<digito>', '<opmat>', '<special>', '<num_decimal>', '<unknown>']


def accepts(transitions, initial, accepting, s):
    state = initial
    aux2 = ''
    for c in s:
        if c == ' ':  # es un espacio
            aux = c
            c = ' '

        elif c == '(' or c == ')':  # es un ) o (
            aux = c
            c = 'especial'

        elif c == '*' or c == '/' or c == '+' or c == '-':  # es un operador de estos (*, /, +, -)
            aux = c
            c = 'operacion'

        elif c.isalpha():  # es del alfabeto (A-Z) y (a-z)
            aux = c
            aux2 = aux2 + c
            c = 'letra'

        elif c.isdigit():  # es digito (0-9)
            aux = c
            c = 'digito'

        elif c == '.':  # es un decimal
            aux = c
            c = 'decimal'

        else:  # es un unknown :c
            return False
        state = transitions[state][c]
        print(aux, names[state])
    return state in accepting


accepts(dfa, 0, {1, 2, 3, 4, 5}, '(2+2) hola')
print("\n"*10)
#accepts(dfa, 0, {1, 2, 3, 4, 5}, '(define radius 10) ')
print("\n"*10)
#accepts(dfa, 0, {1, 2, 3, 4, 5}, '(define circumference (* 2 pi radius))  ')
# piedad, solo no supe como imprimirlo como decia el profe, pero el resto si funciona de verdad nesesito la nota :c
