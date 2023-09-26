
#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_STREAM
import time
from multiprocessing import Process
import exercicios as EX

IP_MONITOR = '127.0.0.1'
PORTA_IOT = 9999
ESTADO = 'OFF'

def interpretaComando(id: str, comando: str, s : socket):
    global ESTADO
    EX.fazLog(f'IOT {id}: recebeu o comando={comando}\n')
    if comando.lower() == 'ligar':
        ESTADO = 'ON'
    elif comando.lower() == 'desligar':
        ESTADO = 'OFF'
    elif comando.lower() == 'consulta':
        EX.exercicio6(s, id, ESTADO)   
    elif comando.lower() == 'shutdown':
        s.close()    
    else:
        EX.fazLog(f'IoT {id}: comando desconhecido = {comando}\n')
        time.sleep(10)

def main_sensor(ip: str, porta: int, id: str):

    '''
    Programa principal executado pelo dispositivo de IoT

    Parametros:
    ip: endereço do monitor
    porta: porta do monitor
    id: identificado do dispositivo de IoT
    '''

    s = socket(AF_INET, SOCK_STREAM)
    try:
        EX.exercicio5( s, (ip,porta))
    except:
        EX.fazLog(f'IoT {id}: O monitor nao está ativo!!!\n')
        exit()

    try:
        s.send(id.encode()) # Envia o identificador
    except:
        EX.fazLog(f'IoT {id}: O monitor nao está ativo!!!\n')
        exit()

    while True:
        try:
            dados = s.recv(100)
            if not dados:
                EX.fazLog(f'IOT {id}: O MONITOR ENCERROU, BYE!\n')
                break
            interpretaComando(id, dados.decode(), s)        
        except:
            print(f'IoT {id}: Conexão encerrada!')
            EX.fazLog(f'IOT {id}: SHUTDOWN, BYE!\n')
            break

#--------------------------------------------------------------
if __name__ == '__main__':
    Process(target=main_sensor, args=(IP_MONITOR, PORTA_IOT,'sala')).start()
    Process(target=main_sensor, args=(IP_MONITOR, PORTA_IOT,'quarto')).start()
    Process(target=main_sensor, args=(IP_MONITOR, PORTA_IOT,'cozinha')).start()
    print('Os dispositivos de IoT foram lançados')
