# the command line is manage the hiera config file 
# and deploy bigtop component on each node.
from sys import stderr, stdin, stdout
from paramiko import SSHClient, AutoAddPolicy
client = SSHClient()

client.load_host_keys('C:/Users/peng/.ssh/known_hosts')
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect('192.168.1.5', username='root')

stdin, stdout, stderr = client.exec_command('cat /etc/hosts')
while True:
    line = stdout.readline()
    if not line:
        break
    print(line, end="")
stdin.close()
stdout.close()
stderr.close()
client.close()