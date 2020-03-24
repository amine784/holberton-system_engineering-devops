# ssh confifuration
exec { 'echo "IdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config':
provider => 'shell',
command  => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config'
}