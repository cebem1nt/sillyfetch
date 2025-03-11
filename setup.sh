CONFIG_DIR="$HOME/.config/sillyfetch"
SILLYFETCH_BIN="/usr/bin/sillyfetch"

if [ ! -d  "$CONFIG_DIR" ]; then
    echo "Creating config directory..."
    mkdir -p "$CONFIG_DIR"
    echo "Copying default config"
    cp default_config.py "$CONFIG_DIR"
fi

if [ ! -f "$SILLYFETCH_BIN" ]; then
    echo "Adding shortcut to /usr/bin ..."
    echo "python3 $(pwd)/sillyfetch.py" | sudo tee "$SILLYFETCH_BIN" > /dev/null
fi

echo "Setup finished"