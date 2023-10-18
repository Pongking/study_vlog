#!/bin/bash
#check target file
if [-t ./tmp/userinfo.txt]
then
    rm -f ./tmp/userinfo.txt
fi
mkdir tmp
# if ! which mkpasswd
# then
#     sudo apt-get install -y expect
# fi

for i in `seq -w 1 10` #-w weight
do
    # p=`mkpasswd -l 15 -s 0`
    p=$(openssl rand -base64 12)
    # useradd user_${i} && echo "${p}"| chpasswd --stdin user_${i} # | connect the previous and the next
    username="user_${i}"
    useradd $username
    echo "$username:$p" | chpasswd
    echo "$username $p" >> ./tmp/userinfo.txt
done