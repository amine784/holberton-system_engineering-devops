# fix
exec { 'debug':
command => 'sed -i "s/15/50000/g" /etc/default/nginx | service nginx restart',
path    => ['/bin', '/usr/bin', '/usr/sbin']
}