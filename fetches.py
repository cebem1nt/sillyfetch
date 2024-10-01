import os, socket, re, math, platform
from shutil import which
from colors import cb, cf, r
from subprocess import run, PIPE, CalledProcessError

def __add_function_marks(string : str):
    # Add special marks to identify beginning and the end of function's output
    return "%^^" + string + "^^%"

def __run_command(command: str):
    #
    # Run linux specific shell comands silently 
    # return empty string if couldnt run command
    # 
    try:
        result = run(command, stdout=PIPE, stderr=PIPE, shell=True, text=True)
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return ""
            
    except CalledProcessError as e:
        print(e)
        return ""

def distro(architecture=False):
    name = __run_command(f"cat /etc/*-release | grep 'PRETTY_NAME'").split('=')[1].replace('"', '')

    if architecture:
        name += " " + platform.machine()

    return __add_function_marks(name)

def distro_id():
    if os.path.isfile('/bedrock/etc/os-release'):
        os_file = '/bedrock/etc/os-release'
    elif os.path.isfile('/etc/os-release'):
        os_file = '/etc/os-release'
    else:
        raise FileNotFoundError("Can't find distro info file")

    id = __run_command(f"cat {os_file} | grep 'ID'").split('\n')[0].split('=')[1]
    
    return id

def model(version=False):
    device_dir = "/sys/devices/virtual/dmi/id/"
    device_name_file = os.path.join(device_dir, "product_name")
    device_version_file = os.path.join(device_dir, "product_version")

    product_info = ""

    if os.path.exists(device_name_file):
        product_info = __run_command(f"cat {device_name_file}").strip()

        if os.path.exists(device_version_file) and version:
            product_version = __run_command(f"cat {device_version_file}").strip()
            product_info += f" ({product_version})"

    return __add_function_marks(product_info)

def shell(version=True):
    shell = os.environ["SHELL"].split('/')[-1]

    pairs = {
        "fish" : lambda: __run_command("fish --version").replace("fish, version ","").strip(),
        "zsh"  : lambda: __run_command("zsh --version").split()[1],
        "bash" : lambda: os.environ.get('BASH_VERSION', '').split('(')[0].strip()
    }

    if version and shell in pairs:
        try:
            shell_ver = pairs[shell]()

        except:
            shell_ver = ""

        shell = f"{shell} {shell_ver}"
    
    return __add_function_marks(shell)

def kernel(small=True):
    kernel_info = __run_command("uname -r")

    if not small:
        kernel_info = "Linux " + kernel_info

    return __add_function_marks(kernel_info)


def terminal():
    return __add_function_marks(os.environ["TERM"].replace('xterm-', ''))

def uptime(up=False, length="full"):
    uptime_info = __run_command("uptime -p")

    if not up:
        uptime_info = uptime_info.replace("up ", "")

    if length == "medium":
        uptime_info = uptime_info.replace(' minutes', 'mins').replace(' hours', 'hrs').replace(' minute', 'min').replace(' hour', 'hr')

    elif length == "short":
        uptime_info = uptime_info.replace(' minutes', 'm').replace(' hours', 'h').replace(' minute', 'm').replace(' hour', 'h')

    return __add_function_marks(uptime_info)

def hostname():
    return __add_function_marks(f"{os.environ['USER']}@{socket.gethostname()}")

def packages():
    # tuple : querry command, package-manager name
    packages_queries = [
        ("kiss -l",                "kiss"),
        ("pacman -Qq",           "pacman"),
        ("dpkg-query -f '.\n' -W", "dpkg"),
        ("rpm -qa",                 "rpm"),
        ("xbps-query -l",          "xbps"),
        ("apk info",                "apk"),
        ("opkg list-installed",    "opkg"),
        ("pacman-g2 -Q",      "pacman-g2"),
        ("lvu installed",           "lvu"),
        ("tce-status -i",    "tce-status"),
        ("pkg_info",           "pkg_info"),
        ("tazpkg list",          "tazpkg"),
        ("gaze installed",      "sorcery"),
        ("alps showinstalled",     "alps"),
        ("butch list",            "butch"),
        ("mine -q",                "mine"),
        ('snap list',              'snap'),
        ('flatpak list',        'flatpak')
    ]

    res = ""
    total_pkgs = 0

    for p in packages_queries:
        binary = p[0].split()[0]

        if which(binary) is not None:
            pkgs = len(__run_command(p[0]).splitlines())
            total_pkgs += pkgs
            if pkgs > 0:
                res += f"{pkgs} {p[1]}, "

    res = res.rstrip(', ')

    if len(res.split()) == 2:
        return __add_function_marks(f"{res.split()[0]} ({res.split()[1]})")
    else:
        return __add_function_marks(f"{total_pkgs}, ({res})")
        
def de():
    return __add_function_marks(os.environ['DESKTOP_SESSION'])

def wm(protocol=True):
    des = os.environ['DESKTOP_SESSION'].lower()
    res = des

    if 'gnome' in des:
        res = 'Mutter'
    elif 'plasma' in des:
        res = 'KWin'
    elif 'xfce' in des:
        res = 'Xfwm'
    elif 'lxqt' in des:
        res = 'Openbox'
    elif 'cinnamon' in des:
        res = 'Muffin'
    elif 'mate' in des:
        res = 'Marco'

    if protocol:
        res = f"{res} ({os.getenv('XDG_SESSION_TYPE').strip().capitalize()})"

    return __add_function_marks(res)
    
def __gtk_fetch(param: str):
    try:
        gtk_config_path = os.path.expanduser('~/.config/gtk-3.0/settings.ini')
        if os.path.exists(gtk_config_path):
           out = __run_command(f"cat {gtk_config_path} | grep '{param}'")
           return out.split('=', maxsplit=1)[1].strip()
                    
        return None
    except Exception as e:
        print(f"Error fetching GTK theme: {str(e)}")
        return None

def gtk_theme():
    return __add_function_marks(__gtk_fetch('gtk-theme-name'))
    
def icon_theme():
    return __add_function_marks(__gtk_fetch('gtk-icon-theme-name'))
    
def cursor_theme():
    return __add_function_marks(__gtk_fetch('gtk-cursor-theme-name'))

def gtk_font():
    return __add_function_marks(__gtk_fetch('gtk-font-name'))


def cpu(round_to=2, full_name=False, colorize=False):

    cpu_data = __run_command("cat /proc/cpuinfo | grep 'model name'")
    cpu_count = len(cpu_data.split('\n'))
    cpu_info = cpu_data.split(':')[-1].strip()

    if not full_name:
        cpu_info = cpu_info.split('with')[0].strip()

    max_freq = int(__run_command("cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq"))

    cpu_max_freq_mhz = max_freq / 1000
    cpu_max_freq_ghz = max_freq / 1000 / 1000

    if cpu_max_freq_ghz > 1:
        cpu_freq_info = str(round(cpu_max_freq_ghz, round_to))+"GHz"
    else:
        cpu_freq_info = str(round(cpu_max_freq_mhz, round_to))+"MHz"

    full_cpu_info = f'{cpu_info} ({cpu_count}) @{cpu_freq_info}'

    if colorize:
        if "AMD" in cpu_info:
            full_cpu_info = f"{cf['2']}{full_cpu_info}{r}"

        elif "INTEL" in cpu_info or 'i7' in cpu_info or "i3" in cpu_info or "i5" in cpu_info:
            full_cpu_info = f"{cf['5']}{full_cpu_info}{r}"


    return __add_function_marks(full_cpu_info)

def gpu(full_name=True, colorize=False):
    output = __run_command("lspci | grep 'VGA'").replace('VGA compatible controller:', '').split('\n')
    gpus = []

    for string in output:
        matches = re.findall(r'\[(.*?)\]', string)
        gpu = str(matches).replace("'", '').replace('[', '').replace(']', '')
        gpu_l = gpu.lower()

        if full_name:
            if ("rtx" in gpu_l or "gtx" in gpu_l or "geforce" in gpu_l) and (not "nvidia" in gpu_l):
                gpu = f"NVIDIA {gpu}"

            elif ("ati" in gpu_l or "radeon" in gpu_l) and (not "amd" in gpu_l):
                gpu = f"AMD {gpu}"
            
        if colorize:
            if "NVIDIA" in gpu:
                gpu = f"{cf[3]}{gpu}{r}"

            elif "AMD" in gpu:
                gpu = f"{cf[2]}{gpu}{r}"

        gpus.append(gpu)
        
    if len(gpus) > 1:
        return '%^&' + '%!&'.join(gpus)

    return __add_function_marks(gpus[0])


def memory(GiB=True, round_to=3, colorize=True):
    memory_total = 0
    memory_used = 0
    memory_free = 0
    memory_percent = 0

    try:
        # Read /proc/meminfo to gather memory information
        with open('/proc/meminfo') as meminfo_file:
            for line in meminfo_file:
                if line.startswith('MemTotal:'):
                    memory_total = int(line.split()[1]) / 1024  # Convert from kB to MiB
                elif line.startswith('MemFree:'):
                    memory_free += int(line.split()[1]) / 1024  # Convert from kB to MiB
                elif line.startswith('Buffers:'):
                    memory_free += int(line.split()[1]) / 1024  # Convert from kB to MiB
                elif line.startswith('Cached:'):
                    memory_free += int(line.split()[1]) / 1024  # Convert from kB to MiB
                elif line.startswith('SReclaimable:'):
                    memory_free += int(line.split()[1]) / 1024  # Convert from kB to MiB
                elif line.startswith('Shmem:'):
                    memory_used += int(line.split()[1]) / 1024  # Convert from kB to MiB

        # Calculate used memory
        memory_used = (memory_total + memory_used - memory_free)

        # Calculate memory percentage
        if memory_total > 0:
            memory_percent = math.floor((memory_used / memory_total) * 100)

        if GiB:
            memory_used = str(round(memory_used / 1024, round_to)) + ' GiB'
            memory_total = str(round(memory_total / 1024, round_to)) + ' GiB'
            memory_free = str(round(memory_free / 1024, round_to)) + ' GiB'

        else:
            memory_used = str(round(memory_used / 1024, round_to)) + ' MiB'
            memory_total = str(round(memory_total / 1024, round_to)) + ' MiB'
            memory_free = str(round(memory_free / 1024, round_to)) + ' MiB'

        if colorize:
            memory_percent = f"{cf[3]}{memory_percent}"

        return __add_function_marks(f'{memory_used} / {memory_total} ({memory_percent}%%^^)')
 
    except:
        return None
    
def gpu_driver():
    output = __run_command("lspci | grep 'VGA'").replace('VGA compatible controller:', '').split('\n')
    drivers = []

    for string in output:
        PPI = string.split('  ')[0]
        info = __run_command(f'lspci -vv -s {PPI}')
        for line in info.split('\n'):
            if line.strip().startswith('Kernel driver in use:'):
                driver_name = line.split(':')[-1].strip()

                if driver_name.lower() == 'nvidia':
                    driver_version = __run_command('cat /proc/driver/nvidia/version').split('  ')[1] 

                    if __run_command("ls /lib/modules/$(uname -r)/updates/dkms | grep nvidia") != None:
                        driver_name = "nvidia-dkms"

                    drivers.append(f'{driver_name} {driver_version}')

                else:
                    drivers.append(driver_name)

    return __add_function_marks(drivers[0])

def colors(background=True, char="   ", normal_only=False):
    res = ""

    palette = cb if background else cf

    for i, color in enumerate(palette.keys()):
        if normal_only and i == 8:
            return res
        
        if i / 8 == 1:
            res += "\n"
        res += f"{palette[color]}{char}{r}" 

    return res


def disk(path='/', colorize=True, file_system=True, percent=True,
         round_mem_to=2):
    stat = os.statvfs(path)
    
    # Calculate space in bytes
    block_size = stat.f_frsize
    total_blocks = stat.f_blocks
    free_blocks = stat.f_bfree
    total_space = block_size * total_blocks
    free_space = block_size * free_blocks
    used_space = total_space - free_space
    
    # Convert bytes to GiB
    bytes_per_gib = 1024**3  # 1 GiB = 1024^3 bytes

    if round_mem_to:
        total_space_gib = round(total_space / bytes_per_gib, round_mem_to)
        used_space_gib = round(used_space / bytes_per_gib, round_mem_to)
    
    else:
        total_space_gib = int(total_space / bytes_per_gib)
        used_space_gib = int(used_space / bytes_per_gib)

    res = f"{used_space_gib} GiB / {total_space_gib} GiB"


    # Calculate percentage used
    if percent:
        percent_used = round((used_space / total_space) * 100, 2)

        if colorize:
            percent_used = f"{cf[3]}{percent_used}"

        res += f" ({percent_used}%%^^)"


    if file_system:
        output = __run_command('df -T | grep "/dev"')
        for line in output.splitlines():
            if line.startswith('/dev'):
                fs = line.split(' ')[1].strip() 
                res += f" - {fs}"
                break

    return __add_function_marks(res)



def monitor(refresh_rate=True, inch=True):
    """
    Get information about only one monitor with xrandr or 
    by looking in to /sys/class/drm/*/modes file
    """

    if which('xrandr') is None:
        res = __run_command("cat /sys/class/drm/*/modes").split('\n')[0]

    else:
        output_lines = __run_command("xrandr").split('\n')
        current_resolution = output_lines[0].split("current")[1].split(',')[0].replace(' ', '')
        refresh = float(output_lines[2].split()[1].replace('*', '').replace('+', ''))

        res = current_resolution

        if refresh_rate:
            res += f" @ {round(refresh)}Hz"

        if inch:
            match = re.search(r'(\d+)mm x (\d+)mm', output_lines[1])
            if match:
                w_mm = int(match.group(1))
                h_mm = int(match.group(2))

                # Convert millimeters to inches (1 inch = 25.4 mm)
                width_inch = w_mm / 25.4
                height_inch = h_mm / 25.4

                # Calculate the diagonal size in inches
                diagonal_inch = int(math.sqrt(width_inch**2 + height_inch**2))
                res += f' {diagonal_inch}"'

    return __add_function_marks(res)