#!/usr/bin/env python

import urllib2, time, pygame.mixer
from bs4 import BeautifulSoup

url = "http://www.webhostingstatus.com/"
#url = "http://localhost:4000/"
beepsound = "beep.wav"
alertsound = "missile.wav"
reference_page = ""
current_page = ""
wait_time = 10 #seconds
sound = ""

def main():
    setup()
    print "Loaded..."
    
    while True:
        download_page()
        if not same_as_reference():
            if page_shows_warning():
                flash_and_stuff()
            save_as_reference()
        wait_a_bit()


def setup( ):
    #set up pins, mixer, whatevs.
    pygame.mixer.init()
    global sound
    sound = pygame.mixer.Sound(beepsound)
    sound.play()
    #replace with alert ready for use
    sound = pygame.mixer.Sound(alertsound)

def download_page():
    global current_page
    try:
        response = urllib2.urlopen(url)
        current_page = response.read()
    except Exception:
        print "ERR: Couldn't connect to ", url


def same_as_reference():
    if current_page == reference_page:
        return True
    else:
        if not reference_page == "":
            print "Page has been updated..."
            t = time.time()
            f = open("examples/" + str(t) + ".txt", 'w')
            f.write(current_page)
            f.close() 
        return False

def page_shows_warning():
    soup = BeautifulSoup(current_page)
    divs = soup.find_all("div", class_="contentbox")
    for div in divs:
        notifs = div.find_all("li")
        if notifs is None: #means there are no error items
            return False
        for item in notifs:
            fixed = item.find("p", class_="fixed")
            if fixed is not None: #means that all error items are fixed
                return True
    return False


def flash_and_stuff():
    print "Page has errors..."
    sound.play()


def save_as_reference():
    global reference_page
    reference_page = current_page

def wait_a_bit():
    time.sleep(wait_time)


if __name__ == "__main__":
    main()
