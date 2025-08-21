/// Defining Sensor Input Data , Last force , and Threshold( which is for appogee)
int sensorPin = A0;
int lastForce = 0;
int threshold = 2;

// Now we have Leds  connected to pin 2,3,4 and Buzzer to 5  
// for us to easy understanding we are giving them name 
int ledAscending = 2;
int ledApogee    = 3;
int ledDescending = 4;
int buzzer = 5;

// State when force is 0
String state = "idle";



void setup() {
  
// to make a connection with Aurdino
  Serial.begin(9600);
// here we are defining that pins are OUTPUT or INPUT , in our case Leds are output so 
  pinMode(ledAscending, OUTPUT);
  pinMode(ledApogee, OUTPUT);
  pinMode(ledDescending, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  
// this line gives Sensor data to currentForce variable
  int currentForce = analogRead(sensorPin);

// here decision 
  if (currentForce > lastForce + threshold) {
    state = "ascending";
  } 
  else if (currentForce < lastForce - threshold) {
    if (state == "ascending") {
      state = "apogee";       // peak point
      tone(buzzer, 1000, 300); // short beep
    } else {
      state = "descending";
    }
  }

  
  if (state == "ascending") {
    digitalWrite(ledAscending, HIGH);
    digitalWrite(ledApogee, LOW);
    digitalWrite(ledDescending, LOW);
  } 
  else if (state == "apogee") {
    digitalWrite(ledAscending, LOW);
    digitalWrite(ledApogee, HIGH);
    digitalWrite(ledDescending, LOW);
  } 
  else if (state == "descending") {
    digitalWrite(ledAscending, LOW);
    digitalWrite(ledApogee, LOW);
    digitalWrite(ledDescending, HIGH);
  }

  Serial.print("Force: ");
  Serial.print(currentForce);
  Serial.print(" | State: ");
  Serial.println(state);

  lastForce = currentForce; // update for next loop
  delay(200);
}

// Hail TEAM JANUS
