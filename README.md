# Dotfiles

Linux Dotfiles managed with Ansible and Git 🌸

![](src/screenshot.png)

## Structure

Here is the structure of the Playbook:
```
├── playbook.yml
└── roles
    ├── core
    │   ├── defaults
    │   ├── files
    │   └── tasks
    ├── desktop
    │   ├── defaults
    │   └── tasks
    ├── network
    │   ├── defaults
    │   └── tasks
    ├── security
    │   ├── defaults
    │   └── tasks
    ├── system
    │   ├── defaults
    │   └── tasks
    └── user
        ├── defaults
        ├── files
        └── tasks
```

The variables are present in the `/defaults` directories. You can edit them to customize your installation.

Dotfiles are located in the [`/files` folder of the `user` role](ansible/roles/user/files/dotfiles). They are automatically copied to your user directory.

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
# ansible-pull -U https://github.com/kaniville/ansible-dotfiles.git ansible/playbook.yml
```

Or you can use this Playbook like this:
```
$ git clone https://github.com/Kaniville/ansible-dotfiles.git
$ cd ansible-dotfiles/ansible
# ansible-playbook playbook.yml
```

## Configuration

You can perform partially run of playbook using tags:
```
# ansible-pull -U https://github.com/kaniville/ansible-dotfiles.git ansible/playbook.yml -t packages,services
```

Available tags are:
- core
- system
- security
- desktop
- user
- network
- packages
- services
- dotfiles

⚠️ **This playbook does not update the system.**
