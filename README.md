<p align="center">
  <img src="logo.png" alt="Commandshelf Logo" width="200" />
</p>

<h1 align="center">🧠 Commandshelf</h1>
<p align="center">Store, search, and run your favorite shell commands — from anywhere.</p>

<p align="center">
  <a href="https://github.com/h3ggem/Commandshelf/releases">
    <img src="https://img.shields.io/github/v/release/yourname/commandshelf-cli?style=for-the-badge" alt="Latest Release" />
  </a>
  <a href="https://github.com/h3ggem/Commandshelf/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/yourname/commandshelf-cli?style=for-the-badge" alt="License" />
  </a>
  <a href="https://github.com/h3ggem/Commandshelf/issues">
    <img src="https://img.shields.io/github/issues/yourname/commandshelf-cli?style=for-the-badge" alt="Issues" />
  </a>
  <a href="https://github.com/h3ggem/Commandshelf/pulls">
    <img src="https://img.shields.io/github/issues-pr/yourname/commandshelf-cli?style=for-the-badge" alt="Pull Requests" />
  </a>
  <a href="https://github.com/h3ggem/Commandshelf/stargazers">
    <img src="https://img.shields.io/github/stars/yourname/commandshelf-cli?style=for-the-badge" alt="Stars" />
  </a>
</p>


<h1 align="center">✨ What is Commandshelf?</h1>
<p align="center">Commandshelf is a lightweight, local CLI tool that lets you save and reuse your most important terminal commands using simple, memorable aliases.  
No more scrolling through `.bash_history` or losing time rewriting what you've already solved.
</p>

---

<h1 align="center">⚡️ Example Usage</h1>

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


<h1 align="center">🛠 Installation</h1>

One-liner install (coming soon):
```bash
curl -sSL https://commandshelf.sh/install.sh | bash
```

<h1 align="center">Manual install:</h1>

```bash
git clone https://github.com/yourname/commandshelf-cli.git
cd commandshelf
sudo chmod +x ./install.sh
./install.sh
```

---

<h1 align="center">🧩 Commands Available</h1>
<l>
- Command -	Description
- shelf add	(Save a new command with an alias)
- shelf run <alias>	(Run a saved command)
- shelf list	(Show all saved commands)
- shelf search	((coming soon) Search commands by keyword)
- shelf stats	((coming soon) Show most used commands)
- shelf remove	(Delete a command from the shelf)
</l>
  
---

<h1 align="center">💡 Tip</h1>
Name your commands clearly:

```bash
shelf add "fix docker stuck" "sudo systemctl restart docker"
shelf add "ssh into dev" "ssh ubuntu@dev-server"
```

---

<h1 align="center">📄 License</h1>
MIT License — free to use, fork, and share!

---

<h1 align="center">🚀 Contributing</h1>
Pull requests welcome!
If you’ve got an idea, open an issue or drop a PR.
This project is beginner-friendly and open to collaboration
