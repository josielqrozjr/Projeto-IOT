#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import exercicios as EX  
import os

# ---------------------------------------------------------------------------------------------
# UMA THREAD PARA CADA SENSOR CONECTADO
def TrataSensor(conn: socket, SENSORES: dict, CONSOLE: list): 
   
    '''
    Recebe mensagens vindas dos dispositivos de IoT
    - atualiza o dicionario SENSORES
    - repassa as mensagens recebidas para a Thread Console

    Parametros:
    conn: conexão TCP com o dispositivo de IoT
    SENSORES: dicionario com os sensores conectados
    CONSOLE: lista que contém a conexão de console com o usuário
    '''
    sensor = conn.recv(10).decode()
    SENSORES[sensor] = conn

    EX.fazLog(f'MONITOR: o sensor {sensor} registrou: {conn.getpeername()}\n')

    while True:
        try:
            data = conn.recv(100)
            if not data:
                break

            EX.fazLog(f'MONITOR: sensor {sensor} enviou {data.decode()}')
            EX.exercicio2(CONSOLE[0], data)                 

        except Exception as e:
            print(e)
            break       

    conn.close()
    EX.fazLog(f'MONITOR: sensor {sensor} encerrou\n')
    SENSORES.pop(sensor)


#---------------------------------------------------------------------------------------------
# MAIN THREAD


if __name__ == "__main__":    

    if os.path.exists("log.txt"): os.remove("log.txt")

    PORTA_IOT = 9999
    SENSORES = {} # dicionário é mutável
    CONSOLE =[None] # lista é mutável

    EX.exercicio1(CONSOLE, SENSORES)

    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.bind(('', PORTA_IOT))
    except:
        EX.fazLog(f'MONITOR: erro de bind na porta {PORTA_IOT}\n')
        exit()

    s.listen(5)
    
    EX.fazLog(f'MONITOR: aguardando dispositivos de IOT em {PORTA_IOT}\n')

    while True:
        conn, addr = s.accept()
        t = Thread( target= TrataSensor, args=(conn, SENSORES, CONSOLE))
        t.start()




