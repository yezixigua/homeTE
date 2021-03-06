
# 关闭服务
service supervisor stop
service nginx stop

# 删除原本建立的软连接
rm /etc/supervisor/conf.d/myHome.conf
rm /etc/nginx/sites-enabled/myHome

# 建立对应软件的配置软连接，将配置源文件放在项目本地，在对应软件目录下生成链接，链接到本地
ln -s /home/an/myHome/config/supervisor.conf /etc/supervisor/conf.d/myHome.conf
ln -s /home/an/myHome/config/nginx_config /etc/nginx/sites-enabled/myHome

# 重启服务
service supervisor restart
service nginx restart

