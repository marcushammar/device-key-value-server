Device Key Value
================
This application runs on Google App Engine. It will give you access to a
key-value database that you can use from any IOT device that can support HTTP.
Values can be saved by one IOT device and read by another IOT device. The
purpose is to use a common database for your IOT devices.

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

To save a key-value pair, request the following address from your IOT device:
http://APPLICATION.appspot.com/?device=DEVICE&key=KEY&value=VALUE

To read a value based on a key, request the following address from your IOT
device:
http://APPLICATION.appspot.com/?device=DEVICE&key=KEY
