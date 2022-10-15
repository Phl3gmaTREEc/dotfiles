#!/bin/env bash

mic_s=$(pamixer --list-sources | rg "Blue" | awk '{print $1}' | xargs -i pamixer --source {} --get-mute)
mic_volume_blue=$(pamixer --list-sources | rg "Blue" | awk '{print $1}' | xargs -i pamixer --source {} --set-volume 80)
mic_volume_ee=$(pamixer --list-sources | rg "EasyEffects Source" | awk '{print $1}' | xargs -i pamixer --source {} --set-volume 100)
mic_toggle=$(pamixer --list-sources | rg "Blue" | awk '{print $1}' | xargs -i pamixer --source {} -t)

if [ "$mic_s" == "true" ]
then
	echo $mic_toggle && $mic_volume_blue && $mic_volume_ee
elif [ "$mic_s" == "false" ]
then
	echo $mic_toggle
fi
