import sys
import os

# Adiciona o caminho do diretório pai (ativ1) ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Module.functions as f
from prettytable import PrettyTable

try:
    print("\tCalculo do Metodo da Falsa Posição\t\n")
    func = str(input("Função f(x) = "))
    f.is_valid(func)
    print("\nConsiderando o intervalo [a, b]")
    a = float(input("Digite o valor de a = "))
    b = float(input("Digite o valor de b = "))
    e = float(input("Digite o nível de erro = "))
    n = int(input("Número máximo de interações = "))

    table = PrettyTable()
    table.field_names = ["i", "a", "b", "f(a)", "f(b)", "x", "f(x)"]

    i = 0
    fa = f.resolve(func, a)
    fb = f.resolve(func, b)
    
    while i < n:

        x = (a*abs(fb) + b*abs(fa))/(abs(fb) + abs(fa))
        fx = f.resolve(func, x)

        table.add_row([i, a, b, fa, fb, x, fx])

        if abs(fx) < e:
            print(table)
            print(f'\n\nResultado apos {i+1} interações: {x}')
            exit()
        i = i + 1
        if fb*fx < 0:
            a = x
            fa = fx
        else:
            b = x
            fb = fx

    print(f"O método falhou após {n} interações")
except (ValueError):
    print("Erro! Verifique se digitou as entradas corretamente")
finally:
     print("Fim do programa")