# Dotfiles

Linux Dotfiles managed with Ansible a Git 🌸

![](src/screenshot.png)

## Structure

Here is the structure of the Playbook:
```
├── playbook.yml
└── roles
    ├── 01-core
    │   ├── defaults
    │   ├── files
    │   └── tasks
    ├── 02-system
    │   ├── defaults
    │   └── tasks
    ├── 03-desktop
    │   ├── defaults
    │   └── tasks
    └── 04-user
        ├── files
        ├── tasks
        └── vars
```

The variables are present in the `/defaults` and `/vars` files. You can edit them to customize your installation.

Dotfiles are located in the `/files` folder of the `04-user` role. They are automatically copied to your user directory.

## Installation

First, follow the [ArchLinux installation guide](https://wiki.archlinux.org/title/Installation_guide) and chroot into your system.

Be sure that Ansible is installed in your system:
```
# pacman -S ansible
```

Or if you haven't chrooted yet:
```
# pacstrap -K /mnt ansible
```

All you have to do now is launch the Ansible Playbook:
```
# ansible-pull -U https://github.com/kaniville/ansible-dotfiles.git ansible/playbook.yml --ask-vault-pass
```

Or you can use this Playbook like this:
```
$ git clone https://github.com/Kaniville/ansible-dotfiles.git
$ cd ansible-dotfiles/ansible
# ansible-playbook playbook.yml --ask-vault-pass
```

If you don't add the `--ask-vault-pass`, the user role is disabled.

## Configuration

You can perform partially run of playbook using tags:
```
# ansible-pull -U https://github.com/kaniville/ansible-dotfiles.git ansible/playbook.yml --ask-vault-pass --tags desktop,user
```

Available tags are:
- core
- system
- desktop
- user

In the future, each task will have an assigned tag.

## FAQ
- **How to create a user ?**

In my case, I created a [vault](https://docs.ansible.com/ansible/latest/vault_guide/index.html) in the `/vars` folder of the `04-user` role with these variables in it:
```
user:
  name: USER
  password: PASSWORD
  groups: GROUP1,GROUP2
  shell: SHELL
```
<sup>user.yml</sup>

All I had to do after that was import this file:
```
- name: Include the user vault
  ansible.builtin.include_vars:
    file: user.yml
  when: user is defined
```
<sup>main.yml</sup>
