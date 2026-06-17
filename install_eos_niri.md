# Proceso para instalar y configurar ambiente de niri en eos con plasma

## Básicos

- Instalar eos con plasma
- Agregar [chaotic-aur](https://aur.chaotic.cx/docs)
- Instalar básicos

```bash
yay -Syu
yay -S zsh nvim fastfetch btop rocm-smi-lib eza bat fzf github-cli pacseek ttf-iosevka-nerd otf-font-awesome gum tree alacritty-smooth-cursor-git qt6ct nautilus-git ffmpeg 7zip jq poppler fd ripgrep zoxide resvg imagemagick wl-clipboard chafa
```



## SHELL y APPS elementales 

- Instalar [oh-my-zsh](https://ohmyz.sh/#install)
- Reiniciar / logout-login

- Clonar y habilitar [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#oh-my-zsh)

- Agregar alias basicos y plugins a .zshrc **REEMPLAZAR EN .zshrc en cada campo**

```bash

# tema
ZSH_THEME='jaischeema' 

# plugins
plugins=(git emoji vi-mode emotty  bgnotify colored-man-pages compleat dircycle history jump sudo themes zsh-interactive-cd zsh-autosuggestions )

# alias
alias ls="eza -lhg --icons --git -snew"
alias c="bat"
alias vim="nvim"
alias ovim="/usr/bin/vim"
alias vi="nvim"
alias xport="xclip -selection clipboard"
alias ubmiproxy="ssh ifc -D1080 -N"
alias vz="nvim /home/cpa/.zshrc"
alias sz="source /home/cpa/.zshrc"
alias sl="/usr/bin/ls"
alias j="jump"
#alias pss="/home/cpa/repos/my_configs/scripts/pss.sh"
#alias pskill="/home/cpa/repos/my_configs/scripts/pskill.sh"
alias dfh='df -h | grep -v tmp'
alias here="nautilus . &"
#alias opentunel="sed -i 's/^#//' /storage/Sync/tunel/tunel.sh && watch -d cat /storage/Sync/tunel/tunel.sh"
#alias aluxeproxy="ssh aluxelocal -D 1080 -N"
alias lsblk="lsblk -o NAME,MODEL,SIZE,MOUNTPOINT,FSTYPE,LABEL"
#alias querido_diario="/storage/Sync/scripts/querido_diario.sh"
#alias leer_diario="cat /storage/Sync/bitacora_ubmi/actividades.txt | gum pager"
#alias editar_diario="chmod u+w /storage/Sync/bitacora_ubmi/actividades.txt && nvim /storage/Sync/bitacora_ubmi/actividades.txt; chmod u-w /storage/Sync/bitacora_ubmi/actividades.txt"
#alias ww="nvim /home/cpa/vimwiki/index.md"

```

- Instalar [Atuin](https://atuin.sh/)
- Editar el config de atuin en ~/.config/atuin/config.toml para que esto quede asi  `enter_accept = false`

- Instalar [LazyVim](https://www.lazyvim.org/installation)
- Agregar plugin de vimwiki, y arreglar las autosugerencias ~/.config/nvim/lua/plugins

- esto es: ~/.config/nvim/lua/plugins/vimwiki.lua

```Lua 
return {
  {
    'vimwiki/vimwiki',
    init = function()
      -- Configura la ruta, la sintaxis y la extensión
      vim.g.vimwiki_list = {
        {
          path = '~/vimwiki/',
          syntax = 'markdown',
          ext = '.md',
        }
      }
      -- Fundamental: Evita que Vimwiki secuestre TODOS los archivos .md de tu sistema
      -- y solo actúe sobre los que están en ~/vimwiki/
      vim.g.vimwiki_global_ext = 0 
    end,
  }
}
```

- esto es: ~/.config/nvim/lua/plugins/blink.lua

```Lua 
return {
  "saghen/blink.cmp",
  opts = {
    keymap = {
      preset = "super-tab",
    },
  },
}
```

## Software complementario

Comenta lo que no utilices de aca abajo

```bash
# CLI Essential Utilities
yay -S \
  zellij \
  flatpak \
  sshfs \
  speech-dispatcher \
  espeakup


# GUI Essential Utilities
yay -S \
#  xfce4-appfinder \
#  rpi-imager \
  gnome-disk-utility \
  rofi \
  rofi-themes-collection-git \
#  gthumb

# Additional System Monitors
yay -S \
#  nvtop \
  s-tui \
  stress

# Web Browsers
#yay -S \
#  google-chrome

# Audio
yay -S \
  easyeffects \
  easyeffects-bundy01-presets \
  calf

# Video
yay -S \
  ffmpeg

flatpak install \
  com.obsproject.Studio \
#  com.obsproject.Studio.Plugin.BackgroundRemoval

# Image Edition
yay -S \
  gimp \
  inkscape

# Office Software
yay -S \
  libreoffice-fresh \
  libreoffice-fresh-es \
  densify \
  okular

# Laptop Monitor Brightness Control
#yay -S \
#  brightnessctl

# Gaming
#yay- S \
  lutris \
  steam-devices-git \
  lib32-mesa

#flatpak install \
  com.valvesoftware.Steam

# Software you probably don't need
yay -S \
  openrgb \
  zotero-bin \
  tailscale \
#  xf86-input-wacom \
  igv \
  proxy-ns \
  syncthing \
#  upscayl-bin \
#  open-webui \
  virtualbox \
  virtualbox-host-dkms \
  pandoc \
  texlive-latex \
  texlive-fontsrecommended \
  texlive-fonts-fontawesome \
  texlive-latexextra \
  texlive-fontutils \
  texlive-xetex \
  ttf-ms-fonts \ 
  ttf-google

flatpak install \
  org.freefilesync.FreeFileSync

# Required for AMD discrete GPUs
#yay -S \
#  vulkan-radeon \
#  radeontop \
#  rocminfo \
#  rocm-smi-lib
```


## Instalar Niri y DMS

- Seguir [instrucciones](https://github.com/niri-wm/niri/wiki/Getting-Started) actualizadas
- A continuación instalamos los ajustes adicionales 

```bash
curl -fsSL https://install.danklinux.com | sh
```

- finalmente ejecutamos `./cp_configs.sh` para incorporar los binds y configuraciones de alacritty y rofi

## Configurar DMS

- Usa los menus interactivos del shell para terminar de configurar

## Otros ajustes

### habilitar sintesis de voz

`systemctl --user enable --now speech-dispatcher.socket`
