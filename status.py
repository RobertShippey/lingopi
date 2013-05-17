#!/usr/bin/env python

import urllib2, time, pygame.mixer
import xml.etree.ElementTree as et

url = "http://www.webhostingstatus.com/"
beepsound = "beep.wav"
#url = "http://localhost:4000/"
reference_page = ""
current_page = ""
wait_time = 10 #seconds
sound = ""

def main():
    setup()
    
    while True:
        download_page()
        if not same_as_reference():
            if page_shows_warning():
                flash_and_stuff()
            save_as_reference()
        wait_a_bit()


def setup( ):
    # set up pins, mixer, whatevs.
    pygame.mixer.init()
    global sound
    sound = pygame.mixer.Sound(beepsound)
    print "starting"
 
def download_page():
    global current_page
    try:
        response = urllib2.urlopen(url)
        current_page = response.read()
        print "downloading..."
    except Exception:
        print "no internet"

 
def same_as_reference():
    return current_page == reference_page
 
def page_shows_warning():
    # XML parse some shit
    #root = et.fromstring(html)

    #for e in root.findall(".//h2"):
    #    break
    print "page analysed"
    if reference_page == "":
        return False
    return True
 
def flash_and_stuff():
    print "something has been reported"
    sound.play()
    # play sound
    # flash lights
 
def save_as_reference():
    global reference_page
    reference_page = current_page
    print "update ref"
 
def wait_a_bit():
    time.sleep(wait_time)


if __name__ == "__main__":
    main()
