import random
import collections

inc = 5
app = ['acad', 'revit', 'skt', 'word', 'excel', 'ppt']


def check():
    time = 0
    lista = []
    print(time)

    def count(inc, app, user):
        nonlocal time, lista
        time = time+inc
        lista.append(app)
        print(f'{time}')
        print(lista)
        # zerar
        if time == 300:

            col = collections.Counter(lista)
            print(col)
            print(col.most_common(1))
            for i in col:
                print(f'{i} - {col[i]}')

            time = 0
            lista = []
    return count


vis = check()
i = 0
while i < 301:
    vis(inc, random.choice(app), 'vinicius')
    i = i+1
