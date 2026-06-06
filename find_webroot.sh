import os

# 在FinalShell终端里跑这些命令

commands = """
# ===== 找到Web根目录 =====
echo "=== 1. 检查常见web目录 ==="
ls -la /var/www/html/ 2>/dev/null | head -5 || echo "没有 /var/www/html"
ls -la /usr/share/nginx/html/ 2>/dev/null | head -5 || echo "没有 /usr/share/nginx/html"
ls -la /srv/www/html/ 2>/dev/null | head -5 || echo "没有 /srv/www/html"

echo ""
echo "=== 2. 检查nginx配置 ==="
cat /etc/nginx/sites-enabled/* 2>/dev/null | grep -E "root |server_name" | head -10 || echo "nginx配置没找到"

echo ""
echo "=== 3. 检查Apache配置 ==="
cat /etc/apache2/sites-enabled/* 2>/dev/null | grep -E "DocumentRoot|ServerName" | head -10 || echo "apache配置没找到"

echo ""
echo "=== 4. 检查Caddy配置 ==="
find /etc /root /usr/local /opt -name "Caddyfile" -o -name "*.caddy" 2>/dev/null | head -5
cat /etc/caddy/Caddyfile 2>/dev/null | grep -E "root |file_server" | head -10 || echo "caddy配置没找到"

echo ""
echo "=== 5. 检查当前运行了哪些web服务器 ==="
netstat -tlnp 2>/dev/null | grep -E ":80|:443" || ss -tlnp 2>/dev/null | grep -E ":80|:443" || echo "无法查看端口"
"""

print(commands)
