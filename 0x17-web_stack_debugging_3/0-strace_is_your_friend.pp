# fix bug
exec { 'fix_debug':
path     => ['/usr/bin/', '/bin/'],
provider => 'shell',
command  => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}