#!/usr/bin/bash

cp ./alacritty.toml /home/$USER/.alacritty.toml
[ ! -d /home/$USER/.config/rofi ] && mkdir -p /home/$USER/.config/rofi
cp ./rofidmenu.rasi /home/$USER/.config/rofi/rofidmenu.rasi
cp ./config.rasi /home/$USER/.config/rofi/config.rasi
cp ./config.kdl /home/$USER/.config/niri/config.kdl
