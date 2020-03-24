# ssh confifuration
exec { 'echo -e "IdentityFile ~/ssh/holberton" >> /etc/ssh/ssh_config':
provider => shell,
command  => 'echo -e "PasswordAuthentication no" >> /etc/ssh/ssh_config',
}