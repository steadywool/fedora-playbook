# Configuration 🌸

ArchLinux configuration managed with Ansible.

![](src/screenshot-1.png)

## Structure

Variables are present in the `ansible/group_vars` & `ansible/roles/ROLE_NAME/defaults` directories. You can edit them to customize your installation.

Here is the partitioning I use:

| Partition                 | Mount Options                                                  | Filesystem | Mount Point   |
|---------------------------|----------------------------------------------------------------|------------|---------------|
| `/dev/sda1`               |`nodev,noexec,nosuid`                                           | vfat       | `/boot`       |
| `/dev/sda2`               |                                                                | swap       | none          |
| `/dev/sda3`               |                                                                | luks2      |               |
| `/dev/mapper/luks_root`   | `noatime,compress=zstd,subvol=@`                               | btrfs      | `/`           |
| `/dev/mapper/luks_root`   | `nodev,noexec,nosuid,noatime,compress=zstd,subvol=@.snapshots` | btrfs      | `/.snapshots` |
| `/dev/mapper/luks_root`   | `nodev,exec,nosuid,noatime,compress=zstd,subvol=@home`         | btrfs      | `/home`       |
| `/dev/mapper/luks_root`   | `nodev,noexec,nosuid,noatime,compress=zstd,subvol=@var_log`    | btrfs      | `/var/log`    |
| `/dev/mapper/luks_root/@` |                                                                | btrfs      | `/var/cache`  |
| `/dev/mapper/luks_root/@` |                                                                | btrfs      | `/var/tmp`    |

Don't forget to edit `ansible/group_vars/all`.

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

ℹ️ **With the "chroot" tag, only basic packages from the official repository (core & system), and the basic configuration (core) will be installed.**

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

ℹ️ **By default this playbook use Systemd-homed to create the default user.
A configuration exists in `ansible/roles/02-users/tasks/user.yml` to create a traditional user if needed.**

## Configuration

You can perform partially run of playbook using tags.

Available tags are:
- chroot
- core
- users
- system
- tools
- desktop
- applications
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
