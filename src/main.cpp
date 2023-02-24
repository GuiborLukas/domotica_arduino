#include <Arduino.h>

int PinAnalogLM35 = 0;    //Setando Pino A0
float valAnalog = 0;    // Iniciando variavel valAnalog como 0
float temp = 0;        //Iniciando variavel temp como 0

int potValueMotor = 0;
int transistor = 4;
int pinLed = 2;

void setup(){
    Serial.begin(9600);
    pinMode(transistor, INPUT);
    pinMode(pinLed, OUTPUT);
}
 
void loop(){
    if (Serial.available() > 0){
        char leitura = Serial.read();
        if (leitura == 116){ // TEMP_ASCII
            valAnalog = analogRead(PinAnalogLM35);
            temp = valAnalog * 0.0048828125 * 100;
            Serial.print("Temperatura = "); //IMPRIME O TEXTO NA SERIAL
            Serial.println(temp);          
        }

        if (leitura == 117){ // VEL0_ASCII
            potValueMotor = 0;
            analogWrite(transistor, potValueMotor);
            Serial.println("Velocidade 0 definida"); //IMPRIME O TEXTO NA SERIAL
        }

        if (leitura == 118){ // VEL1_ASCII
            potValueMotor = 340 / 4;
            analogWrite(transistor, potValueMotor);
            Serial.println("Velocidade 1 definida"); //IMPRIME O TEXTO NA SERIAL
        }

        if (leitura == 119){ // VEL2_ASCII
            potValueMotor = 680 / 4;
            analogWrite(transistor, potValueMotor);
            Serial.println("Velocidade 2 definida"); //IMPRIME O TEXTO NA SERIAL
        }

        if (leitura == 120){ // VEL3_ASCII
            potValueMotor = 1023 / 4;
            analogWrite(transistor, potValueMotor);
            Serial.println("Velocidade 3 definida"); //IMPRIME O TEXTO NA SERIAL
        }

        if (leitura == 121){ // LED0_ASCII
            digitalWrite(pinLed, LOW);
            Serial.println("LED desligado"); //IMPRIME O TEXTO NA SERIAL
        }

        if (leitura == 122){ // LED1_ASCII
            digitalWrite(pinLed, HIGH);
            Serial.println("LED ligado"); //IMPRIME O TEXTO NA SERIAL
        }
    }
}