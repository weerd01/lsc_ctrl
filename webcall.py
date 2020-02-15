#!/usr/bin/env python3

def call(call):

  if call == "spot_on":
    value = "/cm?cmnd=Power%20On" 

  elif call == "spot_off":
    value = "/cm?cmnd=Power%20Off"

  elif call == "dimmer":
    value = "/cm?cmnd=Dimmer%20"

  elif call == "color":
    value = "/cm?cmnd=Color%20"

  elif call == "color_temp":
    value = "/cm?cmnd=CT%20"

  elif call == "fade_on":
    value = "/cm?cmnd=Fade%201"

  elif call == "fade_off":
    value = "/cm?cmnd=Fade%200"

  elif call == "method":
    value = "http://"
 
  return value
