import time
from script import scriptUp


def main():

    step = 2
    run = True
    while run:
        scriptUp()
        time.sleep(step)


if __name__ == '__main__':
    main()
