# Dotfiles

Linux Dotfiles managed with Ansible and Git 🌸

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

Here is the partitioning I use:

| Partition               | Mount Options                             | Filesystem | Mount Point   |
|-------------------------|-------------------------------------------|------------|---------------|
| `/dev/sda1`             |`nodev,noexec,nosuid`                      | FAT-32     | `/boot`       |
| `/dev/sda2`             |                                           | Swap       | [SWAP]        |
| `/dev/sda3`             |                                           | Luks2      |               |
| `/dev/mapper/luks_root` |`noatime,compress=zstd,subvol=@`           | Btrfs      | `/`           |
| `/dev/mapper/luks_root` |`noatime,compress=zstd,subvol=@.snapshots` | Btrfs      | `/.snapshots` |
| `/dev/mapper/luks_root` |`noatime,compress=zstd,subvol=@var`        | Btrfs      | `/var`        |
| `/dev/sda4`             |                                           | Ext4       | `/home`       |

## Installation

First, follow the [ArchLinux installation guide](https://wiki.archlinux.org/title/Installation_guide) and chroot into your system.

Be sure that Ansible & Git are installed in your system:
```
# pacman -S ansible git
```

Or if you haven't chrooted yet:
```
# pacstrap -K /mnt ansible git
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
- packages
- services
- dotfiles

You can skip the "user" part like this:
```
# ansible-pull -U https://github.com/kaniville/ansible-dotfiles.git ansible/playbook.yml --tags core,system,desktop
```

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
```
<sup>main.yml</sup>
