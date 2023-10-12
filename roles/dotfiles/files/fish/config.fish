
# PATH variable
set -gx PATH $HOME/.local/bin $PATH

# Interactive
if status is-interactive
    # Remove fish greeting
    set fish_greeting

    # Always source aliases
    for i in (ls $__fish_config_dir/aliases/)
        source $__fish_config_dir/aliases/$i
    end
end