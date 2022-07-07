#!/bin/bash

ip=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | grep 192.168 | cut -d\  -f2)
sed -E -i '' "s/192.168.[0-9][0-9]?[0-9]?.[0-9][0-9]?[0-9]?/$ip/g" contentplayer-mobile/.env
echo "👻 Updated ip address on env file : $ip"

