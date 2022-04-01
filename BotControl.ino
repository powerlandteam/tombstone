#include"Con_setup.h"
#include "BluetoothSerial.h"
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;
char input; float voltage;
MCP4822 dac(CS);
void setup() {
  {
    Serial.begin(115200);
    SerialBT.begin("ESP32test"); //Bluetooth device name
    Serial.println("The device started, now you can pair it with bluetooth!");
    // We call the init() method to initialize the instance
    dac.init();
    // The channels are turned off at startup so we need to turn the channel we need on
    dac.turnOnChannelA();
    dac.turnOnChannelB();
  }
  initPins();
  //brake();
}


void loop() {
  BTinit();
  BOTDir();
  DACvlt();
  motorspeed();
}

void BTinit()
{
  if (SerialBT.available())
  {
    input = SerialBT.read();
  }
}

void initPins() {
  //Set motor dir outputs low before setting as output
  setAllNeutral();
  //Motor dir outputs
  setDirPinsAsOutput();

  // Inputs
  //pinMode(Switch, INPUT); ONN-OFF Button
}

void setAllNeutral() {
  digitalWrite(R_F, LOW);
  digitalWrite(L_F, LOW);
  digitalWrite(R_R, LOW);
  digitalWrite(L_R, LOW);
}

void setDirPinsAsOutput() {
  pinMode(R_F, OUTPUT);
  pinMode(L_F, OUTPUT);
  pinMode(R_R, OUTPUT);
  pinMode(L_R, OUTPUT);
  pinMode(BRAKE, OUTPUT);
}

//void brake() {
//  digitalWrite(BRAKE, HIGH);
//}

void BOTDir() {
  if (input == 'F') {          //move forward(all motors rotate in forward direction)
    digitalWrite(R_F, HIGH);
    digitalWrite(L_F, HIGH);
    digitalWrite(R_R, LOW);
    digitalWrite(L_R, LOW);
    digitalWrite(BRAKE, LOW);
    Serial.print("Forward");
  }
  if (input == 'B')
  { //move Rev(all motors rotate in back direction)
    digitalWrite(R_F, LOW);
    digitalWrite(L_F, LOW);
    digitalWrite(R_R, HIGH);
    digitalWrite(L_R, HIGH);
    digitalWrite(BRAKE, LOW);
    Serial.print("Reverse");
  }

  if (input == 'R')
  { //move RIGHT(all motors rotate in right direction)
    digitalWrite(R_F, LOW);
    digitalWrite(L_F, HIGH);
    digitalWrite(R_R, LOW);
    digitalWrite(L_R, LOW);
    digitalWrite(BRAKE, LOW);
    Serial.print("Right");
  }
  if (input == 'L')
  { //move left(all motors rotate in left direction)
    digitalWrite(R_F, HIGH);
    digitalWrite(L_F, LOW);
    digitalWrite(R_R, LOW);
    digitalWrite(L_R, LOW);
    digitalWrite(BRAKE, LOW);
    Serial.print("Left");
  }
  if (input == 'S')
  { //move Rev(all motors rotate in right direction)
    digitalWrite(R_F, LOW);
    digitalWrite(L_F, LOW);
    digitalWrite(R_R, LOW);
    digitalWrite(L_R, LOW);
    digitalWrite(BRAKE, HIGH);
    voltage = 0;
    Serial.print("Brake");
  }
  if (input == 'V')
  { //magnetised)
    digitalWrite(M_ON, HIGH);
  }

    if (input == 'v')
    { //move Rev(all motors rotate in right direction)
      digitalWrite(M_ON, LOW);
    }
    Serial.print(",");
}

void motorspeed()
{
  switch (input)
  {
    case '0': // off
      {
        voltage = 0;
      }
      break;

    case '1': // speed 1

      {
        voltage = 300;
      }
      break;

    case '2': // speed 2
      {
        voltage = 700;
      }
      break;

    case '3': // speed 3
      {
        voltage = 1200;
      }
      break;

    case '4': // speed 4
      {
        voltage = 1800;
      }
      break;

    case '5': // speed 5
      {
        voltage = 2400;
      }
      break;

    case '6': // speed 6

      {
        voltage = 3000;
      }
      break;

    case '7': // speed 7

      {
        voltage = 3600;
      }
      break;

    case '8': // speed 8
      {
        voltage = 4200;
      }
      break;

    case '9': // speed 8
      {
        voltage = 4800;
      }
      break;
  }
  Serial.println(voltage);
}

void DACvlt()
{
  dac.setVoltageA(voltage);
  dac.setVoltageB(voltage);
  dac.updateDAC();
}
