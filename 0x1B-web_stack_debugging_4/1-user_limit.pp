# debug
exec { 'debug':
path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command => 'echo -n  > /etc/security/limits.conf',
}