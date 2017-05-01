#include <Arduino.h>
#include <SPI.h>
#include <Ethernet.h>
#include <RestClient.h>

#define OUT 3

RestClient client = RestClient("46.101.238.27", 8000);

void setup() {
  pinMode(OUT, OUTPUT);

  Serial.begin(9600);

  client.dhcp();

  delay(1000);

  analogWrite(OUT, 0);
}

String response;
void loop(){
  response = "";
  int statusCode = client.get("/out", &response);
  Serial.print("Status code from server: ");
  Serial.println(statusCode);
  Serial.print("Response body from server: ");
  Serial.println(response);
  analogWrite(OUT, min(response.toInt(),255));
  delay(5000);
}