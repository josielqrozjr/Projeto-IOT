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

    t = Thread(target=Console, args=(CONSOLE, SENSORES, sudp))
    t.start()

    # fazLog('esqueci de fazer o exercicio 1\n') # comente quando fizer o exercicio

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
  
    s.sendto(comando.encode("utf-8"), SENSORES[id])

    # fazLog('esqueci de fazer o exercicio 2\n') #comente quando fizer o exercicio
 

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

    for conexao in SENSORES.values():
        s.sendto(comando.encode("utf-8"), conexao)

    # fazLog('esqueci de fazer o exercicio 3\n') # comente quando fizer o exercicio

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

    mensagem = f'ESTADO {sensor}={estado}\n'
    s.sendto(mensagem.encode("utf-8"), monitor)

    # fazLog('esqueci de fazer o exercicio 4\n') # comente quando fizer o exercicio

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
    
    # fazLog('esqueci de fazer o exercicio 5\n') # comente quando fizer o exercicio
    
    try:
        s.settimeout(60)
        dados, endereco = s.recvfrom(1024)
        s.settimeout(None) # coloca o timeout no default      
        return dados, endereco
    except:
        return None, None
    

    #---------------------------------------------------------------------
    # A ENTREGA DA SOMATIVA É ESTE ARQUIVO
    # COPIE O RESULTADO DO ARQUIVO log.txt E COLE ABAIXO PARA ENTREGAR A TAREFA

''''
2023-09-26 21:05:33.149224 : MONITOR: aguardando dispositivos de IOT em 9999
2023-09-26 21:05:33.149244 : CONSOLE: aguardando conexão do usuário em 8888
2023-09-26 21:05:59.308422 : SENSOR quarto: registrou no Monitor ('127.0.0.1', 9999)
2023-09-26 21:05:59.308448 : MONITOR: o sensor quarto registrou: ('127.0.0.1', 60191)
2023-09-26 21:05:59.308555 : MONITOR: o sensor sala registrou: ('127.0.0.1', 62558)
2023-09-26 21:05:59.308686 : SENSOR sala: registrou no Monitor ('127.0.0.1', 9999)
2023-09-26 21:05:59.309910 : MONITOR: o sensor cozinha registrou: ('127.0.0.1', 54446)
2023-09-26 21:05:59.309957 : SENSOR cozinha: registrou no Monitor ('127.0.0.1', 9999)
2023-09-26 21:06:15.138354 : CONSOLE: O usuário conectou
2023-09-26 21:06:15.147557 : CONSOLE RECEBEU: sala ligar
2023-09-26 21:06:15.147871 : IOT sala: recebeu o comando=ligar
2023-09-26 21:06:15.177986 : USUARIO RECEBEU: CONSOLE: digite SENSOR_ID COMANDO

2023-09-26 21:06:16.150110 : CONSOLE RECEBEU: sala consulta
2023-09-26 21:06:16.150330 : IOT sala: recebeu o comando=consulta
2023-09-26 21:06:16.150481 : MONITOR: sensor sala enviou sala=ON

2023-09-26 21:06:16.150715 : USUARIO RECEBEU: sensor sala enviou sala=ON

2023-09-26 21:06:59.308131 : MONITOR: o sensor quarto registrou: ('127.0.0.1', 60191)
2023-09-26 21:06:59.308171 : SENSOR quarto: registrou no Monitor ('127.0.0.1', 9999)
2023-09-26 21:06:59.309201 : MONITOR: o sensor cozinha registrou: ('127.0.0.1', 54446)
2023-09-26 21:06:59.309304 : SENSOR cozinha: registrou no Monitor ('127.0.0.1', 9999)
2023-09-26 21:07:16.150198 : SENSOR sala: registrou no Monitor ('127.0.0.1', 9999)
2023-09-26 21:07:16.150249 : CONSOLE RECEBEU: todos ligar
2023-09-26 21:07:16.150427 : MONITOR: o sensor sala registrou: ('127.0.0.1', 62558)
2023-09-26 21:07:16.150868 : IOT sala: recebeu o comando=ligar
2023-09-26 21:07:16.150971 : IOT quarto: recebeu o comando=ligar
2023-09-26 21:07:16.150964 : IOT cozinha: recebeu o comando=ligar
2023-09-26 21:07:17.150750 : CONSOLE RECEBEU: todos consulta
2023-09-26 21:07:17.151565 : IOT quarto: recebeu o comando=consulta
2023-09-26 21:07:17.151625 : IOT cozinha: recebeu o comando=consulta
2023-09-26 21:07:17.151635 : IOT sala: recebeu o comando=consulta
2023-09-26 21:07:17.151989 : MONITOR: sensor quarto enviou quarto=ON

2023-09-26 21:07:17.152291 : MONITOR: sensor cozinha enviou cozinha=ON

2023-09-26 21:07:17.152555 : MONITOR: sensor sala enviou sala=ON

2023-09-26 21:07:17.152701 : USUARIO RECEBEU: sensor quarto enviou quarto=ON

2023-09-26 21:07:17.153028 : USUARIO RECEBEU: sensor cozinha enviou cozinha=ON
sensor sala enviou sala=ON

2023-09-26 21:07:24.791268 : CONSOLE: aguardando conexão do usuário em 8888
'''