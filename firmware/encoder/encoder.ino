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

long oldMillis;
long newMillis;
long oldPosition;
long newPosition;

long dx;
double dt;
double omega;
double t = 0;

void setup() {
  Serial.begin(2000000);
  Serial.println("<Arduino is ready>");
  oldMillis = millis();
  oldPosition  = myEnc.read();

}


void loop() {
  newPosition = myEnc.read();
  dx = newPosition - oldPosition;

  newMillis = millis();
  dt = newMillis - oldMillis;

  if (abs(dx) > 0) {
    //if (abs(dx) > 0) {
    //t = t + dt;
    //omega = dx * 250 / dt / 3;

    Serial.print("<");
    Serial.print(t / 1000);
    Serial.print(",");
    Serial.print(newPosition);
    Serial.println(">");

    oldMillis = newMillis;

    oldPosition = newPosition;
    //}
    // long toprint = oldPosition/4/3;
    //Serial.println(toprint);
  }
}
