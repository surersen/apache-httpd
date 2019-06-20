#!/bin/bash

echo -e 'Content-Type: text/html\n'

echo '<h1>I am using cgi (shell script)</h1>'
echo '<form action="" method="GET">'
echo '<input type="text" name="cmd" autofocus />'
echo '<input type="submit" />'
echo '</form>'

exit 0
