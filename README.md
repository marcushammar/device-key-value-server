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

To delete a device, request the following address using your web browser:
https://APPLICATION.appspot.com/delete/?device=DEVICE

To save a key-value pair, request the following address from your IOT device:
https://APPLICATION.appspot.com/?device=DEVICE&key=KEY&value=VALUE

To read a value based on a key, request the following address from your IOT
device:
https://APPLICATION.appspot.com/?device=DEVICE&key=KEY


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
