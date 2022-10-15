#!/bin/env bash

# Options for powermenu
rsn="Night"
rsd="Day"
calc="Calculator"
layout="Layout rep"

# Get answer from user via rofi
selected_option=$(echo "$rsn
$rsd
$layout
$calc" | rofi -dmenu\
                  -i\
                  -p "Menu"\
                  -config "~/.config/rofi/smallmenu.rasi"\
		  -l 4\ )

# Do something based on selected option
# if [ "$selected_option" == "$lock" ]
# then
#     /home/$USER/.config/scripts/i3lock-fancy/i3lock-fancy.sh
# elif [ "$selected_option" == "$logout" ]
# then
#     loginctl terminate-user `whoami`
if [ "$selected_option" == "$rsn" ]
then
    redshift -P -O 4500 -b 0.8
elif [ "$selected_option" == "$rsd" ]
then
    redshift -x
elif [ "$selected_option" == "$calc" ]
then
    rofi -show calc -modi calc -no-show-match -no-sort
elif [ "$selected_option" == "$layout" ]
then
    ~/.local/share/scripts/screen/layout_reapir.sh
else
    echo "No match"
fi
