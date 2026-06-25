#include <Servo.h>

Servo servo;

#define ECHO 4 
#define TRIG 5 
#define SERVO 3 

#define POSICAO_MINIMA 0 
#define POSICAO_MAXIMA 90 

#define DELAY_POSICAO_MINIMA 0 
#define DELAY_POSICAO_MAXIMA 5 

#define DELAY_FECHAR_LIXEIRA 2000 
#define DELAY_ABRIR_LIXEIRA 500 

#define DISTANCIA_MINIMA_ABRIR 20

unsigned long tempo;
double distancia;

int posicao_atual;
bool lixeira_fechada = true;

void setup() 
{
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  Serial.begin(9600);

  digitalWrite(TRIG, LOW);

  servo.attach(SERVO);
}

void loop() 
{
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  tempo = pulseIn(ECHO, HIGH);

  distancia = tempo/58;

  Serial.println(distancia);

  if(distancia < DISTANCIA_MINIMA_ABRIR)
  {
    //Abre a lixeira
    posicao_atual = servo.read();

    for(int i=posicao_atual; i<=POSICAO_MAXIMA; i++)
    {
      servo.write(i);
      delay(DELAY_POSICAO_MAXIMA);
    }

    lixeira_fechada = false;
  }
  else
  {
    //Fecha a lixeira
    posicao_atual = servo.read();

    for(int i=posicao_atual; i>=POSICAO_MINIMA; i--)
    {
      servo.write(i);
      delay(DELAY_POSICAO_MINIMA);
    }

    lixeira_fechada = true;
  }

  if(lixeira_fechada)
  {
    delay(DELAY_ABRIR_LIXEIRA);
  }
  else
  {
    delay(DELAY_FECHAR_LIXEIRA);
  }
}
