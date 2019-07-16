import docker

try:
    client = docker.from_env()
    client.containers.list()
except:
    print("obviously failed")