# This manuscript increases the amount of traffic an Nginx server can handle

# Increase the ULIMIT of the default file
file { 'fix-for-nginx':
  ensure  => 'file',
  path    => '/etc/default/nginx',
  content => inline_template('<%= File.read("/etc/default/nginx").gsub(/ULIMIT=-n 15/, "ULIMIT=-n 4096") %>'),
}

# Restart Nginx
exec { 'nginx-restart':
  command     => '/etc/init.d/nginx restart', # or 'service nginx restart'
  path        => '/etc/init.d/',
  refreshonly => true,
  subscribe   => File['fix-for-nginx'],
}
