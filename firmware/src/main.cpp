#include <Arduino.h>

void setup()
{
    Serial.begin(115200);
    delay(1000);
    Serial.println();
    Serial.println("==============================");
    Serial.println(" ESP32-CAM Edge AI Project");
    Serial.println("==============================");
    Serial.println("Firmware started successfully!");
}

void loop()
{
    Serial.println("ESP32-CAM is running...");
    delay(1000);
}