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
| `/dev/mapper/luks_root`   | `noatime,compress=zstd,subvol=@var_log`    | btrfs      | `/var/log`    |
| `/dev/mapper/luks_root/@` |                                                                | btrfs      | `/var/cache`  |
| `/dev/mapper/luks_root/@` |                                                                | btrfs      | `/var/tmp`    |

Don't forget to edit `ansible/group_vars/all`.

## Installation

First, follow the [ArchLinux installation guide](https://wiki.archlinux.org/title/Installation_guide) and chroot into your system.

⚠️ **By default, this playbook uses `linux-hardened` as kernel and follows the above partitioning !**

Be sure that Ansible is installed in your system:
```
# pacman -S ansible
```

Then install the AUR collection:
```
# ansible-galaxy collection install kewlfft.aur
```

After that, you can start the playbook with the LIVE tag. This will set up a basic but functional system:
```
# ansible-pull -U https://github.com/Kaniville/ansible-configuration.git ansible/playbook.yml -t LIVE
```

Before exiting chroot, create a password for the root user:
```
# passwd root
```

You can now start your system.

Connect to your network this way:
```
# systemctl start NetworkManager && nmtui
```

You can use the ROOT tag to further configure it:
```
# ansible-pull -U https://github.com/Kaniville/ansible-configuration.git ansible/playbook.yml -t ROOT
```

ℹ️ **By default this playbook use Systemd-homed to create the default user.
A configuration exists in `ansible/roles/06-users/tasks/user.yml` to create a traditional user if needed.**

Finally, leave the root session to connect with your user, and use the USER tag to finalize your configuration:
```
# ansible-pull -U https://github.com/Kaniville/ansible-configuration.git ansible/playbook.yml -t USER
```

ℹ️ **Systemd-homed users must start their sessions in order to write to them (because of encryption).**

## Configuration

You can perform partially run of playbook using tags.

Available tags are:
- LIVE
- ROOT
- USER
- core
- system
- services
- tools
- desktop
- users
- homedir
- hostname
- timezone
- locale
- boot
- kernel
- packages
- aur
- firejail
- snapshot
- user
- flatpak
- sudo
- usbguard
- dotfiles
- xdg

After the installation, you can run this playbook to change some settings and install additional packages.

⚠️ **This playbook does not update the system.**

## Usage

You can use this playbook without tags to reconfigure your entire system:
```
# ansible-pull -U https://github.com/Kaniville/ansible-configuration.git ansible/playbook.yml
```

⚠️ **You need to run this playbook as root !**
