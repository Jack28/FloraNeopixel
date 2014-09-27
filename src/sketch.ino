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

  colorWipe(strip.Color(55,55,55),20);
  colorWipe(strip.Color(0,0,0),0);
  Serial.begin(9600);

  animationSetup();
  animationLoop();
}

short pos=0;
char symbol=0;

short digits[7]={0};

void loop()
{
START:
	while(Serial.available()) {
		symbol = Serial.read();
		digits[pos]=symbol - (symbol >= 'a' ? 'a' - 10 : '0');

		switch (symbol){
			case '.':
				delay(10);
goto START;
			case 's':
				strip.show();
				pos=0;
goto START;
			default:
				if (pos == 6){
					pos=0;
					strip.setPixelColor(digits[0],strip.Color(
						(digits[1]<<4)+digits[2],
						(digits[3]<<4)+digits[4],
						(digits[5]<<4)+digits[6])
					);
goto START;
				} else
					pos++; 
		}
	}
goto START;
}









// ANIMATION THINGS

void animationSetup() {
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}

void animationLoop() {
  while (1) {
	  // Some example procedures showing how to display to the pixels:
	  colorWipe(strip.Color(255, 0, 0), 50); // Red
	  if (Serial.available())
		break;
	  colorWipe(strip.Color(0, 255, 0), 50); // Green
	  if (Serial.available())
		break;
	  colorWipe(strip.Color(0, 0, 255), 50); // Blue
	  if (Serial.available())
		break;
	  // Send a theater pixel chase in...
	  theaterChase(strip.Color(127, 127, 127), 50); // White
	  if (Serial.available())
		break;
	  theaterChase(strip.Color(127,   0,   0), 50); // Red
	  if (Serial.available())
		break;
	  theaterChase(strip.Color(  0,   0, 127), 50); // Blue
	  if (Serial.available())
		break;

	  rainbow(20);
	  if (Serial.available())
		break;
	  rainbowCycle(20);
	  if (Serial.available())
		break;

	  theaterChaseRainbow(50);
	  if (Serial.available())
		break;
	  chaseColor(strip.Color(50,50,50),50,3,5);
	  if (Serial.available())
		break;
	  strobe();
	  if (Serial.available())
		break;
	  roll();
	  if (Serial.available())
		break;
	  rolll();
	  if (Serial.available())
		break;
	  move();
	  if (Serial.available())
		break;
	  //delay(2000);
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

void chaseColor(uint32_t c, uint8_t wait, int num, int rounds) {
	int start=0;
	int r=0;
	while(r<rounds*strip.numPixels()){
		strip.setPixelColor((start)%strip.numPixels(),c);
		strip.setPixelColor((start-3)%strip.numPixels(),strip.Color(0,0,0));
		strip.show();
		delay(wait);
		start=(start+1)%strip.numPixels();
		r++;
	}
}

void rainbow(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j<256; j++) {
    for(i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel((i+j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

// Slightly different, this makes the rainbow equally distributed throughout
void rainbowCycle(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j<256*5; j++) { // 5 cycles of all colors on wheel
    for(i=0; i< strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

//Theatre-style crawling lights.
void theaterChase(uint32_t c, uint8_t wait) {
  for (int j=0; j<10; j++) {  //do 10 cycles of chasing
    for (int q=0; q < 3; q++) {
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, c);    //turn every third pixel on
      }
      strip.show();
     
      delay(wait);
     
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, 0);        //turn every third pixel off
      }
    }
  }
}

//Theatre-style crawling lights with rainbow effect
void theaterChaseRainbow(uint8_t wait) {
  for (int j=0; j < 256; j++) {     // cycle all 256 colors in the wheel
    for (int q=0; q < 3; q++) {
        for (int i=0; i < strip.numPixels(); i=i+3) {
          strip.setPixelColor(i+q, Wheel( (i+j) % 255));    //turn every third pixel on
        }
        strip.show();
       
        delay(wait);
       
        for (int i=0; i < strip.numPixels(); i=i+3) {
          strip.setPixelColor(i+q, 0);        //turn every third pixel off
        }
    }
  }
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  if(WheelPos < 85) {
   return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  } else if(WheelPos < 170) {
   WheelPos -= 85;
   return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else {
   WheelPos -= 170;
   return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
}


void strobe(){
	// 16
	int q=0;
	int r=0;
	while (r<64){
		// swith all off
		for (int i=0;i<16;i++)
			strip.setPixelColor(i,strip.Color(0,0,0));
		// switch 5 on
		for (int i=0;i<3;i++)
			strip.setPixelColor(i+q,strip.Color(255,255,255));
		strip.show();
		delay(40);
		q=rand()%16;
		r++;
	}
}

void roll(){
	int step=1;
	int count=0;
	int q=0;
	while (count<64){
		for (int i=0;i<5;i++)
			strip.setPixelColor(i+q,strip.Color(0,50*(i==0||i==4?0.2:1),0));
		strip.show();
		delay(50);
		for (int i=0;i<5;i++)
			strip.setPixelColor(i+q,strip.Color(0,0,0));
		q=q+step;
		if (q+5>16 || q<0)
			step=step*-1;
		count++;
	}
}

void rolll(){
	int step=1;
	int count=0;
	int q=0;
	int i=0;
	while (count<20){
			strip.setPixelColor((i+q)%16,strip.Color(50,0,0));
			strip.setPixelColor((15-((q-i))%16)%16,strip.Color(0,50,0));
		strip.show();
		delay(70);
			strip.setPixelColor((i+q)%16,strip.Color(0,0,0));
			strip.setPixelColor((15-((q-i))%16)%16,strip.Color(0,0,0));
		q=q+step;
		if (q+1>=8 || q-1<0){
			step=step*-1;
			i+=1;
			count++;
		}
	}
}

void move(){
	int q=0;
	int i=0;
	while (q<16*3){
		// show base
		for (i=0;i<6;i++)
			strip.setPixelColor((i+q)%16,strip.Color(50,0,0));
		strip.show();
		for (i=16;i>=6;i--){
			strip.setPixelColor((i+q)%16,strip.Color(50,0,0));
			strip.show();
			delay(50);
			strip.setPixelColor((i+q)%16,strip.Color(0,0,0));
		}
		q=(q+1);//%16;
		i=0;
	}
}
