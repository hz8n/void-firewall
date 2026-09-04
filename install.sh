#!/bin/bash
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.local/bin
ln -sf "$DIR/void-firewall.py" ~/.local/bin/void-firewall
chmod +x ~/.local/bin/void-firewall
echo "[+] installed -> ~/.local/bin/void-firewall | Design by al3rab | Terminal Advanced"
~/.local/bin/void-firewall --help | head -n 20
