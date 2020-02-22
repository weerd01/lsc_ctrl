# tlc (Tasmota Lightning Control) 

Intro:

A small python script to control your tasmota flashed LSC Smart Connect bulbs. I didn't find any satisfactory solution to integrate these bulbs within Domoticz. I also found using a MQTT broker for controlling a few bulbs a bit overkill. I just settle with a python 3 script along with some virtual buttons from within Domoticz.

Requirements:

pip3 install -U pyYAML (it DOESN'T work with the one supplied with raspbian distro. Upgrade it!)
pip3 install paho-mqtt

Status: 

Fairly usable! Although some things are missing, it's actually running in 'production' here :) Once you have setup your configuration file, this program can turn your lights on, off as well as setting colors, dim values and a few other tricks.  

Planned: 

lsc_ctrl currently supports tasmota web commands. I will add MQTT support shortly to improve speed.


Dennis/weerd01@gmail.com
-

