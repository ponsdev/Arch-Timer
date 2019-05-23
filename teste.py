import random
import collections

inc = 5
appList = ['acad', 'revit', 'chrome', 'word', 'skt', 'ppt', 'firefox']
appUteis = ['acad', 'revit', 'word', 'ppt', 'skt']


def check(user):
    time = 0
    lista = []
    # print(time)

    def count(inc, app):
        global appList
        nonlocal time, lista, user
        time = time+inc
        lista.append(app)
        # print(f'{time}')
        # print(lista)
        # zerar
        if time == 300:
            uteis = collections.Counter(x for x in lista if x in appUteis)
            inuteis = collections.Counter(x for x in lista if x not in appUteis)
            # print(uteis)
            # print(inuteis)
            somaUteis = sum(uteis.values())*inc
            maisUtilizado = uteis.most_common(1)[0][0]
            maisUtilizadoValor = uteis.most_common(1)[0][1]
            # print(maisUtilizadoValor*inc/60)

            print(somaUteis)
            if somaUteis >= 300*0.50:
                # print('extra')
                maisUtilizadoValor = round(((maisUtilizadoValor)*inc + (300-somaUteis))/60, 2)
                # print(maisUtilizadoValor)

            for i in list(uteis):
                if i == maisUtilizado:
                    print(f'{i} - {maisUtilizadoValor}')
                else:
                    print(f'{i} - {round(uteis[i]*inc/60, 2)}')

            print('----------------------')
            time = 0
            lista = []
    return count


vis = check('vinicius')
i = 0
while i < 600:
    vis(inc, random.choice(appList))
    i = i+inc
