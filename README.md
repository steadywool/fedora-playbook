# Configuration 🌸

ArchLinux configuration managed with Ansible.

![](src/screenshot-1.png)

## Structure

Variables are present in the `ansible/group_vars` & `ansible/roles/ROLE_NAME/defaults` directories. You can edit them to customize your installation.

Here is the partitioning I use:

| Partition               | Mount Options                                                 | Filesystem | Mount Point   |
|-------------------------|---------------------------------------------------------------|------------|---------------|
| `/dev/sda1`             |`nodev,noexec,nosuid`                                          | FAT-32     | `/boot`       |
| `/dev/sda2`             |                                                               | Swap       | [SWAP]        |
| `/dev/sda3`             |                                                               | Luks2      |               |
| `/dev/mapper/luks_root` |`noatime,compress=zstd,subvol=@`                               | Btrfs      | `/`           |
| `/dev/mapper/luks_root` |`nodev,noexec,nosuid,noatime,compress=zstd,subvol=@.snapshots` | Btrfs      | `/.snapshots` |
| `/dev/mapper/luks_root` |`noatime,compress=zstd,subvol=@var`                            | Btrfs      | `/var`        |
| `/dev/sda4`             | `nodev,nosuid`                                                | Ext4       | `/home`       |

## Installation

First, follow the [ArchLinux installation guide](https://wiki.archlinux.org/title/Installation_guide) and chroot into your system.

Be sure that Ansible & Git are installed in your system:
```
# pacman -S ansible git
```

Then install the AUR collection:
```
# ansible-galaxy collection install kewlfft.aur
```

After that, you can start the playbook with the chroot tag. It will install every packages and configure the system:
```
# ansible-pull -U https://github.com/Kaniville/ansible-configuration.git ansible/playbook.yml -t chroot
```

ℹ️ **With the "chroot" tag, only packages from the official repository, and the basic configuration will be installed.**

Before exiting chroot, create a password for the root user:
```
# passwd root
```

You can now start your system to finalize the configuration.

Connect to your network this way:
```
# systemctl start NetworkManager && nmtui
```

Then start the playbook without the chroot tag:
```
# ansible-pull -U https://github.com/Kaniville/ansible-configuration.git ansible/playbook.yml
```

## Configuration

You can perform partially run of playbook using tags.

Available tags are:
- chroot
- common
- users
- system
- tools
- desktop
- packages
- services
- hostname
- timezone
- locale
- boot
- kernel
- user
- dotfiles
- aur
- flatpak
- sudo
- usbguard
- firejail
- snapshot

After the installation, you can run this playbook to change some settings and install additional packages.

⚠️ **This playbook does not update the system.**
