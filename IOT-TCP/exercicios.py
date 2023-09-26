#!/usr/bin/env python3
from console import Console
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from datetime import datetime
import time

def fazLog(msg: str):
    '''
    Registra em um log a mensagem recebida
    - Não altere essa função
    - O arquivo log.txt deve sem entregue como resultado da tarefa
    - O log é único para cada equipe pois inclui portas aleatórias e horário de cada evento     
    '''
    print(msg, end='')
    f = open('log.txt', 'a')
    f.write(f'{datetime.now()} : {msg}')
    f.close()

def exercicio1(CONSOLE: list, SENSORES: dict):
    '''
    Lança o Console como uma Thread

    Parametros:
    CONSOLE: lista contendo usada para salvar o socket que representa a conexão TCP com o usuário
    SENSORES: dicionario que associa o id do sensor e sua conexão TCP
    '''

    # DICA: Para chamar uma thread: Thread(target=, args=) 
    # Use a chamada de TrataSensor em monitor.py como exemplo
    # Veja a definição da função Console e passe os argumentos na ordem correta
    # Não esqueça do start()

    t = Thread(target=Console, args=(CONSOLE, SENSORES))
    t.start() 

    # fazLog('esqueci de fazer o exercicio 1\n') # comente quando fizer o exercicio

def exercicio2(console: socket, dados: bytes):
    '''
    Se o usuário estiver conectado envie o dados RECEBIDOS pelos sensores para o Console
    - console precisa ser diferente de None
    
    Parametros:
    console: socket do tipo cliente que representa a conexão TCP com o usuário
    dados: dados recebidos pelo dispositivos de IoT
    '''
    # DICA: teste se o objeto de conexão is not None
    # Para enviar os dados execute: conexão.send( dados em bytes)
    # Observe o tipo dos argumentos da função para saber se precisa fazer conversão
    
    if console is not None:
        console.send(dados)

    # fazLog('esqueci de fazer o exercicio 2\n') # comente quando fizer o exercicio

def exercicio3(console: socket, SENSORES: dict):
    '''
    Envia para o usuario a lista de sensores conectados
    - console precisa ser diferente de None
    
    Parametros:
    console: socket do tipo cliente que representa a conexão TCP com o usuário
    '''

    # DICA: os IDs dos sensores conectados estão em SENSORES.keys()
    # Monte a mensagem da seguinte forma: msg = 'Sensores conectados: ' + ','.join(SENSORES.keys())
    # Para enviar a mensagem use console.send(bytes). 
    # Não esqueça de converter de string para bytes com encode()

    if console is not None:
        msg = 'Sensores conectados: ' + ','.join(SENSORES.keys())
        converter = msg.encode("utf-8")
        console.send(converter)

    # fazLog('esqueci de fazer o exercicio 3\n') # comente quando fizer o exercicio

def exercicio4(SENSORES: dict, commando: str):
    '''
    Envia o mesmo comando para todos os sensores conectados
    
    Parametros:
    SENSORES: dicionario que associa o id do sensor e sua conexão TCP
    commando: string com o comando para o usuário - precisa ser convertida para bytes
    '''

    # DICA: a conexão de cada um dos sensores conectados está em SENSORES.values()
    # Faça um for para executar conexao_do_sensor.send(bytes)
    # Não esqueça de converter de string para bytes com encode()

    for conexao in SENSORES.values():
        conexao.send(commando.encode("utf-8"))
    
    # fazLog('esqueci de fazer o exercicio 4\n') # comente quando fizer o exercicio

def exercicio5(s: socket, addr: tuple):
    '''
    Faz a conexão com o monitor
    - caso o monitor responda retorna imediatamente
    - caso o monitor não responda, tenta novamente em intervalos de 10 segundos
    
    Parametros:
    s: socket do tipo cliente usado pelo dispositivo de IoT
    addr: tupla com o ip e porta do monitor
    '''
    
    # DICA: coloque o código abaixo em um while True
    # caso o não caia na exceção, coloque um return abaixo do connect
    # substitua o print da exceção por um time.sleep(10)

    while True:
        try:
            s.connect(addr)
            return
        except:
            time.sleep(10)
        
    # fazLog('esqueci de fazer o exercicio 5\n') # comente quando fizer o exercicio

def exercicio6(s: socket, sensor: str, estado: str):
    '''
    Envia o estado de um sensor para o monitor 
    - formato da mensagem: sensor=estado\n
    
    Parametros:
    s: socket com a conexão entre o dispositivo de IoT e o monitor
    estado: string com o estado do dispositivo de IoT
    '''
    
    # DICA: monte a string a ser enviada f'{sensor}={estado}\n'
    # converta para bytes
    # envie com s.send(bytes)

    envio = f'{sensor}={estado}\n'
    s.send(envio.encode("utf-8"))

    # fazLog('esqueci de fazer o exercicio 6\n') # comente quando fizer o exercicio


    #---------------------------------------------------------------------
    # A ENTREGA DA SOMATIVA É ESTE ARQUIVO
    # COPIE O RESULTADO DO ARQUIVO log.txt E COLE ABAIXO PARA ENTREGAR A TAREFA

'''
2023-09-26 20:26:05.002877 : MONITOR: aguardando dispositivos de IOT em 9999
2023-09-26 20:26:05.002931 : CONSOLE: aguardando conexão do usuário em 8888
2023-09-26 20:26:17.179426 : MONITOR: o sensor sala registrou: ('127.0.0.1', 50542)
2023-09-26 20:26:17.179624 : MONITOR: o sensor quarto registrou: ('127.0.0.1', 50543)
2023-09-26 20:26:17.181908 : MONITOR: o sensor cozinha registrou: ('127.0.0.1', 50544)
2023-09-26 20:26:33.445750 : CONSOLE: O usuário conectou
2023-09-26 20:26:33.454649 : CONSOLE RECEBEU: sala ligar
2023-09-26 20:26:33.454911 : IOT sala: recebeu o comando=ligar
2023-09-26 20:26:33.484611 : USUARIO RECEBEU: CONSOLE: digite SENSOR_ID COMANDO

2023-09-26 20:26:34.456397 : CONSOLE RECEBEU: sala consulta
2023-09-26 20:26:34.456646 : IOT sala: recebeu o comando=consulta
2023-09-26 20:26:34.456887 : MONITOR: sensor sala enviou sala=ON
2023-09-26 20:26:34.457129 : USUARIO RECEBEU: sala=ON

2023-09-26 20:26:35.461975 : CONSOLE RECEBEU: todos consulta
2023-09-26 20:26:35.462844 : IOT sala: recebeu o comando=consulta
2023-09-26 20:26:35.462896 : IOT quarto: recebeu o comando=consulta
2023-09-26 20:26:35.463030 : IOT cozinha: recebeu o comando=consulta
2023-09-26 20:26:35.463306 : MONITOR: sensor sala enviou sala=ON
2023-09-26 20:26:35.463536 : MONITOR: sensor quarto enviou quarto=OFF
2023-09-26 20:26:35.463742 : MONITOR: sensor cozinha enviou cozinha=OFF
2023-09-26 20:26:35.463837 : USUARIO RECEBEU: sala=ON

2023-09-26 20:26:35.464153 : USUARIO RECEBEU: quarto=OFF
cozinha=OFF

2023-09-26 20:26:36.467001 : CONSOLE RECEBEU: quarto shutdown
2023-09-26 20:26:36.467772 : IOT quarto: recebeu o comando=shutdown
2023-09-26 20:26:36.468148 : IOT quarto: SHUTDOWN, BYE!
2023-09-26 20:26:36.468297 : MONITOR: sensor quarto encerrou
2023-09-26 20:26:37.472146 : CONSOLE RECEBEU: quarto consulta
2023-09-26 20:26:37.472734 : CONSOLE: O sensor quarto nao existe
2023-09-26 20:26:37.473080 : USUARIO RECEBEU: O sensor quarto nao existe

2023-09-26 20:26:37.473381 : USUARIO RECEBEU: Sensores conectados: sala,cozinha
'''