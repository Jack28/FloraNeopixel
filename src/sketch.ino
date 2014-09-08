#include <Adafruit_NeoPixel.h>

#define PIN 6

// Parameter 1 = number of pixels in strip
// Parameter 2 = Arduino pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(16, PIN, NEO_GRB + NEO_KHZ800);

// bla bla bla

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.

void setup() {
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'

//  
//	int c1=strip.Color(50,50,50);
//	int c0=strip.Color(0,0,0);
//	 for(int i=0;i<1024;i++){ // count from 0 to 1023
//		int bin=log(i) / log(2); // get bit count
//		for(int j=0;j<bin;j++){ // go from 0 to bit count
//			if ((i>>(i-j))%2) // shift
//    		 strip.setPixelColor(j,c1);
//			else
//    		 strip.setPixelColor(j,c0);
//		}
//		delay(50);
//      strip.show();
//	}
//
  colorWipe(strip.Color(55,55,55),20);
  colorWipe(strip.Color(0,0,0),0);
  Serial.begin(9600);
}

String content = "";
char character;

void run(String command){
	// 2 3 3 3 --- 11
	if (command == "show\n" || command == "show\r" || command == "show\0"){
		strip.show();
		return;
	}

	char buf[13]={0};

	command.toCharArray(buf,command.length());

	int led,r,g,b;
	sscanf(buf, "%1x%2x%2x%2x", &led,&r,&g,&b);
//	Serial.print(led);
//	Serial.print(" ");
//	Serial.print(r);
//	Serial.print(" ");
//	Serial.print(g);
//	Serial.print(" ");
//	Serial.println(b);

	strip.setPixelColor(led,strip.Color(r,g,b));
}

void loop()
{
	while(Serial.available()) {
		character = Serial.read();
		if (character == '\n' || character == '\r' || character == 0){
			content.concat(character);
			run(content);
			content="";
			character=0;
		} else {
			content.concat(character);
		}
	}
}

// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, c);
      strip.show();
      delay(wait);
  }
}
