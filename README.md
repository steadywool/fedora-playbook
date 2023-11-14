# 🌸 Ansible Dotfiles

Fedora Workstation configuration managed with Ansible.

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

> ⛔ **Important variables are present in the `ansible/host_vars` directory. You need to edit them to customize your installation.**

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

> ⛔ **If you run the playbook with the `root` user, your user configuration will be installed under the root account.**

## 🔧 Configuration

<details open>
    <summary>✨ You can perform partially run of playbook using tags:</summary>
    <ul>
        <li>SYSTEM</li>
        <li>USER</li>
        <li>packages</li>
        <li>configuration</li>
        <li>security</li>
        <li>services</li>
        <li>flatpak</li>
        <li>dotfiles</li>
        <li>desktop</li>
        <li>remote</li>
        <li>apps</li>
        <li>repo</li>
        <li>hostname</li>
        <li>users</li>
        <li>sysctl</li>
        <li>adb</li>
        <li>firewalld</li>
        <li>usbguard</li>
        <li>snapper</li>
        <li>fish</li>
        <li>vscode</li>
        <li>xdg</li>
        <li>papirus</li>
        <li>dconf</li>
        <li>font</li>
    </ul>
</details>

## 📕 Exemples

Install every packages & enable/start Systemd services:
```
$ ansible-playbook playbook.yml -K -t packages,services
```

> 📌 **The `-K` option is used to request the "sudo" password. We need it for tasks requiring privileges.**

Executes tasks requiring no privileges:
```
$ ansible-playbook playbook.yml -t USER
```

Execute the entire playbook but skip the "dotfiles" role:
```
$ ansible-playbook playbook.yml -K --skip-tags dotfiles
```

For more arguments, check the man page with the command `man ansible-playbook`.
