cb = {
    1:  '\033[40m',      # black background
    2:  '\033[41m',      # red background
    3:  '\033[42m',      # green background
    4:  '\033[43m',      # yellow background
    5:  '\033[44m',      # blue background
    6:  '\033[45m',      # magenta background
    7:  '\033[46m',      # cyan background
    8:  '\033[47m',      # white background
    9:  '\033[1;40m',    # bright black background
    10: '\033[1;41m',   # bright red background
    11: '\033[1;42m',   # bright green background
    12: '\033[1;43m',   # bright yellow background
    13: '\033[1;44m',   # bright blue background
    14: '\033[1;45m',   # bright magenta background
    15: '\033[1;46m',   # bright cyan background
    16: '\033[1;47m',   # bright white background
}

cf = {
    1:  '\033[30m',      # black
    2:  '\033[31m',      # red
    3:  '\033[32m',      # green
    4:  '\033[33m',      # yellow
    5:  '\033[34m',      # blue
    6:  '\033[35m',      # magenta
    7:  '\033[36m',      # cyan
    8:  '\033[37m',      # white
    9:  '\033[1;30m',    # bright black
    10: '\033[1;31m',    # bright red
    11: '\033[1;32m',   # bright green
    12: '\033[1;33m',   # bright yellow
    13: '\033[1;34m',   # bright blue
    14: '\033[1;35m',   # bright magenta
    15: '\033[1;36m',   # bright cyan
    16: '\033[1;37m',   # bright white
}

color_codes = {f'c{key}': value for key, value in cf.items()}

r = '\033[0m' # reset to the default color

def get_color(key: int, foreground_color=True):
    if key in cf:
        if foreground_color:
            return cf[key]
        return cb[key]
    
    raise KeyError(f"Incorrect color key, {key}")