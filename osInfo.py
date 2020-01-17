import platform,socket

print('Platform : {}'.format(platform.system()))
print('Platform-Version : {}'.format(platform.platform()))
print('Platform-Release : {}'.format(platform.release()))
print('Architechture : {}'.format(platform.machine()))
print('Processor : {}'.format(platform.processor()))
print('Hostname : {}'.format(socket.gethostname()))
print('Ip-Address : {}'.format(socket.gethostbyname(socket.gethostname())))
