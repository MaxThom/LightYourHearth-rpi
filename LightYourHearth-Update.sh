#!/bin/sh
set -x #echo on

count = 0
while ! ping -c 1 -W 1 github.com; do
    if ($count -le 20)
    then
	break
    fi
    count=$(( $count + 1 ))
    echo "Waiting for network interface ..."
    sleep 3
done

cd /home/pi/Desktop/LightYourHearth-rpi/
sudo git fetch

UPSTREAM=${1:-'@{u}'}
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")
BASE=$(git merge-base @ "$UPSTREAM")

if [ $LOCAL = $REMOTE ]; then
    echo "Up-to-date"
elif [ $LOCAL = $BASE ]; then
    echo "Need to pull"
    sudo git pull
    sudo pip3 install -r requirements.txt
    sudo reboot
elif [ $REMOTE = $BASE ]; then
    echo "Need to push"
else
    echo "Diverged"
fi