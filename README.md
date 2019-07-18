# TGNBInstrumentSim

*Latest Update: 17 July 2019*

**Currently in progress, expect working ~ 14 days**

Container-based software that easily allows mock Tangen instrument instances to be simulated
on your pc. Originally built for testing the Tangen Data Portal, but can be used for any use where
an instrument is required as it simulates API requests exactly like the physical hardware.

&nbsp;

## Installation
~~~~
git clone https://github.com/griffinpuc/TGNBInstrumentSim.git
cd TGNBInstrumenSim
python mtisim.py --update
~~~~ 

&nbsp;

## Dependencies

### Auto Updates & Dependency Satisfaction
~~~~
python mtisim.py --update
~~~~
Running this will automatically fetch updated code and satisfy dependencies if PIP is installed. The
only dependency this will **NOT** satisfy is Docker Toolbox.

&nbsp;

### Docker Requirements

#### Docker Toolbox (Windows Home Edition Systems)  
[Download Docker Toolbox Here](https://docs.docker.com/toolbox/toolbox_install_windows/)

#### Docker Desktop (Windows Pro & Enterprise Systems)
[Download Docker Desktop Here](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

&nbsp;

### PIP Requirements

#### Docopt
~~~~
pip install docopt
~~~~
#### Docker
~~~~
pip install docker
~~~~
#### Flask
~~~~
pip install Flask
~~~~

<br/><br/>
## Usage Guide
~~~~
Usage:
  mtisim.py launch <name> on <port>
  mtisim.py crash <name>
  mtisim.py (-n | --nuke)
  mtisim.py push <filepath> to <name>
  mtisim.py add <delay> delay to <name>
  mtisim.py remove delay from <name>
  mtisim.py --update

Options:
  -h --help     Show this screen.
  -n --nuke     Crash all mock instrument containers.
  --update      Automatically update code and satisfy pip dependencies.
~~~~
&nbsp;

## Launching an Instrument Instance

~~~~
mtisim.py launch <name> to <port>
~~~~

Replace **\<name>** with whatever you would like to call this instance, and **\<port>** with the dedicated
port for this instance. If you are launching multiple instances, multiple ports must be used as they
are all running from one piece of hardware.

&nbsp;

## Crashing an Instrument Instance

~~~~
mtisim.py crash <name>
~~~~

Have no need for an instance anymore? Replace **\<name>** with the instance name to make it disappear forever.

&nbsp;

## Pushing a Custom Results, Raw, or Log File

~~~~
mtisim.py push <filepath> to <name>
~~~~

Replace **\<filepath>** with the path to your Results.JSON or RawData.JSON and the file will be added to
the instrument instance's **/tdx/getResults** queue, queing it to be sent out.

&nbsp;

## Adding Delayed Rolling Results

~~~~
mtisim.py add <delay> delay to <name>
~~~~

Adding delayed rolling results is useful if you'd like to automate the process of having new results
pop up regularly. Simply replace **\<delay>** with seconds (Eg. '10' for a ten second delay), and every
**x** seconds a new set of results will be added to the queue. To remove this delay, crash the instance.

&nbsp;
&nbsp;

Copyright &copy; Tangen Biosciences 2019
