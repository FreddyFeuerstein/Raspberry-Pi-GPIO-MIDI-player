#!/bin/bash
sudo cp ./beep.py /usr/local/bin
sudo cp ./beep /usr/local/bin
sudo chmod +x /usr/local/bin/beep
rm beep
rm beep.py
cd ~
mkdir midibeep
cd "./Raspberry-Pi-GPIO-MIDI-player"
mv -v ./ "../midibeep"
cd ..
# If you get an error here, ignore it.
rm -r Raspberry-Pi-GPIO-MIDI-player
cd ~/midibeep
echo "Installation completed."
