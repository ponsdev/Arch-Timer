import random
import collections

INC = 5
APPLIST = ['revit', 'acad', 'sketchup', 'word',
           'excel', 'ppt', 'firefox', 'chrome']
APPUTEIS = ['revit', 'acad', 'sketchup', 'word',
            'excel', 'ppt']


def check(user):
    time = 0
    lista = []

    def count(inc, app):
        nonlocal time, lista, user
        time = time+inc
        lista.append(app)
        if time == 300:
            uteis = collections.Counter(x for x in lista if x in APPUTEIS)
            soma_uteis = sum(uteis.values())*inc
            soma_inuteis = 300 - soma_uteis
            mais_utilizado = uteis.most_common(1)[0][0]
            mais_utilizado_valor = uteis.most_common(1)[0][1]*inc

            print(soma_uteis)
            if soma_uteis >= 300*0.75:
                mais_utilizado_valor = round(
                    (mais_utilizado_valor) + soma_inuteis, 2)

            tempo_considerado = 0
            for i in list(uteis):
                if i == mais_utilizado:
                    print(f'{i} - {mais_utilizado_valor}')
                    tempo_considerado += mais_utilizado_valor
                else:
                    print(f'{i} - {round(uteis[i]*inc, 2)}')
                    tempo_considerado += round(uteis[i]*inc, 2)

            print(tempo_considerado)

            print('----------------------')
            time = 0
            lista = []
    return count


CHECKER = check('vinicius')
i = 0
while i < 1200:
    CHECKER(INC, random.choice(APPLIST))
    i = i+INC
