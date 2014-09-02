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

  colorWipe(strip.Color(255,255,255),50);
  colorWipe(strip.Color(0,0,0),50);
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

	char ci[3]={0};
	char cr[4]={0};
	char cg[4]={0};
	char cb[4]={0};

	ci[0]=buf[0];
	ci[1]=buf[1];

	cr[0]=buf[2];
	cr[1]=buf[3];
	cr[2]=buf[4];

	cg[0]=buf[5];
	cg[1]=buf[6];
	cg[2]=buf[7];

	cb[0]=buf[8];
	cb[1]=buf[9];
	cb[2]=buf[10];

	int i,r,g,b;

	i = atoi(ci);
	r = atoi(cr);
	g = atoi(cg);
	b = atoi(cb);

	strip.setPixelColor(i,strip.Color(r,g,b));
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
