# Configuration 🌸

Linux Dotfiles managed with Ansible and Git.

![](src/screenshot.png)

## Structure

Variables are present in the `ansible/group_vars` & `ansible/roles/ROLE_NAME/defaults` directories. You can edit them to customize your installation.

Dotfiles are located in the [`/files/dotfiles`](ansible/roles/02-users/files/dotfiles) directory of the user role.

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

All you have to do now is launch the Ansible Playbook:
```
# ansible-pull -U https://github.com/kaniville/ansible-dotfiles.git ansible/playbook.yml
```

⚠️ **The starting of NetworkManager may disconnect you.**

⚠️ **This playbook does not update the system.**

## Configuration

You can perform partially run of playbook using tags. For exemple, to install only dotfiles and start services:
```
# ansible-pull -U https://github.com/kaniville/ansible-dotfiles.git ansible/playbook.yml -t dotfiles,services
```

Available tags are:
- common
- user
- system
- configuration
- desktop
- services
- dotfiles
- packages

⚠️ **Be sure to change variables in the group_vars directory.**
