/*
TEST CODE FOR PROXIMITY SENSOR
Metal Detection with 3 wire sensor
*/
float metalDetected;
int monitoring;
int metalDetection = 0;

void setup(){
Serial.begin(9600);
}

void loop(){
monitoring = analogRead(metalDetection);
metalDetected = 100 - (float) monitoring*100/1024.0;
Serial.println("14CORE METAL DETECTOR TEST");
delay(1000);
Serial.println("Initializing Proximity Sensor");
delay(1000);
Serial.println("Please wait...");
delay(1000);
Serial.print("Metal is Proximited = ");
Serial.print(metalDetected);
Serial.println("%");
if (metalDetected > 50)
Serial.println("METAL DETECTED");
delay(1000);
}
