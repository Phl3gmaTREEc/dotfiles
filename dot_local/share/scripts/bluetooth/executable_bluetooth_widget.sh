#!/bin/env bash

bt_s=$(bluetoothctl show | rg "Powered:" | awk '{print $2}')
bt_i=$(bluetoothctl info | rg -i "Device" | awk '{print $1}')
bt_on=''
bt_off=''
bt_head=''
bt_err=''

if [ "$bt_s" == "no" ]
then
	echo $bt_off
elif [ "$bt_s" == "yes" ] && [ "$bt_i" == "Device" ]
then
	echo $bt_head
elif [ "$bt_s" == "yes" ] && [ "$bt_i" == "Missing" ]
then
	echo $bt_on
else
	echo $error
fi
