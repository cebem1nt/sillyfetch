#!/usr/bin/env python3
import shutil, sys, os, re, subprocess, fetches
from itertools import zip_longest
from logos import get_logos_values
from colors import get_color, r, color_codes

def ensure_config_exist(config_dir: str):
    #Check does config exist, copy default one if no config found
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

        config_file = os.path.join(config_dir, 'config.py')

        if not os.path.exists(config_file):
            
            current_dir = os.path.dirname(os.path.abspath(__file__))
            shutil.copy(os.path.join(current_dir, 'default_config.py'), config_file)

def add_function_marks_wrapper(func):
    # Wrapper function for custom user functions, to colorize them in the future

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        wrapped = "%^^" + str(result) + "^^%"
        return wrapped
    
    return wrapper

class ConfigInterlayer:
    def __init__(self, settings: dict) -> None:
        self._logo_info_whitespace: int = settings["logo_info_whitespace"]
        self._colorize_functions: bool = settings["colorize_functions"]
        self._functions_color: str | int = settings["functions_color"]
        self._custom_fetches: dict = settings["custom_fetches"]
        self._text_color: str | int = settings["text_color"]
        self._logo_position: str = settings["logo_position"]
        self._lstrip_info: bool = settings["lstrip_info"]
        self._print_logo: bool = settings["print_logo"]
        self._logo: str | dict = settings["logo"]
        self._layout: str = settings["layout"]

    def get_logo_info_whitespace(self):
        return self._logo_info_whitespace
    
    def get_custom_fetches(self):
        return self._custom_fetches

    def get_lstrip_info(self):
        return self._lstrip_info

    def get_colorize_functions(self):
        return self._colorize_functions

    def get_logo_position(self):
        if self._logo_position in ['top', 'left', 'bottom', 'right']:
            return self._logo_position
        
        raise ValueError(f"Incorrect logo_position: {self._logo_position}")

    def get_functions_color(self):
        if self.get_colorize_functions():
            if self._functions_color == 'logo':
                return self.get_logo_main_color()

            return get_color(self._functions_color)
        return ''
    

    def get_text_color(self):
        if self._text_color == 'logo':
            return self.get_logo_main_color()

        return get_color(self._text_color)
    

    def get_logo(self):
        if not self._print_logo:
            return ' '

        if isinstance(self._logo, dict) and "logo" in self._logo:
            return self._logo["logo"]

        elif self._logo == "auto":
            return get_logos_values()["logo"]
        
        elif self._logo.startswith("name_"):
            distro_name = self._logo.replace("name_", '')
            return get_logos_values(key=distro_name)["logo"]
        
        else:
            raise KeyError(f"Incorrect logo: {self._logo}")
        

    def get_logo_main_color(self):
        if isinstance(self._logo, dict) and "logo" in self._logo:
            return self._logo["main_color"]

        elif self._logo == "auto":
            return get_logos_values()["main_color"]
        
        elif self._logo.startswith("name_"):
            distro_name = self._logo.replace("name_", '')
            return get_logos_values(key=distro_name)["main_color"]
        
        else:
            raise KeyError(f"Incorrect logo: {self._logo}")


    def get_evaluated_layout(self):
        eval_dict = {}

        for f in dir(fetches):
            if callable(getattr(fetches, f)) and not f.startswith('__'):
                eval_dict[f] = getattr(fetches, f)

        for key, function in self.get_custom_fetches().items():
            self._custom_fetches[key] = add_function_marks_wrapper(function)

        eval_dict.update(self._custom_fetches)
        eval_dict.update(color_codes)

        evaluated_layout: str = eval(f"f'''{self._layout}'''", { "__builtins__" : None }, eval_dict)
        
        lines = evaluated_layout.splitlines()
        functions_color = self.get_functions_color()
        text_color = self.get_text_color()
        
        formatted_lines = []

        for line in lines:
            if self.get_lstrip_info():
                line = line.lstrip()
            
            # Replace placeholders with respective colors
            line = text_color + line.replace("%^^", functions_color).replace("^^%", text_color)
            
            # Check for multi-line split markers
            if "%^&" in line:
                beginning, rest = line.split("%^&", 1)
                items = rest.split("%!&")
                multi_lines = [beginning + functions_color + item + text_color for item in items]
                formatted_lines.extend(multi_lines)
            else:
                formatted_lines.append(line)

        return "\n".join(formatted_lines)

def strip_ansii(text: str):
    pattern = r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])'
    ansi_escape = re.compile(pattern)
    return ansi_escape.sub('', text)


def get_separator(largest_line: str, main_line: str, whitespace_length: int) -> str:
    sep_length = largest_line - len(strip_ansii(main_line.rstrip())) + whitespace_length-1
    return " " * sep_length 

def get_largest_line(lines: list):
    return max(len(strip_ansii(l.rstrip())) for l in lines)


def print_logo_info_line_lef_right(logo_line: str, info_line: str, position: str, 
                         separator: str, logo_main_color: str):
    
    if position == 'left':
        print(f"{logo_main_color}{logo_line.rstrip()}{r}" + separator, end=' ')
        print(f"{info_line}{r}")

    elif position == 'right':
        print(f"{info_line.rstrip()}{r}" + separator, end=' ')
        print(f"{logo_main_color}{logo_line}{r}")


def print_logo_info_top_bottom(logo_text: str, info_text: str, 
                        postion: str, logo_main_color: str):
    
    if postion == 'top':
        print(logo_main_color + logo_text + r)
        print(info_text + r)

    elif postion == 'bottom':
        print(info_text + r)
        print(logo_main_color + logo_text + r)


def render(config_object: ConfigInterlayer):
    logo_main_color = config_object.get_logo_main_color()
    position = config_object.get_logo_position()

    # Split logo and info text into lines
    logo = config_object.get_logo()
    info = config_object.get_evaluated_layout()

    whitespace_length = config_object.get_logo_info_whitespace()

    # Find the maximum length of logo lines for alignment (ignoring ANSI escape codes) and whitespaces from right

    subprocess.run(['setterm', '-linewrap', 'off'])

    if position in ['top', 'bottom']:
        print_logo_info_top_bottom(logo, info, position, logo_main_color)
        return
    
    elif position == 'left':
        largest_line = get_largest_line(logo.splitlines())

    else: 
        largest_line = get_largest_line(info.splitlines())


    for logo_line, info_line in zip_longest(logo.splitlines(), info.splitlines(), fillvalue=''):

        if position == 'left':
            main_line = logo_line

        else:
            main_line = info_line

        separator = get_separator(
            largest_line, main_line, whitespace_length
        )

        # Print logo line with the appropriate space and color
        print_logo_info_line_lef_right(
            logo_line, info_line, position, separator, logo_main_color
        )


    subprocess.run(['setterm', '-linewrap', 'on'])

def main(config_dir='~/.config/sillyfetch'):
    config_dir = os.path.expanduser(config_dir)
    sys.path.append(config_dir)
    ensure_config_exist(config_dir)

    from config import settings
    config_object = ConfigInterlayer(settings)

    render(config_object)

if __name__ == '__main__':
    main()