Device Key Value Server
=======================
This application runs on Google App Engine. It will give you access to a
key-value database that you can use from any IOT device that can support HTTPS
or HTTP. Values can be saved by one IOT device and read by another IOT device.
The purpose is to use a common database for your IOT devices.


Installation
------------
* Create an application on Google App Engine.
* Change the application field on the first row in the file "app.yaml"
* Upload the files to your application on Google App Engine.


Usage
-----
To use the application, replace the values below written in uppercase letters
with your values.

To add a device, request the following address using your web browser:
https://APPLICATION.appspot.com/add/?device=DEVICE

To delete a device, request the following address using your web browser:
https://APPLICATION.appspot.com/delete/?device=DEVICE

To save a key-value pair, request the following address from your IOT device:
https://APPLICATION.appspot.com/?device=DEVICE&key=KEY&value=VALUE

To read a value based on a key, request the following address from your IOT
device:
https://APPLICATION.appspot.com/?device=DEVICE&key=KEY


Sample client for Arduino
--------------------------
Here is a simple program for Arduino that will access the database using HTTP.
Replace appEngineApplication, wifiSsid and wifiPassword with your own values to
try it out. Before you can run below client code you need to deploy the main
application to Google App Engine.

```
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

String appEngineApplication = "YOUR_APPLICATION";
String wifiSsid = "YOUR_WIFI_SSID";
String wifiPassword = "YOUR_WIFI_PASSWORD";

void setup() {
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);
  WiFi.begin(wifiSsid.c_str(), wifiPassword.c_str());
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
}

void loop() {
  setString("device-01", "test", "it_works");
  String response = getString("device-01", "test");
  Serial.println("Value from the server was: " + response);
}

void setString(String device, String key, String value) {
  HTTPClient httpClient;
  httpClient.begin(String("http://") + appEngineApplication + ".appspot.com/?device=" + device + "&key=" + key + "&value=" + value);
  httpClient.GET();
  httpClient.end();
}

String getString(String device, String key) {
  HTTPClient httpClient;
  httpClient.begin(String("http://") + appEngineApplication + ".appspot.com/?device=" + device + "&key=" + key);
  String response;
  if (httpClient.GET() == HTTP_CODE_OK) {
    response = httpClient.getString();
  }
  httpClient.end();
  return response;
}
```


Security
--------
To add or delete devices you must use HTTPS. HTTPS is also highly recommended
when saving or reading a key-value pair but it is possible to use HTTP as well.


License
-------
Copyright 2018 Marcus Hammar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
