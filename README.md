# 🎩 Fedora Playbook

Fedora Workstation managed with Ansible.

## 📜 Preamble

### 🟢 What this playbook does ?

- Installs essential programs.
- hardens your Fedora Linux.
- Configure your system & programs very easily.
- Customize the Gnome environment.

### 🔴 What this playbook doesn't do ?

- Update your operating system.
- Configure any other distribution than Fedora Linux.
- Install hardware-specific programs.
- Manage your partitions or your disks.

## 🚀 Installation

> [!WARNING]
> Variables are present in the `group_vars` directory. You need to edit them to customize your installation. </br></br>
> If you need a "sudo" password, use the `-K` (upper-case) argument. </br></br>

Firstly, install Ansible:
```
# dnf install ansible
```

You can then clone this repository and enter it:
```
$ git clone https://github.com/steadywool/fedora-playbook.git
$ cd fedora-playbook
```

Start the playbook and configure your system with this command:
```
$ ansible-playbook playbook.yml -K
```

## ✨ Configuration

You can perform partially run of playbook using tags.

You can list them with this command:
```
$ ansible-playbook playbook.yml --list-tags
```

Then use them with the `-t ROLE` parameter.