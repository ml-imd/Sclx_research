#!/bin/sh

cat /etc/passwd | grep "$1" > /dev/null
echo $1
if [[ $? -ne 0 ]]
then
  adduser -D $1
  addgroup $1 $1
fi
cd /app
python3 run.py $2 $3
chown $1:$1 *.csv
rm -r __pycache__
exit 0
