#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ainav.nz 上传脚本
在本地 Windows / Mac / Linux 上运行，通过 SFTP 上传到服务器

使用前修改以下变量：
  REMOTE_DIR  = 服务器上网站根目录（如 /var/www/html/ainav 或 /var/www/html）
"""

import paramiko
import os

# ========== 修改这里 ==========
HOST     = '170.64.166.47'
USER     = 'root'
PASSWORD = 'nLt9fCY@TWJgqKr'
REMOTE_DIR = '/var/www/html/ainav'   # ← 改成你服务器上的实际路径
LOCAL_DIR = r'D:\ainav-nz-pages'   # ← 本地项目目录（一般不用改）
# =================================

def upload_dir(sftp, local_path, remote_path):
    """递归上传整个目录"""
    try:
        sftp.mkdir(remote_path)
        print('  [DIR] 创建目录: %s' % remote_path)
    except Exception:
        pass  # 目录已存在

    for item in os.listdir(local_path):
        local_item = os.path.join(local_path, item)
        remote_item = remote_path + '/' + item
        if os.path.isdir(local_item):
            upload_dir(sftp, local_item, remote_item)
        else:
            sftp.put(local_item, remote_item)
            print('  [PUT] %s' % remote_item)

def main():
    print('连接到 %s ...' % HOST)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(HOST, username=USER, password=PASSWORD, timeout=15, banner_timeout=15)
    print('SSH 连接成功！')

    sftp = ssh.open_sftp()
    print('SFTP 已打开')
    print('远程目录: %s' % REMOTE_DIR)
    print('本地目录: %s' % LOCAL_DIR)
    print('-' * 40)

    # 先确保远程目录存在
    try:
        sftp.stat(REMOTE_DIR)
        print('远程目录已存在: %s' % REMOTE_DIR)
    except Exception:
        print('远程目录不存在，尝试创建...')
        sftp.mkdir(REMOTE_DIR)

    # 上传所有文件（排除 .py 脚本和 .git）
    skip_ext = ('.py', '.pyc')
    skip_dirs = ('.git', 'node_modules', '__pycache__')

    for item in os.listdir(LOCAL_DIR):
        if item.startswith('.'):
            continue
        if item.endswith(skip_ext):
            print('  [SKIP] %s' % item)
            continue
        local_item = os.path.join(LOCAL_DIR, item)
        remote_item = REMOTE_DIR + '/' + item
        if os.path.isdir(local_item):
            if item in skip_dirs:
                print('  [SKIP] %s/' % item)
                continue
            upload_dir(sftp, local_item, remote_item)
        else:
            sftp.put(local_item, remote_item)
            print('  [PUT] %s' % remote_item)

    print('-' * 40)
    print('上传完成！')

    # 验证：列出远程目录
    print('\n远程目录内容:')
    stdin, stdout, stderr = ssh.exec_command('ls -lh %s/' % REMOTE_DIR)
    print(stdout.read().decode())

    sftp.close()
    ssh.close()

if __name__ == '__main__':
    main()
