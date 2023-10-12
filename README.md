# 🌸 Ansible Dotfiles

Fedora Linux configuration managed with Ansible.

![](src/screenshot.png)

## 🛁 Why

- Provides a quick and easy method of installing an operating system.
- Allow us to easily modify installed packages and applied settings.
- Focus on package installation via Flatpak and Distrobox to keep the system clean and simple.
- Thanks to the simplicity of the YAML language, it is very easy to understand & create additional tasks.

## 🚀 Installation

> ⛔ **Important variables are present in the `ansible/group_vars` directory. You need to edit them to customize your installation.**

Firstly, install Ansible:
```
# dnf install ansible
```

You can then clone this repository and enter it:
```
$ git clone https://github.com/steadywool/ansible-dotfiles
$ cd ansible-dotfiles
```

Start the playbook and configure your system with this command:
```
$ ansible-playbook ansible/playbook.yml -K
```

> ⚠️ **Tasks in the "user" playbook must be executed with the currently logged-in user, not with the root account.**

> ⛔ **If you run the entire playbook, or the "user" part with the `root` user, your configuration will be installed under the root account.**

## 🔧 Configuration

You can perform partially run of playbook using tags:

- packages
- configuration
- users
- flatpak
- dotfiles
- gnome
- services
- hostname
- firewalld
- fish
- vscode

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
$ ansible-playbook playbook.yml -t dotfiles
```
