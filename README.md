# 🧠 Commandshelf

Store, search, and run your favorite shell commands — from anywhere.

---

### ✨ What is Commandshelf?

> Commandshelf is a lightweight, local CLI tool that lets you save and reuse your most important terminal commands using simple, memorable aliases.  
No more scrolling through `.bash_history` or losing time rewriting what you've already solved.

---

### ⚡️ Example Usage

```bash
# Add a command to the shelf
$ shelf add "update system" "sudo apt update && sudo apt upgrade -y"

# Run it later by name
$ shelf run "update system"

# List your saved commands
$ shelf list

# Search the shelf
$ shelf search update
```

---


### 🛠 Installation
One-liner install (coming soon):
```bash
curl -sSL https://commandshelf.sh/install.sh | bash
```

### Manual install:
```bash
git clone https://github.com/yourname/commandshelf-cli.git
cd commandshelf
sudo chmod +x ./install.sh
./install.sh
```

---

### 🧩 Commands Available
- Command -	Description
- shelf add	(Save a new command with an alias)
- shelf run <alias>	(Run a saved command)
- shelf list	(Show all saved commands)
- shelf search	((coming soon) Search commands by keyword)
- shelf stats	((coming soon) Show most used commands)
- shelf remove	(Delete a command from the shelf)

---

### 💡 Tip
Name your commands clearly:

```bash
shelf add "fix docker stuck" "sudo systemctl restart docker"
shelf add "ssh into dev" "ssh ubuntu@dev-server"
```

---

### 📄 License
MIT License — free to use, fork, and share!

---

### 🚀 Contributing
Pull requests welcome!
If you’ve got an idea, open an issue or drop a PR.
This project is beginner-friendly and open to collaboration
