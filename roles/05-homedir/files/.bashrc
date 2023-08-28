# PATH variable
export PATH=$PATH:$HOME/.local/bin

# XDG variables
export XDG_CONFIG_HOME=$HOME/.config
export XDG_CACHE_HOME=$HOME/.cache
export XDG_DATA_HOME=$HOME/.local/share

# Editor variables
EDITOR=vim
VISUAL=vim
PAGER=less

# Wayland
export MOZ_ENABLE_WAYLAND=1

# Git aliases
alias g="git"
alias ga="git add --all --verbose"
alias gc="git commit -am"
alias gp="git push"

# Color aliases
alias ls="ls --color=auto"
alias grep="grep --color=auto"
alias ip="ip --color"

# Usbguard aliases
alias usbl="usbguard list-devices -t"
alias usba="usbguard allow-device"
alias usbp="usbguard allow-device --permanent"
