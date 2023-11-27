# Puppet manifest to make changes to your configuration file

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "# SSH client configuration\n
    Host *\n
      IdentityFile ~/.ssh/school\n
      PasswordAuthentication no\n
  ",
}
