# import random
import collections
from models.logfncs import saveLog


# INC = 5
# APPLIST = ['revit', 'autocad', 'sketchup', 'word',
#            'excel', 'ppt', 'firefox', 'chrome']
# APPUTEIS = ['revit', 'autocad', 'sketchup', 'word',
#             'excel', 'ppt']


def check(user):
    time = 0
    lista = []

    def count(cfgSets, appRunning):
        nonlocal time, lista, user
        APPUTEIS = ['revit', 'autocad', 'sketchup', 'word',
                    'excel', 'ppt']
        inc = int(cfgSets[1])
        time = time+inc
        lista.append(appRunning)
        print(time)
        if time == 180:
            uteis = collections.Counter(x for x in lista if x.app in APPUTEIS)
            soma_uteis = sum(uteis.values())*inc
            soma_inuteis = 180 - soma_uteis
            if soma_uteis is not 0:
                mais_utilizado = uteis.most_common(1)[0][0]
                mais_utilizado_valor = uteis.most_common(1)[0][1]*inc

            if soma_uteis >= 180*0.75:
                mais_utilizado_valor = round(
                    (mais_utilizado_valor) + soma_inuteis, 2)

            tempo_considerado = 0
            for i in list(uteis):
                if i == mais_utilizado:
                    # print(f'{i.fileName} - {mais_utilizado_valor}')
                    saveLog(i, user,
                            cfgSets, mais_utilizado_valor)
                    tempo_considerado += mais_utilizado_valor
                else:
                    # print(f'{i.fileName} - {round(uteis[i]*inc, 2)}')
                    saveLog(i, user, cfgSets,
                            round(uteis[i]*inc, 2))
                    tempo_considerado += round(uteis[i]*inc, 2)

            print(tempo_considerado)

            print('----------------------')
            time = 0
            lista = []
    return count


# CHECKER = check('vinicius')
# i = 0
# while i < 1200:
#     CHECKER(INC, random.choice(APPLIST))
#     i = i+INC
