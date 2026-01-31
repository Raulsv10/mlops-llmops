import sys
from funciones import clasificar_texto

def main():
    texto = sys.argv[1]
    modelo = sys.argv[2]

    resultado = clasificar_texto(texto, modelo)
    print(resultado)

if __name__ == "__main__":
    main()