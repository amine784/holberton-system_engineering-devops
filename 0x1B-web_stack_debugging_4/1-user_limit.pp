# debug
exec { 'debug':
path    => ['/bin/', '/sbin/', '/usr/bin/'],
command => 'echo -n  > /etc/security/limits.conf',
}