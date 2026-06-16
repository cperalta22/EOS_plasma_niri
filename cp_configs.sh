#!/usr/bin/bash

[ ! -d /home/$USER/.config/rofi ] && mkdir -p /home/$USER/.config/rofi ]
cp ./rofidmenu.rasi /home/$USER/.config/rofi/rofidmenu.rasi
cp ./config.rasi /home/$USER/.config/rofi/config.rasi
cp ./binds.kdl /home/$USER/.config/niri/binds.kdl
cp ./alacritty.toml /home/$USER/.config/alacritty/alacritty.toml
sed -i 's/dms\/binds/binds/' /home/$USER/.config/niri/config.kdl
