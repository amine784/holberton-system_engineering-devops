#install inginx and confg
exec {'up':
provider => shell,
path     => '/usr/sbin',
command  => 'sudo apt-get -y update ',
}
exec {'config new serv':
provider => shell,
command  => '"Holberton School" | sudo tee /var/www/html/index.nginx-debian.html',
}
exec {'restart':
provider => shell,
command  => '/usr/sbin/service nginx restart',
}