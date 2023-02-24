#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import serial
import keyboard
 
comport = serial.Serial('COM4', 9600)
 
TEMP_ASCII=str(chr(116))
VEL0_ASCII=str(chr(117))
VEL1_ASCII=str(chr(118))
VEL2_ASCII=str(chr(119))
VEL3_ASCII=str(chr(120))
LED0_ASCII=str(chr(121))
LED1_ASCII=str(chr(122))

time.sleep(1.8) 
 
def monitorar_temperatura():
    comport.write(TEMP_ASCII.encode())
    VALUE_SERIAL=comport.readline()
    print('\nRetorno da serial: %s' % (VALUE_SERIAL))

def ligar_desligar_led(estado):
    if estado:
        comport.write(LED1_ASCII.encode())
        VALUE_SERIAL=comport.readline()
        print('\nRetorno da serial: %s' % (VALUE_SERIAL))
    else:
        comport.write(LED0_ASCII.encode())
        VALUE_SERIAL=comport.readline()
        print('\nRetorno da serial: %s' % (VALUE_SERIAL))

# Função para ajustar velocidade do motor (exemplo fictício)
def ajustar_motor(velocidade):
    if velocidade == 0 :
        comport.write(VEL0_ASCII.encode())
        VALUE_SERIAL=comport.readline()
        print('\nRetorno da serial: %s' % (VALUE_SERIAL))
    
    if velocidade == 1 :
        comport.write(VEL1_ASCII.encode())
        VALUE_SERIAL=comport.readline()
        print('\nRetorno da serial: %s' % (VALUE_SERIAL))

    if velocidade == 2 :
        comport.write(VEL2_ASCII.encode())
        VALUE_SERIAL=comport.readline()
        print('\nRetorno da serial: %s' % (VALUE_SERIAL))

    if velocidade == 3 :
        comport.write(VEL3_ASCII.encode())
        VALUE_SERIAL=comport.readline()
        print('\nRetorno da serial: %s' % (VALUE_SERIAL))

while True:
    # Exibir opções do menu
    print("\nSelecione uma das opções:")
    print("1 - Ligar/Desligar LED")
    print("2 - Ajustes do motor")
    print("3 - Relatório de temperatura")
    print("4 - Sair")

    # Ler opção selecionada pelo usuário
    opcao = input("Opção selecionada: ")

    if opcao == "1":
        estado_led = input("Ligar ou desligar o LED? (L/D): ")
        if estado_led.lower() == "l":
            ligar_desligar_led(True)
        elif estado_led.lower() == "d":
            ligar_desligar_led(False)
        else:
            print("Opção inválida!")

    elif opcao == "2":
        # Pedir ao usuário para informar qual velocidade deseja ajustar o motor
        velocidade = input("Ajustar velocidade do motor para (0-3): ")
        if velocidade.isdigit() and int(velocidade) in [0, 1, 2, 3]:
            ajustar_motor(int(velocidade))
        else:
            print("Opção inválida!")

    elif opcao == "3":
            print("Iniciando leitura...")
            while True:
                monitorar_temperatura()
                time.sleep(1)
                if keyboard.is_pressed('enter'):
                    print("Leitura interrompida.")
                    break

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")

comport.close()