# changes SSH config file

echo {'echo':
    command => 'echo" IdentityFile ~/.ssh/school\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
    path    => 'usr/bin:/bin',
    returns => 0,     
}
