#!/bin/sh

# Start polkit agent from GNOME
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Start apps
dunst -conf "~/.config/dunst/dunstrc" &
easyeffects --gapplication-service &
solaar --window=hide &
qpwgraph -m &
nm-applet &
#blueman-applet &
steam -silent &
flameshot &
flatpak run org.ferdium.Ferdium &
corectrl --minimize-systray &
#discord --start-minimized &
#pasystray &
#/home/ptc/.local/share/applications/pCloud.AppImage &

# Xrandr script
~/.screenlayout/screen_layout_def.sh &

# Compositor
picom & # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Backgrounds
feh --bg-fill ~/Pictures/Wallpapers/arch3.jpg
