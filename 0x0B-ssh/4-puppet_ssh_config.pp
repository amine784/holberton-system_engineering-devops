# ssh confifuration
exec { 'echo -e "Id_File ~/ssh/holberton\n" >> /etc/ssh/ssh_config':
provider => shell,
path     => '/etc/ssh/ssh_config',
command  => 'echo -e "Pass_Auth no\n" >> /etc/ssh/ssh_config',
}