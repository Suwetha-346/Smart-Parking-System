int irSensor1 = 2;  
int irSensor2 = 3;
int irSensor3 = 4;
int irSensor4 = 5;
int irSensor5 = 6;
int irSensor6 = 7;

void setup() {
  Serial.begin(9600);
  pinMode(irSensor1, INPUT);
  pinMode(irSensor2, INPUT);
  pinMode(irSensor3, INPUT);
  pinMode(irSensor4, INPUT);
  pinMode(irSensor5, INPUT);
  pinMode(irSensor6, INPUT);
}

void loop() {
  if (digitalRead(irSensor1) == LOW) {
    Serial.println("1st parking slot is full");
  } else {
    Serial.println("1st parking slot is empty");
  }

  if (digitalRead(irSensor2) == LOW) {
    Serial.println("2nd parking slot is full");
  } else {
    Serial.println("2nd parking slot is empty");
  }       

  if (digitalRead(irSensor3) == LOW) {
    Serial.println("3rd parking slot is full");
  } else {
    Serial.println("3rd parking slot is empty");
  }

  if (digitalRead(irSensor4) == LOW) {
    Serial.println("4th parking slot is full");
  } else {
    Serial.println("4th parking slot is empty");
  }

  if (digitalRead(irSensor5) == LOW) {
    Serial.println("5th parking slot is full");
  } else {
    Serial.println("5th parking slot is empty");
  }

  if (digitalRead(irSensor6) == LOW) {
    Serial.println("6th parking slot is full");
  } else {
    Serial.println("6th parking slot is empty");
  }
  delay(500);  
}
