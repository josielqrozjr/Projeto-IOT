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
        except Exception as e:
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

    fazLog('esqueci de fazer o exercicio 6\n') # comente quando fizer o exercicio


    #---------------------------------------------------------------------
    # A ENTREGA DA SOMATIVA É ESTE ARQUIVO
    # COPIE O RESULTADO DO ARQUIVO log.txt E COLE ABAIXO PARA ENTREGAR A TAREFA