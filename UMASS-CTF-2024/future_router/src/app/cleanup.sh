#!/bin/sh
while :
do
    rm -rf $(find /tmp/* -mmin +2)
    sleep 15
done