import functions_framework
import subprocess

@functions_framework.http
def has_nvidia_drivers():
    gpu = False
    out = subprocess.run("nvidia-smi", shell=True)
    if out.returncode == 0: # success state on shell command
        gpu = True

    return gpu  