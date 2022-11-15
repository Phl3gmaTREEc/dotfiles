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
flatpak run com.logseq.Logseq &
#discord --start-minimized &
#pasystray &
#/home/ptc/.local/share/applications/pCloud.AppImage &

# Backgrounds
feh --bg-fill ~/Pictures/Wallpapers/arch3.jpg
