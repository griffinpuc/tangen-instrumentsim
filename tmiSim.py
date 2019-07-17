"""Mock Tangen Instrument Sim Usage

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

"""
#Dependencies
from docopt import docopt
import docker
import sys
import os

client = docker.from_env()

#Build an image for Docker containers to use
def buildImage():
    try:

        #Critical variables
        client = docker.from_env()
        currentDir = os.getcwd()
        buildPath = os.path.join(currentDir, 'unbuilt_resources')

        #Build Docker image from source
        client.images.build(path=buildPath, tag='mtisim_image')

        #Successfully built image!
        print("Successfully built container image!")
        return client

    except Exception:

        #Will throw exception if Docker is configured incorrectly
        print("Broken or missing docker environment. Check configuration or install and configure Docker toolbox > https://docs.docker.com/toolbox/toolbox_install_windows/.")
        sys.exit()


#Launch a new instrument
def launchInstrument(name, port, client):
    try:
        client.containers.run('mtisim_image', name=('TMIS_'+name), detach=True)
        throwMessage('success', (("Launched instrument {0} to port {1}").format(name, port)))
    except:
        print('Found a Docker container with this name already...')


def crashInstrument(name):
    for container in client.containers.list():
        if(container.name == 'TMIS_'+name):
            container.remove(force = True)
            throwMessage('success', 'Successfully removed container ' + container.name)


#Message handeling
def throwMessage(type, message):
    print(('ERROR: {0}').format(message) if type == 'error' else ('SUCCESS: {0}').format(message))


#Main argument handler
if __name__ == '__main__':
    arguments = docopt(__doc__, version='MTISIM 0.0.2')


if((arguments['launch'] == True)):
    instanceName = arguments['<name>']
    instancePort = arguments['<port>']
    launchInstrument(instanceName, instancePort, buildImage())

if((arguments['crash'] == True)):
    instanceName = arguments['<name>']
    crashInstrument(instanceName)

