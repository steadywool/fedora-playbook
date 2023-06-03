# Configuration 🌸

ArchLinux configuration managed with Ansible.

## Preambule

⚠️ **Important variables are present in the `ansible/group_vars` directory. You need to edit them to customize your installation.**

Here is the partitioning I use:

| Partition                 | Mount Options                                     | Filesystem | Mount Point   |
|---------------------------|---------------------------------------------------|------------|---------------|
| `/dev/sda1`               | `nodev,noexec,nosuid`                             | vfat       | `/boot`       |
| `/dev/sda2`               |                                                   | swap       | none          |
| `/dev/sda3`               |                                                   | luks2      |               |
| `/dev/mapper/luks_root`   | `noatime,compress=zstd,subvol=@`                  | btrfs      | `/`           |
| `/dev/mapper/luks_root`   | `noatime,compress=zstd,subvol=@.snapshots`        | btrfs      | `/.snapshots` |
| `/dev/mapper/luks_root`   | `noatime,compress=zstd,subvol=@var_log`           | btrfs      | `/var/log`    |
| `/dev/mapper/luks_root`   | `nodev,nosuid,noatime,compress=zstd,subvol=@home` | btrfs      | `/home`       |
| `/dev/mapper/luks_root`   | `nodev,nosuid,noatime,compress=zstd,subvol=@opt`  | btrfs      | `/opt`        |
| `/dev/mapper/luks_root`   | `nodev,nosuid,noatime,compress=zstd,subvol=@srv`  | btrfs      | `/srv`        |
| `/dev/mapper/luks_root/@` |                                                   | btrfs      | `/var/cache`  |
| `/dev/mapper/luks_root/@` |                                                   | btrfs      | `/var/tmp`    |

## Installation

First, follow the [ArchLinux installation guide](https://wiki.archlinux.org/title/Installation_guide) and chroot into your system.

*You can also encrypt your swap memory by following [these instructions](https://wiki.archlinux.org/title/Dm-crypt/Swap_encryption).*

Then, let's clone the repository into a directory (for example, `/mnt`):
```
# git clone https://github.com/kaniville/ansible-configuration.git /mnt/ansible-configuration
# cd /mnt/ansible-configuration
```

The installation will be done in 3 steps, for each step we will use a different tag.
Let's use first the **LIVE** tag to install the necessary configuration to start the system:
```
# ansible-playbook playbook.yml -t LIVE
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
# ansible-playbook playbook.yml -t ROOT
```

⚠️ **Don't forget to modify the variables in `group_vars`, especially the user password !**

Finally, GDM should start. Install dotfiles & Flatpak packages with the **USER** tag:
```
$ ansible-playbook playbook.yml -t USER
```

## Configuration

You can perform partially run of playbook using tags.

Available tags are:
- LIVE
- ROOT
- USER
- 00-core
- 01-system
- 02-users
- 03-desktop
- 04-homedir
- boot
- kernel
- hostname
- timezone
- locale
- packages
- usbguard
- snapshot
- services
- systemd
- sudo
- user
- flatpak
- dotfiles

⚠️ **This playbook does not update the system.**

## Exemples

Run the entire playbook:
```
$ ansible-playbook playbook.yml -K
```

📌 **The `-K` option is used to request the "sudo" password. We need it for tasks requiring privileges.**

Install every packages & enable/start Systemd services:
```
$ ansible-playbook playbook.yml -K -t packages,services
```

Executes tasks requiring no privileges:
```
$ ansible-playbook playbook.yml -t USER
```
📌 **The `04-homedir`, `dotfiles` & `flatpak` tags don't require privileges either.**
