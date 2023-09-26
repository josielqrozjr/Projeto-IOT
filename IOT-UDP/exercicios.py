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

def exercicio1(CONSOLE: list, SENSORES: dict, sudp: socket):
    '''
    Lança o Console como uma Thread

    Parametros:
    CONSOLE: lista usada para salvar o socket que representa a conexão TCP com o usuário
    SENSORES: dicionario que associa o id do sensor e sua conexão TCP
    sudp: socket udp usada na comunicaçao com os sensores
    '''

    # DICA: Para chamar uma thread: Thread(target=, args=) 
    # Use a chamada de TrataSensor em monitor.py como exemplo
    # Veja a definição da função Console e passe os argumentos na ordem correta
    # Não esqueça do start()

    fazLog('esqueci de fazer o exercicio 1\n') # comente quando fizer o exercicio

def exercicio2(s: socket, SENSORES: dict, id: str, comando: str):
    '''
    Envia um comando em unicast para um sensor

    Parametros:
    s: socket udp que se comunica com os sensores
    SENSORES: dicionário que contém o endereço dos sensores
    id: identificador do sensor
    comando: comando que deve ser enviado
    '''

    # DICA: obtenha o endereço do sensor a partir do dicionário SENSORES
    # use a função s.sendto(bytes, endereço) para enviar o comando que deve ser convertido para bytes   
  
    fazLog('esqueci de fazer o exercicio 2\n') #comente quando fizer o exercicio
 

def exercicio3(s: socket, SENSORES: dict, comando: str):
    '''
    Envia o mesmo comando para todos os sensores
    
    Parametros:
    s: socket udp que se comunica com os sensores
    SENSORES: dicionario que associa o id do sensor e seu endereço
    commando: string com o comando para o usuário - precisa ser convertida para bytes
    '''

    # DICA: os endereços dos sensores registrados estão em SENSORES.values()
    # Faça um for para enviar o mesmo comando com sendto(bytes, endereço)

    fazLog('esqueci de fazer o exercicio 3\n') # comente quando fizer o exercicio

def exercicio4(s: socket, sensor: str, estado: str, monitor: tuple):
    '''
    Envia o estado de um sensor para o monitor 
    - formato da mensagem: ESTADO sensor=estado\n
    
    Parametros:
    s: socket udp usado para se comunicar com o monitor
    sensor: id do dispositivo de IoT
    estado: string com o estado do sensor
    monitor: endereço do monitor (ip, porta)
    '''
    
    # DICA: monte a string a ser enviada f'ESTADO {sensor}={estado}\n'
    # converta para bytes
    # envie com s.sendto(bytes, addr)

    fazLog('esqueci de fazer o exercicio 4\n') # comente quando fizer o exercicio

def exercicio5(s: socket)-> tuple:
    '''
    Aguarda no máximo 60 segundos até receber uma mensagem.
     - Caso a mensagem seja recebida, retorna uma tupla (dados, endereco do transmissor)
     - Caso não seja recebida, retorna a tupla (None, None)
    
    Parametros:
    s: socket do tipo cliente usado pelo dispositivo de IoT
    '''
    
    # DICA: crie uma estrutura try e except
    # coloque s.settimeout(60) no try seguido das tres linhas que já estão no código
    # no except retorne None,None
    
    fazLog('esqueci de fazer o exercicio 5\n') # comente quando fizer o exercicio
    
    dados, endereco = s.recvfrom(1024)
    s.settimeout(None) # coloca o timeout no default      
    return dados, endereco
    

    #---------------------------------------------------------------------
    # A ENTREGA DA SOMATIVA É ESTE ARQUIVO
    # COPIE O RESULTADO DO ARQUIVO log.txt E COLE ABAIXO PARA ENTREGAR A TAREFA