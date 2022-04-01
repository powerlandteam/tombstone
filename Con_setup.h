#ifndef Con_setup.h
#define Con_setup.h
#include <Arduino.h>
#include <MCP48xx.h>

#define CS 5
#define R_F 26
#define L_F 25
#define R_R 12
#define L_R 13
#define BRAKE 14
#define M_ON 26


void setAllNeutral();
void setDirPinsAsOutput();
void initPins();
void brake();
void BOTDir();
void DACvlt();
void motorspeed();
void BTinit();
#endif
