import time, json, os
from subprocess import run, PIPE, CalledProcessError

__CACHE_DIR = os.path.expanduser("~/.cache/sillyfetch")

def add_function_marks(out: any):
    # Add special marks to identify beginning and the end of function's output
    # Also ensure the out is converted to string
    return "%^^" + str(out) + "^^%"

def add_function_marks_wrapper(func):
    # Wrapper function for custom user functions, to colorize them while rendering

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapped = add_function_marks(result)
        return wrapped
    
    return wrapper

def run_command(command: str):
    # Run linux specific shell comands silently 
    # return empty string if couldn't run command
    try:
        result = run(command, stdout=PIPE, stderr=PIPE, shell=True, text=True)
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return ""
            
    except CalledProcessError as e:
        print(e)
        return ""

def set_cache(key:str, val: any):
    os.makedirs(__CACHE_DIR, exist_ok=True)

    with open(os.path.join(__CACHE_DIR, key), 'w') as f:
        json.dump(val, f)

def get_cache(key:str, expiration_days = 30) -> str:
    cached_file = os.path.join(__CACHE_DIR, key)
    expiration_time = expiration_days * 86400

    try:
        modification_time = os.path.getmtime(cached_file)
        current_time = time.time()

        if current_time - modification_time < expiration_time:
            with open(cached_file, 'r') as f:
                return json.load(f)
        else:
            os.remove(cached_file)  # if the cache has expired delete the file
    except:
        return None