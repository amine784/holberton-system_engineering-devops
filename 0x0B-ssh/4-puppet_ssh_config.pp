# ssh confifuration
exec { 'echo':
command  => 'echo "IdentityFile ~/.ssh/holberton " >>  /etc/ssh/ssh_config',
path     => '/bin/',
provider => 'shell',
}
exec { 'echo':
command  =>'echo "PasswordAuthentication no"  >>  /etc/ssh/ssh_config',
path     => '/bin/',
provider => 'shell',
}