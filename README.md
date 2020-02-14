# lsc_ctrl

Intro:

A small python script to control your tasmota flashed LSC Smart Connect bulbs. I didn't find any satisfactory solution to integrate these bulbs within Domoticz. I also found using a MQTT broker for controlling a few bulbs a bit overkill. I just settle with a python 3 script along with some virtual buttons from within Domoticz.

Requirements:

pip3 install -U pyYAML (it DOESN'T work with the one supplied with raspbian distro. Upgrade it!)
pip3 install paho-mqtt

Status: 

very experimental. I am currently converting simple WEB requests you can send to tasmota to python 3 code/functions. It's not usable code at this moment! Once the script does something useful, i will update the status. Since i am testing/refactoring a lot, i suggest you don't waste time on this script .. yet (!) :)

Planned: 

lsc_ctrl currently supports tasmota web commands. I will add MQTT support shortly to improve speed.


Dennis/weerd01@gmail.com

