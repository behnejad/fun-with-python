import urllib2
import json
#from RPi.GPIO import *
#from sys import *

def main():


  #  setmode(GPIO.BCM)
   # cleanup()
   # setwarnings(False)
   # setup(17,GPIO.OUT)
    while True:
        response = urllib2.urlopen("http://api.thingspeak.com/channels/52939/feed.json?key=IUOGMX8FC3H2BH0W")
        html = response.read()

        data_string = json.loads(html)
        print data_string

        #print type(data_string["feeds"][::-1]['field 1'])
        status = data_string['feeds'][::-1][0]['field1']



        if status == '100':
            print "light is becoming on"
            light_on()

        elif status == '0':
            print "light is becoming off"
            light_off()

        else:
            print "light changed to " + status
            light_density(status)

def light_on():
#    output(17,LOW)
    print "light is now on"

def light_off():
#    output(17,HIGH)
    print "light is now off"

def light_density(density):
#    led=PWM(17,100)
 #   led.start(0)
 #   led.ChangeDutyCycle(density)
    try:
        while 1:
            pass
    except KeyboardInterrupt:
    #    cleanup()
        exit(1)
    print "light is changed as you wish :)" + density


main()
