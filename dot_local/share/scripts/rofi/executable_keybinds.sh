#!/bin/env bash

# Options for powermenu
qtile="qtile"
zathura="zathura"

# Get answer from user via rofi
selected_option=$(echo "$qtile
$zathura" | rofi -dmenu\
                  -i\
                  -p "Cheat"\
                  -config "~/.config/rofi/smallmenu.rasi"\
		  -l 2\ )

# Do something based on selected option
if [ "$selected_option" == "$qtile" ]
then
    /home/ptc/.local/share/scripts/keybinds_cheat/qtile_keybinds.sh
elif [ "$selected_option" == "$zathura" ]
then
    /home/ptc/.local/share/scripts/keybinds_cheat/zathura_keybinds.sh
else
    echo "No match"
fi
