# ssh confifuration
exec { 'echo -e "Pass_dAuth no\n Id_File ~/.ssh/holberton" >> /etc/ssh/ssh_config':
path => '/bin/',
}