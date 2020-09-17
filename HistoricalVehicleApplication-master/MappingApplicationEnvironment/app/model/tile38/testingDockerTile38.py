import docker
client = docker.from_env()
print(client.images.list())
##client.images.pull('tile38/tile38')
#container = client.containers.run('tile38/tile38',detach=True, ports={'9851/tcp': 9851})
#print(container)
#print(container.logs())
#container.stop()
#for line in container.logs(stream=True):
#	print( line.strip())
