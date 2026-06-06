import socket, paramiko

host = '170.64.166.47'
user = 'root'
password = 'nLt9fCY@TWJgqKr'

# Test if port 22 is open
print('Testing TCP connection to %s:22...' % host)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)
try:
    result = sock.connect_ex((host, 22))
    if result == 0:
        print('Port 22 is OPEN')
    else:
        print('Port 22 is CLOSED (error: %d)' % result)
    sock.close()
except Exception as e:
    print('Connection error: %s' % e)
    sock.close()

# Try SSH with short timeout
print('\nTrying SSH connection (5s timeout)...')
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password, timeout=5, banner_timeout=5)
    print('SSH connection SUCCESS')
    stdin, stdout, stderr = ssh.exec_command('echo OK && whoami && pwd')
    print(stdout.read().decode())
    ssh.close()
except Exception as e:
    print('SSH connection FAILED: %s' % e)
