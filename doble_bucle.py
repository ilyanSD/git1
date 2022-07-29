import sys

if __name__ == "__main__":
    tablero = [['P', 'P', 'P', 'P', '-', '-', 'Z', 'Z', '-', '-'],
               ['P', 'P', 'P', 'P', '-', '-', 'Z', 'Z', '-', '-'],
               ['P', 'P', 'P', 'P', '-', '-', 'Z', 'Z', '-', '-'],
               ['P', 'ME VA A IMPRIMIR LO QUE HAYA EN EL PUNTO (3,1)', 'P', 'P', '-', '-', 'Z', 'Z', '-', '-'],
               ['P', 'P', 'P', 'P', '-', '-', 'Z', 'Z', '-', '-'],
               ['P', 'P', 'P', 'P', '-', '-', 'Z', 'Z', '-', '-'],
               ['P', 'P', 'P', 'P', '-', '-', 'Z', 'Z', '-', '-'],
               ['P', 'P', 'P', 'P', '-', '-', 'Z', 'Z', '-', '-'],
               ['P', 'P', 'P', 'P', '-', '-', 'Z', 'Z', '-', '-'],
               ['P', 'P', 'P', 'P', '-', '-', 'Z', 'Z', '-', '-']];
    
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            tablero[i][j] = '0'
        print(tablero[i], sep = ' ')
            