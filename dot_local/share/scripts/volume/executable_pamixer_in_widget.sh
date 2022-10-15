#!/bin/env bash

st_in=$(pamixer --list-sources | rg "Blue" | awk '{print $1}' | xargs -i pamixer --source {} --get-mute)
muted=''
unmuted=''
error=''

if [ "$st_in" == "true" ]
then
	echo $muted
elif [ "$st_in" == "false" ]
then
	echo $unmuted
else
	echo $error
fi
