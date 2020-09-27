#!/bin/bash
sudo cp ./beep.py /usr/local/bin
sudo cp ./beep /usr/local/bin
sudo chmod +x /usr/local/bin/beep
rm beep
rm beep.py
mkdir ~/midibeep
cd ./Raspberry-Pi-GPIO-MIDI-player
mv -v -t ~/midibeep *
sudo rm -r ~/Raspberry-Pi-GPIO-MIDI-player
rm ~/midibeep/setup.sh
echo "Installation completed."
