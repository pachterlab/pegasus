/* Encoder Library - Basic Example
   http://www.pjrc.com/teensy/td_libs_Encoder.html

   This example code is in the public domain.
*/

#include <Encoder.h>

// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
Encoder myEnc(2, 3);
//   avoid using pins with LEDs attached
unsigned long currMillis;
unsigned long oldMillis;
unsigned long dt;
float omega;

void setup() {
  Serial.begin(9600);
  Serial.println("Basic Encoder Test:");
  currMillis = millis();
}

long oldPosition  = -999;

void loop() {
  long newPosition = myEnc.read();
  if (newPosition != oldPosition) {
    oldMillis = currMillis;
    currMillis = millis();
    dt = currMillis - oldMillis;
    // if ( dt != 0) {
    //  omega = (newPosition - oldPosition) / dt;
    //  oldPosition = newPosition;
      Serial.println(newPosition);
    //}
  }
}
