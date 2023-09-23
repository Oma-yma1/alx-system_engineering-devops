#!/usr/bin/env bash
#Client configuration file (w/ Puppet) ssh
file_line { 'Turn off passwd auth':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'IdentifyFile ~/.ssh/school',
}
