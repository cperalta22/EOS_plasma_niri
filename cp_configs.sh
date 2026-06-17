#!/usr/bin/bash

[ ! -d /home/$USER/.config/rofi ] && mkdir -p /home/$USER/.config/rofi ]
cp ./rofidmenu.rasi /home/$USER/.config/rofi/rofidmenu.rasi
cp ./config.rasi /home/$USER/.config/rofi/config.rasi
cp ./binds.kdl /home/$USER/.config/niri/binds.kdl
sed -i 's/dms\/binds/binds/' /home/$USER/.config/niri/config.kdl
sed -i 's/\/\/ focus-follows/focus-follows/' /home/$USER/.config/niri/config.kdl
cp ./alacritty.toml /home/$USER/.config/alacritty/alacritty.toml
grep -q "QT_QPA_PLATFORMTHEME=qt6ct" /etc/environment || echo "QT_QPA_PLATFORMTHEME=qt6ct" | sudo tee -a /etc/environment >/dev/null
