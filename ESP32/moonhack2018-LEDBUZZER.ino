/* this is the Moonhack 2018 project using ESP32, to demo the landing sound and blinking LED light */

int freq = 5000;
int ledChannel = 0;
int buzzerChannel = 1;
int resolution = 8;

void setup() {
  Serial.begin(115200);
  ledcSetup(ledChannel, freq, resolution);
  ledcAttachPin(LED_BUILTIN, ledChannel);	// for LED fade
  ledcAttachPin(12, buzzerChannel);			// for buzzer control
}

void loop() {

  ledcWriteTone(buzzerChannel, 2000);			// for buzzer 
  
  for (int dutyCycle = 0; dutyCycle <= 255; dutyCycle+10) {
	Serial.println(dutyCycle);
    ledcWrite(ledChannel, dutyCycle);
	ledcWrite(buzzerChannel, dutyCycle);
    delay(700);
  }

  for (int dutyCycle = 255; dutyCycle >= 0; dutyCycle--) {
    ledcWrite(ledChannel, dutyCycle);
    delay(700);
  }
  
  // buzzer PWM control
  ledcWrite(buzzerChannel, 125);
 
  for (int freq = 255; freq < 10000; freq = freq + 250){
 
     Serial.println(freq);
 
     ledcWriteTone(channel, freq);
     delay(1000);
  }

}