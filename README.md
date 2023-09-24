# 🌸 Ansible Dotfiles

ArchLinux configuration managed with Ansible.

![](src/screenshot.png)

## 🛁 Why

- Provides a quick and easy method of installing an operating system.
- Allow us to easily modify installed packages and applied settings.
- Focus on package installation via Flatpak and Distrobox to keep the system clean and simple.
- Thanks to the simplicity of the YAML language, it is very easy to understand & create additional tasks.

## 🚀 Installation

> ⛔ **Important variables are present in the `ansible/host_vars` directory. You need to edit them to customize your installation.**

First, follow the [ArchLinux installation guide](https://wiki.archlinux.org/title/Installation_guide) and chroot into your system.

Then, let's clone the repository into a directory (for example, `/mnt`):
```
# git clone https://github.com/steadywool/ansible-dotfiles.git /mnt/ansible-dotfiles
# cd /mnt/ansible-dotfiles/ansible
```

The installation will be done in 3 steps, for each step we will use a different tag.
Let's use first the **LIVE** tag to install the necessary configuration to start the system:
```
# ansible-playbook playbook.yml -t LIVE
```

Quit the chroot and start your new system.
Start the `NetworkManager.service` service and configure your connection with `nmtui`:
```
# systemctl start NetworkManager.service
# nmtui
```

We will now use the **BOOT** tag:
```
# ansible-playbook playbook.yml -t BOOT
```

Your Gnome session will start. Log in with a user and use the **HOME** tag:
```
$ ansible-playbook playbook.yml -t HOME
```

> ⚠️ **Tasks in the "user" playbook must be executed with the currently logged-in user, not with the root account.

> ⛔ If you run the entire playbook, or the "user" part with the `root` user, your configuration will be installed under the root account.**

## 🔧 Configuration

You can perform partially run of playbook using tags.

Available tags are:
- LIVE
- BOOT
- HOME
- SYSTEM
- USER
- packages
- locale
- boot
- users
- configuration
- services
- security
- gnome
- flatpak
- dotfiles

> ⚠️ **This playbook does not update the system.**

## 📕 Exemples

Run the entire playbook:
```
$ ansible-playbook playbook.yml -K
```

> 📌 **The `-K` option is used to request the "sudo" password. We need it for tasks requiring privileges.**

Install every packages & enable/start Systemd services:
```
$ ansible-playbook playbook.yml -K -t packages,services
```

Executes tasks requiring no privileges:
```
$ ansible-playbook playbook.yml -t USER
```

> 📌 **The `HOME` tag don't require privileges either.**