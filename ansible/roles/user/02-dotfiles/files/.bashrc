# PATH
export PATH=$PATH:$HOME/.local/bin

# Wayland
if [ $XDG_SESSION_TYPE = "wayland" ]; then
    export MOZ_ENABLE_WAYLAND=1
fi

# Aliases
## Usbguard
alias usbl="usbguard list-devices"
alias usba="usbguard allow-device"
alias usbp="usbguard allow-device --permanent"

## Git
alias g="git"
alias ga="git add --all --verbose"
alias gc="git commit -am"
alias gp="git push"

## Colors
alias ls="ls --color=auto"
alias grep="grep --color=auto"
alias ip="ip --color"
