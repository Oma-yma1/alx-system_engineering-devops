#let’s fix our stack so that we get to 0 failed

exec { 'change nginx limit':
    command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
    provider => shell,
}
