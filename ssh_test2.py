import paramiko
import socket

host = '170.64.166.47'
user = 'root'
password = 'nLt9fCY@TWJgqKr'

print('Step 1: Testing TCP port 22...')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(8)
try:
    result = sock.connect_ex((host, 22))
    if result == 0:
        print('  Port 22 is OPEN')
        banner = sock.recv(1024)
        print('  SSH banner: %s' % banner)
    else:
        print('  Port 22 CLOSED (code: %d)' % result)
    sock.close()
except Exception as e:
    print('  TCP connect error: %s' % e)
    sock.close()

print()
print('Step 2: Trying SSH connect (10s timeout)...')
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password, timeout=10, banner_timeout=10, allow_agent=False, look_for_keys=False)
    print('  SSH SUCCESS!')
    stdin, stdout, stderr = ssh.exec_command('whoami && pwd && ls /var/www/html/ 2>/dev/null | head -20')
    print(stdout.read().decode())
    ssh.close()
except Exception as e:
    print('  SSH FAILED: %s' % e)
