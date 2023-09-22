#create a manifest that kills process named killmenow
exec { 'pkill':
command => 'pkill killmenow',
path    => '/usr/bin',
}
