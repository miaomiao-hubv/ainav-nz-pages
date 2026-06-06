import paramiko
import os

host = '170.64.166.47'
user = 'root'
password = 'nLt9fCY@TWJgqKr'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=user, password=password, timeout=15)
print('SSH connected')

# Try common web root locations
candidates = [
    '/var/www/html',
    '/var/www',
    '/usr/share/nginx/html',
    '/srv/www/html',
    '/srv/http',
]

webroot = None
for d in candidates:
    stdin, stdout, stderr = ssh.exec_command('test -d %s && echo YES' % d, timeout=5)
    result = stdout.read().decode().strip()
    if result == 'YES':
        webroot = d
        print('Found web root: %s' % d)
        break

if not webroot:
    # Try to get from nginx config
    stdin, stdout, stderr = ssh.exec_command(
        'grep -r "root " /etc/nginx/sites-enabled/ 2>/dev/null | head -5', timeout=5
    )
    out = stdout.read().decode().strip()
    print('nginx config grep result: %s' % out)
    # Try apache
    stdin, stdout, stderr = ssh.exec_command(
        'grep -r "DocumentRoot" /etc/apache2/sites-enabled/ 2>/dev/null | head -5', timeout=5
    )
    out = stdout.read().decode().strip()
    print('apache config grep result: %s' % out)
    print('ERROR: could not detect web root automatically')
else:
    print('Web root is: %s' % webroot)
    # List what's already there
    stdin, stdout, stderr = ssh.exec_command('ls -la %s/' % webroot, timeout=5)
    print('Contents:')
    print(stdout.read().decode())

ssh.close()
print('Done')
