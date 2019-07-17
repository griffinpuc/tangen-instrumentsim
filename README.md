# TGNBInstrumentSim

*Latest Update: 17 July 2019*


Container-based software that easily allows mock Tangen instrument instances to be simulated
on your pc. Originally built for testing the Tangen Data Portal, but can be used for any use where
an instrument is required as it simulates API requests exactly like the physical hardware.

## Installation
~~~~
git clone https://github.com/griffinpuc/TGNBInstrumentSim.git
~~~~

## Usage Guide

~~~~
Usage:
  mtisim.py launch <name> on <port>
  mtisim.py crash <name>
  mtisim.py (-n | --nuke)
  mtisim.py push <filepath> to <name>
  mtisim.py add <delay> delay to <name>
  mtisim.py remove delay from <name>

Options:
  -h --help     Show this screen.
  -b --build    Build latest mock instrument container.
  -n --nuke     Crash all mock instrument containers.
~~~~
