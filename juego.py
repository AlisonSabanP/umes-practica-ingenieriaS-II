import random

def compararJugada(jugadaH, jugadaM):
    jugadaH = jugadaH.lower()
    jugadaM = jugadaM.lower()

    if jugadaH == jugadaM:
        return 0
    elif (jugadaH == 'piedra' and jugadaM == 'tijera') or \
        (jugadaH == 'tijera' and jugadaM == 'papel') or \
        (jugadaH == 'papel' and jugadaM == 'piedra'):
        return 1
    else:
        return -1


jugadaH = input('Ingrese sus 3 jugadas separadas por espacio (piedra, papel o tijera): ')
listajugadaH = jugadaH.lower().split()
opciones_validas = ['piedra', 'papel', 'tijera']

if len(listajugadaH) != 3:
    print('Error: Debe ingresar exactamente 3 jugadas.')
    exit()

for jugada in listajugadaH:
    if jugada not in opciones_validas:
        print(f'Error: {jugada} no es una jugada válida.')
        print('Las opciones válidas son: piedra, papel o tijera.')
        exit()



opciones = ['piedra', 'papel', 'tijera']
jugadaM = [random.choice(opciones) for n in range(3)]

print('El usuario elige:', ' '.join(listajugadaH))

print('El programa elige:', ' '.join(jugadaM))

resultadoH = 0
resultadoM = 0
for i in range(3):
    resultado = compararJugada(listajugadaH[i], jugadaM[i])
    if resultado == 1:
        resultadoH += 1
    elif resultado == -1:
        resultadoM += 1

print('Punteo:', resultadoH, '-', resultadoM)

if resultadoH > resultadoM:
    print('Ganador: Humano')
elif resultadoH < resultadoM:
    print('Ganador: Programa')
else:
    print('Empate')
    print('Ambos obtuvieron los mismos resultados')
