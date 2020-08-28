#!/bin/sh

cd /home/pi/Desktop/LightYourHearth-rpi/
git pull
sudo pip3 install -r requirements.txt
cd /home/pi/Desktop/LightYourHearth-rpi/RpiServer
sudo python3 main.py
