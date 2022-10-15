#!/bin/env bash

st_out=$(pamixer --get-default-sink | awk 'NR>1 {print $1}' | xargs -i pamixer --sink {} --get-mute)
volume=$(pamixer --get-volume-human)
muted='ﱝ'
error=''

if [ "$st_out" == "true" ]
then
	echo $muted
elif [ "$st_out" == "false" ]
then
	echo $volume
else
	echo $error
fi
