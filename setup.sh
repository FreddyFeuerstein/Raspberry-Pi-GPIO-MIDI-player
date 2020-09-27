#!/bin/bash
sudo cp ./beep.py /usr/local/bin
sudo cp ./beep /usr/local/bin
sudo chmod +x /usr/local/bin/beep
rm beep
rm beep.py
mkdir ~/midibeep
mv -r . ~/midibeep
cd ..
# If you get an error here, ignore it.
rm Raspberry-Pi-GPIO-MIDI-player
cd ~/midibeep
echo "Installation completed."
