# Configuration 🌸

ArchLinux configuration managed with Ansible.

## Preambule

⚠️ **Important variables are present in the `ansible/group_vars` directory. You need to edit them to customize your installation.**

Here is the partitioning I use:

| Partition                 | Mount Options                                                  | Filesystem | Mount Point   |
|---------------------------|----------------------------------------------------------------|------------|---------------|
| `/dev/sda1`               |`nodev,noexec,nosuid`                                           | vfat       | `/boot`       |
| `/dev/sda2`               |                                                                | luks2      |               |
| `/dev/mapper/luks_root`   | `noatime,compress=zstd,subvol=@`                               | btrfs      | `/`           |
| `/dev/mapper/luks_root`   | `nodev,noexec,nosuid,noatime,compress=zstd,subvol=@.snapshots` | btrfs      | `/.snapshots` |
| `/dev/mapper/luks_root`   | `nodev,noexec,nosuid,noatime,compress=zstd,subvol=@.swap`      | btrfs      | `/.swap`      |
| `/dev/mapper/luks_root`   | `nodev,nosuid,noatime,compress=zstd,subvol=@opt`               | btrfs      | `/opt`        |
| `/dev/mapper/luks_root`   | `nodev,nosuid,noatime,compress=zstd,subvol=@srv`               | btrfs      | `/srv`        |
| `/dev/mapper/luks_root`   | `noatime,compress=zstd,subvol=@var_log`                        | btrfs      | `/var/log`    |
| `/dev/mapper/luks_root/@` |                                                                | btrfs      | `/var/cache`  |
| `/dev/mapper/luks_root/@` |                                                                | btrfs      | `/var/tmp`    |
| `/dev/sda3`               | `nodev,nosuid`                                                 | ext4       | `/home`       |
| `/.swap/swapfile`         |                                                                | swap       | none          |

## Installation

First, follow the [ArchLinux installation guide](https://wiki.archlinux.org/title/Installation_guide) and chroot into your system.

Then, let's clone the repository into a directory (for example, `/mnt`):
```
# git clone https://github.com/kaniville/ansible-configuration.git /mnt/ansible-configuration
```

The installation will be done in 3 steps, for each step we will use a different tag.
Let's use first the **LIVE** tag to install the necessary configuration to start the system:
```
# cd /mnt/ansible-configuration
# ansible-playbook ansible/playbook.yml -t LIVE
```

After that, let's create a password for the root account:
```
# passwd root
```

Quit the chroot and start your new system.
Start the `NetworkManager` service and configure your connection with `nmtui`:
```
# systemctl start NetworkManager
# nmtui
```

We will now use the **ROOT** tag:
```
# cd /mnt/ansible-configuration
# ansible-playbook ansible/playbook.yml -t ROOT
```

⚠️ **Don't forget to modify the variables in `group_vars`, especially the user password !**

Finally, start your user session and use the **USER** tag:
```
# cd /mnt/ansible-configuration
# ansible-playbook ansible/playbook.yml -t USER
```

## Configuration

You can perform partially run of playbook using tags.

Available tags are:
- LIVE
- ROOT
- USER
- 01-core
- 02-system
- 03-services
- 04-tools
- 05-desktop
- 06-users
- 07-homedir
- boot
- kernel
- hostname
- timezone
- locale
- logind
- packages
- aur
- snapshot
- user
- flatpak
- sudo
- services
- usbguard
- dotfiles
- gsettings

After the installation, you can run this playbook without tag to change some settings and install additional packages.

⚠️ **This playbook does not update the system.**
