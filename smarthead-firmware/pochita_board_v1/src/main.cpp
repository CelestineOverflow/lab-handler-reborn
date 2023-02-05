#include <Arduino.h>
#include <Wire.h>
#include "HX711.h"
#include <stdio.h>


// Calibrated 16.08
static double CALIBRATED_DIVISOR = 221.512;
static long CALIBRATED_OFFSET = 22603;
// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 3;
const int LOADCELL_SCK_PIN = 2;
const int PROBE_OUT = A6;
HX711 scale;

#define DEBUG 0 // 1 for calibrating
#define DEBUG_SERIAL Serial1 // 
#define EEPROM_SIZE 128

void setup()
{
  DEBUG_SERIAL.begin(115200);
  //start DEBUG_SERIAL port in pin 4 and 5
  
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  pinMode(PROBE_OUT, OUTPUT);
  // Wire.begin(2);                // join i2c bus with address #2 
  // Wire.onRequest(requestEvent); // register event 
}

double static lastReading = 0.0;
double static lastReadingFluke = 0.0;
double static delta = 1000.0;
double static pressureThreshold = 1000.0;
bool triggerModeActive = true;
int count = 0;
void loop()
{
  if (scale.is_ready())
  {
    if (DEBUG)
    {
      long reading = scale.read();
      DEBUG_SERIAL.print("G28\r");
      DEBUG_SERIAL.println(reading);
      reading -= CALIBRATED_OFFSET;
      DEBUG_SERIAL.print("HX711 reading with offset: ");
      DEBUG_SERIAL.println(reading);
      double actual_reading = (double)reading / CALIBRATED_DIVISOR;
      DEBUG_SERIAL.print("HX711 reading: ");
      DEBUG_SERIAL.println(actual_reading);
      delay(1000);
    }
    else
    {
      double reading = (double)(scale.read() - CALIBRATED_OFFSET) / CALIBRATED_DIVISOR;
      DEBUG_SERIAL.println(reading);
      if (triggerModeActive && abs(reading) > pressureThreshold )// 
      {
        digitalWrite(PROBE_OUT, HIGH);
      }
      else
      {
        digitalWrite(PROBE_OUT, LOW);
      }
    }
  }
}



/*---------------------------------------------------------------------------------------------------------------------+
|                                .                  COMMANDS                                                            |
+---------------------------------------------------------------------------------------------------------------------*/
/*----trigger on/off----*/
/*----set <pressure>----*/
/*----calibrate----*/
void DEBUG_SERIALEvent()
{
  String input = "";
  while (DEBUG_SERIAL.available())
  {
    char inputChar = DEBUG_SERIAL.read();
    input += inputChar;
    if (inputChar == '\n')
    {
      // split input into tokens
      String tokens[3];
      int tokenCount = 0;
      int tokenStart = 0;
      for (int i = 0; i < input.length(); i++)
      {
        DEBUG_SERIAL.println("processing trigger");
       if (input.charAt(i) == ' ' || input.charAt(i) == '\n')
        {
          tokens[tokenCount] = input.substring(tokenStart, i);
          tokenCount++;
          tokenStart = i + 1;
        }
      }
      // process tokens
      if (tokens[0] == "set")
      {
        DEBUG_SERIAL.println("processing set");
        pressureThreshold = tokens[1].toDouble();
        DEBUG_SERIAL.print("New threshold: ");
        DEBUG_SERIAL.println(pressureThreshold);
        // DEBUG_SERIAL.printf("New threshold: %f\n", pressureThreshold);
      }
      else if (tokens[0] == "trigger")
      {
         triggerModeActive = tokens[1] == "on";
        // DEBUG_SERIAL.printf("Trigger mode: %s\n", triggerModeActive ? "on" : "off");
        DEBUG_SERIAL.println("trigger mode");
        DEBUG_SERIAL.println(triggerModeActive ? "on" : "off");
      }
      else if (tokens[0] == "calibrate")
      {
        // CALIBRATED_DIVISOR = tokens[1].toDouble();
        // CALIBRATED_OFFSET = tokens[2].toInt();
      }
    }
  }
}
