#!/bin/bash
sudo cp ./beep.py /usr/local/bin
sudo cp ./beep /usr/local/bin
sudo chmod +x /usr/local/bin/beep
rm beep
rm beep.py
cd ~
mkdir midibeep
cd ./Raspberry-Pi-GPIO-MIDI-player
mv -v -t ../midibeep *
cd ..
sudo rm -r ./Raspberry-Pi-GPIO-MIDI-player
cd /home/pi/midibeep
echo "Installation completed."
