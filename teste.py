import random
import collections

inc = 5
appList = ['revit', 'acad', 'sketchup', 'word',
           'excel', 'ppt', 'firefox', 'chrome']
appUteis = ['revit', 'acad', 'sketchup', 'word',
            'excel', 'ppt']


def check(user):
    time = 0
    lista = []

    def count(inc, app):
        global appList
        nonlocal time, lista, user
        time = time+inc
        lista.append(app)
        if time == 300:
            uteis = collections.Counter(x for x in lista if x in appUteis)
            somaUteis = sum(uteis.values())*inc
            somaInuteis = 300 - somaUteis
            maisUtilizado = uteis.most_common(1)[0][0]
            maisUtilizadoValor = uteis.most_common(1)[0][1]*inc

            print(somaUteis)
            if somaUteis >= 300*0.75:
                maisUtilizadoValor = round(
                    (maisUtilizadoValor) + somaInuteis, 2)

            ola = 0
            for i in list(uteis):
                if i == maisUtilizado:
                    print(f'{i} - {maisUtilizadoValor}')
                    ola += maisUtilizadoValor
                else:
                    print(f'{i} - {round(uteis[i]*inc, 2)}')
                    ola += round(uteis[i]*inc, 2)

            print(ola)

            print('----------------------')
            time = 0
            lista = []
    return count


vis = check('vinicius')
i = 0
while i < 1200:
    app = random.choice(appList)
    vis(inc, app)
    i = i+inc
