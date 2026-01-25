<pre><center>
 ▄████▄    █████▒ ▄████ 
▒██▀ ▀█  ▓██   ▒ ██▒ ▀█▒
▒▓█    ▄ ▒████ ░▒██░▄▄▄░
▒▓▓▄ ▄██▒░▓█▒  ░░▓█  ██▓
▒ ▓███▀ ░░▒█░   ░▒▓███▀▒
░ ░▒ ▒  ░ ▒ ░    ░▒   ▒ 
  ░  ▒    ░       ░   ░ 
░         ░ ░   ░ ░   ░ 
░ ░                   ░ 
░                       
  CTF FLAG GENERATOR
</center></pre>
# Random CTF Flag Generator

A simple Python script to generate random **CTF-style flags** based on user-defined length.  
This project uses Python's built-in `string` and `secrets` modules to ensure cryptographically secure random flag generation.

---

## Features
- Generates random flags with customizable length.
- Uses `secrets` for secure randomization (better than `random` for security purposes).
- Flags follow the typical `flag{...}` format.
- Lightweight and easy to run.

---

## Requirements
- Python 3.6+
- No external dependencies (only standard library modules: `string`, `secrets`).

---

## Usage

1. Clone this repository or copy the script:
```ba
git clone https://github.com/kraken-503/cfg.git
```

2. Run the script in your terminal:
```ba
python3 cfg.py
```
