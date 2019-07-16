import docker

try:
    client = docker.from_env()
    client.images.build(path="./", tag={image_tag})
except:
    print("No docker environment found. Please install and configure Docker toolbox > https://docs.docker.com/toolbox/toolbox_install_windows/.")

