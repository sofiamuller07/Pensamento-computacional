// C++ code
//
int p1 = 0;

int modo = 0;

void setup()
{
  pinMode(A4, INPUT);
  pinMode(2, INPUT);
  pinMode(4, INPUT);
  pinMode(7, INPUT);
  pinMode(9, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop()
{
  p1 = map(analogRead(A4), 0, 1023, 0, 255);
  if (digitalRead(2) == 1) {
    modo = 1;
  }
  if (digitalRead(4) == 1) {
    modo = 2;
  }
  if (digitalRead(7) == 1) {
    modo = 3;
  }
  if (modo == 1) {
    analogWrite(9, 0);
    analogWrite(11, 0);
    analogWrite(10, p1);
  }
  if (modo == 2) {
    analogWrite(9, p1);
    analogWrite(11, 0);
    analogWrite(10, p1);
  }
  if (modo == 3) {
    analogWrite(9, p1);
    analogWrite(11, 0);
    analogWrite(10, 0);
  }
  delay(10); // Delay a little bit to improve simulation performance
}
