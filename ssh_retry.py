import paramiko
import time

host = '170.64.166.47'
user = 'root'
password = '0'

print('尝试 SSH 连接（新密码）...')
start = time.time()
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        host,
        username=user,
        password=password,
        timeout=15,
        banner_timeout=15,
        auth_timeout=15,
        allow_agent=False,
        look_for_keys=False
    )
    print('✅ SSH 连接成功！耗时: %.1f秒' % (time.time() - start))
    
    stdin, stdout, stderr = ssh.exec_command('echo "用户: $(whoami)" && echo "当前目录: $(pwd)" && ls /var/www/html/ 2>/dev/null | head -10')
    print(stdout.read().decode())
    
    # 找 web 目录
    stdin, stdout, stderr = ssh.exec_command('cat /etc/nginx/sites-enabled/* 2>/dev/null | grep -E "root|server_name" | head -10')
    nginx_conf = stdout.read().decode().strip()
    if nginx_conf:
        print('Nginx 配置:\n%s' % nginx_conf)
    
    ssh.close()
    print('\n✅ 连接正常，可以上传！')
except Exception as e:
    print('❌ 失败: %s' % e)
    print('耗时: %.1f秒' % (time.time() - start))
