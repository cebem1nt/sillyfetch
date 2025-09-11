CONFIG_DIR="$HOME/.config/sillyfetch"
# Shortcut in /usr/bin 
SILLYFETCH_BIN="/usr/bin/sillyfetch"

if [ ! -d  "$CONFIG_DIR" ]; then
    echo "Creating config directory..."
    mkdir -p "$CONFIG_DIR"
    echo "Copying default config"
    cp default_config.py "$CONFIG_DIR/config.py"
fi

if [ ! -f "$SILLYFETCH_BIN" ]; then
    echo "Adding shortcut to /usr/bin ..."
    # Important! Script won't run if you delete this repo ! 
    echo "python3 $(pwd)/sillyfetch.py" | sudo tee "$SILLYFETCH_BIN" > /dev/null
    sudo chmod +x "$SILLYFETCH_BIN"
fi

echo "Setup finished"