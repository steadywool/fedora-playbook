function update
    snapper -c root create --command 'sudo pacman -Syu' --desc 'update'
    flatpak update
end
