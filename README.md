# TGNBInstrumentSim

*Latest Update: 17 July 2019*


Container-based software that easily allows mock Tangen instrument instances to be simulated
on your pc. Originally built for testing the Tangen Data Portal, but can be used for any use where
an instrument is required as it simulates API requests exactly like the physical hardware.

## Installation
~~~~
git clone https://github.com/griffinpuc/TGNBInstrumentSim.git
~~~~

## Dependencies
##### Docker Toolbox (Windows Home Edition Systems)  
[Download Docker Toolbox Here](https://docs.docker.com/toolbox/toolbox_install_windows/)

##### Docker Desktop (Windows Pro & Enterprise Systems)
[Download Docker Desktop Here](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

##### Docopt
~~~~
pip install docopt
~~~~
##### Docker
~~~~
pip install docker
~~~~

***

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
  -n --nuke     Crash all mock instrument containers.
~~~~

## Pushing a Custom Results, Raw, or Log File

~~~~
mtisim.py push <filepath> to <name>
~~~~

Replace <filepath> with the path to your Results.JSON or RawData.JSON and the file will be added to
the instrument instance's **/tdx/getResults** call, queing it to be sent out.
