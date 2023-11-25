# killing process using killmenow

exec { 'pkill killmenow':
  path => '/usr/bin'
}
