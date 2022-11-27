#!/bin/env bash

# Options for powermenu
# lock="    Lock"
# logout="    Logout"
shutdown="    Shutdown"
reboot="    Reboot"
logout="    Logout"
# sleep="    Sleep"

# Get answer from user via rofi
selected_option=$(echo "$reboot
$shutdown
$logout" | rofi -dmenu\
                  -i\
                  -p "Power"\
                  -config "~/.config/rofi/smallmenu.rasi"\
		  -l 3\ )

# Do something based on selected option
# if [ "$selected_option" == "$lock" ]
# then
#     /home/$USER/.config/scripts/i3lock-fancy/i3lock-fancy.sh
# elif [ "$selected_option" == "$logout" ]
# then
#     loginctl terminate-user `whoami`
if [ "$selected_option" == "$shutdown" ]
then
    systemctl poweroff
elif [ "$selected_option" == "$reboot" ]
then
    systemctl reboot
 elif [ "$selected_option" == "$logout" ]
 then
    qtile cmd-obj -o cmd -f shutdown
else
    echo "No match"
fi
