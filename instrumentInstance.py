import docker

class instrumentInstance:

    def __init__(self, name, port, dockerClient):
        self.name = name
        self.port = port
        self.dockerClient = dockerClient

    def startInstrument(self, type, *delay, **delayParameters):

        autoUpdating = True if type == 'auto' else False

        if autoUpdating & ('delay' in delayParameters):
            delay = delayParameters['delay']
        
        self.dockerClient.containers.run("ubuntu:latest", "sleep infinity", detach=True)



