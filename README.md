# Raspberry-Pi-GPIO-MIDI-player
Plays .mid files on GPIO 18 on any Raspberry Pi or compatible SBCs
#
Installation:

Simply run the following commands in a terminal on your pi:
```
git clone https://github.com/FreddyFeuerstein/Raspberry-Pi-GPIO-MIDI-player.git
```
```
cd Raspberry-Pi-GPIO-MIDI-player
```
```
chmod +x setup.sh && ./setup.sh
```
#
Usage:

· For GUI users:
  Simply drag n' drop .mid files onto the Midi Buzzer! desktop entry file.

· For CLI users or for embedding in other projects:
  Run the following command (Replace "/Path/To/My-Midi-File.mid" with your real midi file path)
```
python "/home/pi/midibeep/midi-buzzer.py" "/Path/To/My-Midi-File.mid"
```
#
Other features:

· The 'beep' command (known from x86 Debian) will now work as expected on the Pi (if a speaker is hooked up to GPIO 18).

· For soundcard users, an ALSA-compatible player is included in this project. It will play midis with the 'ffplay' command.
