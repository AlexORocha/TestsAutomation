import sys

def main(argv):
    if argv[1] == 'ruido_impulsivo':
        from tests.ruido_impulsivo import run as ruido_impulsivo
        ruido_impulsivo()

if __name__ == '__main__':
    main(sys.argv)