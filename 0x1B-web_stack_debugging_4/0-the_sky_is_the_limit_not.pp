# fix
exec { 'debug':
command => "sed -i "s/15/30000/g" /etc/default/nginx | service nginx restart",
path    => ['/bin', '/usr/bin', '/usr/sbin']
}