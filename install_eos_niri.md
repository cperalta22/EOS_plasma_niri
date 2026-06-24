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

- Agregar alias básicos y plugins a .zshrc **(puedes copiar y ejecutar este bloque en tu terminal)**

```bash
# 1. Configurar Tema (ZSH_THEME='jaischeema') en ~/.zshrc
sed -i 's/^ZSH_THEME=.*/ZSH_THEME="jaischeema"/' ~/.zshrc

# 2. Configurar Plugins en ~/.zshrc
sed -i 's/^plugins=(.*/plugins=(git emoji vi-mode emotty bgnotify colored-man-pages compleat dircycle history jump sudo themes zsh-interactive-cd zsh-autosuggestions)/' ~/.zshrc

# 3. Limpiar alias antiguos de esta configuración (si existen) y agregar los nuevos
sed -i '/# >>> eos-plasma-niri aliases >>>/,/# <<< eos-plasma-niri aliases <<</d' ~/.zshrc

cat << 'EOF' >> ~/.zshrc

# >>> eos-plasma-niri aliases >>>
alias ls="eza -lhg --icons --git -snew"
alias c="bat"
alias vim="nvim"
alias ovim="/usr/bin/vim"
alias vi="nvim"
alias xport="xclip -selection clipboard"
alias ubmiproxy="ssh ifc -D1080 -N"
alias vz="nvim ~/.zshrc"
alias sz="source ~/.zshrc"
alias sl="/usr/bin/ls"
alias j="jump"
alias dfh='df -h | grep -v tmp'
alias here="nautilus . &"
alias lsblk="lsblk -o NAME,MODEL,SIZE,MOUNTPOINT,FSTYPE,LABEL"

# Opcionales / Personalizados (descomenta los que uses)
#alias pss="~/repos/my_configs/scripts/pss.sh"
#alias pskill="~/repos/my_configs/scripts/pskill.sh"
#alias opentunel="sed -i 's/^#//' /storage/Sync/tunel/tunel.sh && watch -d cat /storage/Sync/tunel/tunel.sh"
#alias aluxeproxy="ssh aluxelocal -D 1080 -N"
#alias querido_diario="/storage/Sync/scripts/querido_diario.sh"
#alias leer_diario="cat /storage/Sync/bitacora_ubmi/actividades.txt | gum pager"
#alias editar_diario="chmod u+w /storage/Sync/bitacora_ubmi/actividades.txt && nvim /storage/Sync/bitacora_ubmi/actividades.txt; chmod u-w /storage/Sync/bitacora_ubmi/actividades.txt"
#alias ww="nvim ~/vimwiki/index.md"
# <<< eos-plasma-niri aliases <<<
EOF
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

Puedes ejecutar el instalador interactivo [install_tui.py](file:///home/cpa/repos/EOS_plasma_niri/install_tui.py) para seleccionar y procesar estos paquetes:
- **En la interfaz interactiva (TUI):** Puedes marcar y desmarcar elementos uno por uno antes de confirmar la instalación.
- **Editando este archivo:** La preselección por defecto se lee directamente de aquí. Comentar un paquete con `#` lo dejará desmarcado por defecto, y descomentarlo lo dejará marcado. También puedes agregar nuevos paquetes o eliminar líneas directamente y la TUI los reconocerá.

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
# (ffmpeg ya está en básicos)

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
  linux-headers \
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
#  rocminfo
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
