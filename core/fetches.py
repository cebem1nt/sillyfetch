from utils.colors import cb, cf, r
from utils.functions import add_function_marks, run_command, set_cache, get_cache
from shutil import which
import os, socket, re, math, platform

def distro(architecture=False):
    name = run_command("cat /etc/*-release | grep 'PRETTY_NAME'").split('=')[1].replace('"', '')

    if architecture:
        name += " " + platform.machine()

    return add_function_marks(name)

def distro_id():
    if os.path.isfile('/bedrock/etc/os-release'):
        os_file = '/bedrock/etc/os-release'
    elif os.path.isfile('/etc/os-release'):
        os_file = '/etc/os-release'
    else:
        raise FileNotFoundError("Can't find distro info file")

    id = run_command(f"cat {os_file} | grep 'ID'").split('\n')[0].split('=')[1]
    
    return id

def model(version=False):
    device_dir = "/sys/devices/virtual/dmi/id/"
    device_name_file = os.path.join(device_dir, "product_name")
    device_version_file = os.path.join(device_dir, "product_version")

    product_info = ""

    if os.path.exists(device_name_file):
        product_info = run_command(f"cat {device_name_file}").strip()

        if os.path.exists(device_version_file) and version:
            product_version = run_command(f"cat {device_version_file}").strip()
            product_info += f" ({product_version})"

    return add_function_marks(product_info)

def shell(version=True):
    shell = os.environ["SHELL"].split('/')[-1]

    pairs = {
        "fish" : lambda: run_command("fish --version").replace("fish, version ","").strip(),
        "zsh"  : lambda: run_command("zsh --version").split()[1],
        "bash" : lambda: os.environ.get('BASH_VERSION', '').split('(')[0].strip()
    }

    if version and shell in pairs:
        try:
            shell_ver = pairs[shell]()

        except:
            shell_ver = ""

        shell = f"{shell} {shell_ver}"
    
    return add_function_marks(shell)

def kernel(small=True):
    kernel_info = run_command("uname -r")

    if not small:
        kernel_info = "Linux " + kernel_info

    return add_function_marks(kernel_info)

def terminal():
    return add_function_marks(os.environ["TERM"].replace('xterm-', ''))

def uptime(up=False, length="full"):
    uptime_info = run_command("uptime -p")

    if not up:
        uptime_info = uptime_info.replace("up ", "")

    if length == "medium":
        uptime_info = uptime_info.replace(' minutes', 'mins').replace(' hours', 'hrs').replace(' minute', 'min').replace(' hour', 'hr')

    elif length == "short":
        uptime_info = uptime_info.replace(' minutes', 'm').replace(' hours', 'h').replace(' minute', 'm').replace(' hour', 'h')

    return add_function_marks(uptime_info)

def hostname():
    return add_function_marks(f"{os.environ['USER']}@{socket.gethostname()}")

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

    total_pkgs = 0
    package_count = []

    for cmd, manager in packages_queries:
        binary = cmd.split()[0]

        if which(binary):
            pkgs = run_command(cmd).splitlines()
            num_pkgs = len(pkgs)

            if num_pkgs > 0:
                package_count.append(f"{num_pkgs} {manager}")

            total_pkgs += num_pkgs

    if len(package_count) > 1:
        return add_function_marks(f"{total_pkgs}, ({', '.join(package_count)})")
    else:
        _, manager = package_count[0].split()
        return add_function_marks(f"{total_pkgs}, {manager}")
        
def _get_de():
    ses = os.environ.get('DESKTOP_SESSION')
    return ses if ses else os.environ.get('XDG_SESSION_DESKTOP')

def de():
    return add_function_marks(_get_de())

def wm(protocol=True):
    des = _get_de().lower()
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

    return add_function_marks(res)
    
def __gtk_fetch(param: str):
    try:
        gtk_config_path = os.path.expanduser('~/.config/gtk-3.0/settings.ini')
        if os.path.exists(gtk_config_path):
           out = run_command(f"cat {gtk_config_path} | grep '{param}'")
           return out.split('=', maxsplit=1)[1].strip()
                    
        return None
    except Exception as e:
        print(f"Error fetching GTK theme: {str(e)}")
        return None

def gtk_theme():
    return add_function_marks(__gtk_fetch('gtk-theme-name'))
    
def icon_theme():
    return add_function_marks(__gtk_fetch('gtk-icon-theme-name'))
    
def cursor_theme():
    return add_function_marks(__gtk_fetch('gtk-cursor-theme-name'))

def gtk_font():
    return add_function_marks(__gtk_fetch('gtk-font-name'))


def cpu(round_to=2, full_name=False, colorize=False):

    cpu_data = run_command("cat /proc/cpuinfo | grep 'model name'")
    cpu_count = len(cpu_data.splitlines())
    cpu_info = cpu_data.split(':')[-1]

    if not full_name:
        if 'AMD' in cpu_info:
            cpu_info = cpu_info.replace('AMD', '')
        elif 'Intel' in cpu_info:
            cpu_info = cpu_info.replace('Intel(R) Core(TM)', '')

    max_freq = int(run_command("cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq"))

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

    return add_function_marks(full_cpu_info.strip())

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
            memory_used = str(round(memory_used, round_to)) + ' MiB'
            memory_total = str(round(memory_total, round_to)) + ' MiB'
            memory_free = str(round(memory_free, round_to)) + ' MiB'

        if colorize:
            memory_percent = f"{cf[3]}{memory_percent}"

        return add_function_marks(f'{memory_used} / {memory_total} ({memory_percent}%%^^)')
 
    except:
        return None

def gpu(full_name=True, colorize=False):
    gpus = get_cache('gpus') or []

    if not len(gpus):
        lspci_output = run_command("lspci | grep 'VGA'").splitlines()
        gpus = [' '.join(re.findall(r'\[([^\]]+)\]', gpu_line)) for gpu_line in lspci_output]
        set_cache('gpus', gpus)

    for i, gpu in enumerate(gpus):
        gpu_l = gpu.lower()

        if full_name:
            if 'geforce' in gpu_l and (not 'nvidia' in gpu_l):
                gpu =  'NVIDIA ' + gpu
            elif 'radeon' in gpu_l and (not 'amd' in gpu_l):
                gpu = 'AMD ' + gpu

        if colorize:
            if "NVIDIA" in gpu:
                gpu = f"{cf[3]}{gpu}{r}"

            elif "AMD" in gpu:
                gpu = f"{cf[2]}{gpu}{r}"

            elif "Intel" in gpu:
                gpu = f"{cf[5]}{gpu}{r}"

        gpus[i] = gpu
        
    if len(gpus) > 1:
        return '%^&' + '%!&'.join(gpus)

    return add_function_marks(gpus[0])
    
def gpu_driver(single_driver=True):
    drivers = get_cache('drivers', 10) or []
    
    if not len(drivers):
        lspci_output = run_command("lspci | grep 'VGA'").splitlines()

        for string in lspci_output:
            PPI = string.split()[0]
            kernel_driver = run_command(f"lspci -vv -s {PPI} | grep 'Kernel driver in use'").split(':')[-1].strip()

            if kernel_driver == 'nvidia':
                driver_version = run_command('cat /proc/driver/nvidia/version').split('  ')[1] 

                if run_command("ls /lib/modules/$(uname -r)/updates/dkms | grep nvidia"):
                    kernel_driver = "nvidia-dkms"

                drivers.append(f'{kernel_driver} {driver_version}')

            else:
                drivers.append(kernel_driver)
        set_cache('drivers', drivers)

    if single_driver:
        drivers = [drivers[0]]

    elif len(drivers) > 1:
        return '%^&' + '%!&'.join(drivers)

    return add_function_marks(drivers[0])

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


def disk(path='/', colorize=True, file_system=True, percent=True, round_mem_to=2):
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
        output = run_command('df -T | grep "/dev"')
        for line in output.splitlines():
            if line.startswith('/dev'):
                fs = line.split(' ')[1].strip() 
                res += f" - {fs}"
                break

    return add_function_marks(res)



def monitor(refresh_rate=True, inch=True):
    """
    Get information about monitors with xrandr or
    by looking in to /sys/class/drm/*/modes file.

    TODO: Doesn't work without xorg / xwayland
    """

    xrandr_output = run_command("xrandr | grep '*' | awk '{print $1, $2}'")

    if which('xrandr') is None or "Can't open display" in xrandr_output:
        res = run_command("cat /sys/class/drm/*/modes").split('\n')[0]

    else:
        monitors = []
        for monitor in xrandr_output.splitlines():
            resolution, refresh_rate = monitor.split()
            monitor = resolution
           
            if refresh_rate:
                monitor += f" @ {round(float(refresh_rate.replace('*', '').replace('+', '') ))}Hz"
            monitors.append(monitor)
                
        if inch:
            xrandr_monitor_info_output = run_command('xrandr | grep -i "mm x"').splitlines()
           
            for i, monitor in enumerate(xrandr_monitor_info_output):
                w_mm, h_mm = re.findall(r"(\d+)mm x (\d+)mm", monitor)[0]
                w_in, h_in = (int(w_mm) / 25.4, int(h_mm) / 25.4)

                diagonal_inch = int(math.sqrt(w_in**2 + h_in**2))
                monitors[i] += f' {diagonal_inch}"' 
                
    if len(monitors) > 1:
        return '%^&' + '%!&'.join(monitors)
    else:
        res = monitors[0]
        
    return add_function_marks(res)