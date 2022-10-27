#! /bin/bash

sudo pacman -Syu
# System
sudo pacman -S firewalld --noconfirm --needed
sudo systemctl enable --now firewalld.service
sudo pacman -S polkit-gnome --noconfirm --needed
sudo pacman -S bluez --noconfirm --needed
sudo pacman -S bluez-utils --noconfirm --needed
sudo pacman -S blueman --noconfirm --needed
sudo systemctl enable --now bluetooth
sudo pacman -S network-manager-applet --noconfirm --needed

# Terminal utils and replacement
sudo pacman -S bat --noconfirm --needed
sudo pacman -S bottom --noconfirm --needed
sudo pacman -S broot --noconfirm --needed
sudo pacman -S fd --noconfirm --needed
sudo pacman -S fzf --noconfirm --needed
sudo pacman -S kitty --noconfirm --needed
sudo pacman -S kitty-shell-integration --noconfirm --needed
sudo pacman -S kitty-terminfo --noconfirm --needed
sudo pacman -S lf --noconfirm --needed
sudo pacman -S lsd --noconfirm --needed
sudo pacman -S neovim --noconfirm --needed
sudo pacman -S pamixer --noconfirm --needed
sudo pacman -S ripgrep --noconfirm --needed
sudo pacman -S starship --noconfirm --needed
sudo pacman -S zoxide --noconfirm --needed
sudo pacman -S zsh --noconfirm --needed
sudo pacman -S zsh-autocompletions --noconfirm --needed
sudo pacman -S zsh-autosuggestions --noconfirm --needed
sudo pacman -S zsh-syntax-highlighzing --noconfirm --needed

# GUI
sudo pacman -S easyeffects --noconfirm --needed
sudo pacman -S corectrl --noconfirm --needed
sudo pacman -S dunst --noconfirm --needed
sudo pacman -S filezilla --noconfirm --needed
sudo pacman -S flameshot --noconfirm --needed
sudo pacman -S font-manager --noconfirm --needed
sudo pacman -S gimp --noconfirm --needed
sudo pacman -S mpv --noconfirm --needed
sudo pacman -S pacseek --noconfirm --needed
sudo pacman -S lapce --noconfirm --needed
sudo pacman -S qpwgraph --noconfirm --needed
sudo pacman -S rofi --noconfirm --needed
sudo pacman -S rofi-calc --noconfirm --needed
sudo pacman -S solaar --noconfirm --needed
sudo pacman -S redshift --noconfirm --needed
sudo pacman -S transmisson-gtk --noconfirm --needed
sudo pacman -S zathura --noconfirm --needed
sudo pacman -S zathura-pdf-poppler --noconfirm --needed
