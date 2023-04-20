#/bin/sh

#curl $1 -s | grep -Po '(?<=href=")[^"]*'

curl -s $1 | grep http | cut -d '"' -f2

exit
