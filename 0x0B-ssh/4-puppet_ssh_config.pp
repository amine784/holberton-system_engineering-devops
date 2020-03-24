# ssh confifuration
exec { 'echo -e "Id_File ~/ssh/holberton\n" >> /etc/ssh/ssh_config':
provider => shell,
command  => 'echo -e "Pass_Auth no\n" >> /etc/ssh/ssh_config',
}