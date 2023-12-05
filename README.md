# 🌸 Ansible Dotfiles

Fedora Workstation managed with Ansible.

![](src/screenshot.png)

## 📜 Preamble

### 🟢 What this playbook does ?

- Installs essential programs (for me).
- hardens your Fedora Linux.
- Configure your system & programs very easily.
- Customize the Gnome environment.

### 🔴 What this playbook doesn't do ?

- Update your operating system.
- Configure any other distribution than Fedora Linux.
- Install hardware-specific programs.
- Manage your partitions or your disks.

## 🚀 Installation

> ⚠️ **Important variables are present in the `host_vars` directory. You need to edit them to customize your installation.**

> ⚠️ **Additional variables are also present in the `vars` directories under each roles.**

> ⛔ **Never run this playbook with `sudo` or as root. If you need privileges, use the `-K` argument.**

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
$ ansible-playbook playbook.yml -K
```

## 🔧 Configuration

<details open>
    <summary>✨ You can perform partially run of playbook using tags:</summary>
    <ul>
        <li>packages</li>
        <li>packages.apps</li>
        <li>packages.copr</li>
        <li>packages.repo</li>
        <li>flatpak</li>
        <li>flatpak.remote</li>
        <li>flatpak.apps</li>
        <li>system</li>
        <li>system.hostname</li>
        <li>system.user</li>
        <li>system.sysctl</li>
        <li>system.adb</li>
        <li>security</li>
        <li>security.firewalld</li>
        <li>security.selinux</li>
        <li>security.usbguard</li>
        <li>security.snapper</li>
        <li>services</li>
        <li>services.system</li>
        <li>services.user</li>
        <li>dotfiles</li>
        <li>desktop</li>
        <li>desktop.dconf</li>
        <li>desktop.font</li>
    </ul>
</details>

## 📕 Exemples

Install every packages & enable/start Systemd services:
```
$ ansible-playbook playbook.yml -K -t packages,services
```

Executes tasks requiring no privileges:
```
$ ansible-playbook playbook.yml -t dotfiles,desktop
```

Execute the entire playbook but skip the configuration of Usbguard & Snapper:
```
$ ansible-playbook playbook.yml -K --skip-tags usbguard,snapper
```

For more arguments, check the man page with the command `man ansible-playbook`.