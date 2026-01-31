import psutil, wmi, platform, cpuinfo
from datetime import datetime
import os
import sys

state_file = os.path.join(
    os.environ.get("PROGRAMDATA", r"C:\ProgramData"),
    "pc_inventory.done"
)

if os.path.exists(state_file):
    sys.exit()

with open(state_file, "w") as f:
    f.write(f"Started: {datetime.now()}\n")

log_file = os.path.join(
    os.environ.get("PROGRAMDATA", r"C:\ProgramData"),
    "pc_inventory_log.txt"
)

try:
    my_cpu_info = cpuinfo.get_cpu_info()
    pc = wmi.WMI()
    os_info = pc.Win32_OperatingSystem()[0]
    gpu_info = pc.Win32_VideoController()[0]

    with open(log_file, "a") as f:
        f.write(f"--- Inventory at {datetime.now()} ---\n")
        f.write(f"Architecture: {platform.architecture()}\n")
        f.write(f"Network: {platform.node()}\n")
        f.write(f"OS: {platform.platform()}\n")
        f.write(f"CPU: {my_cpu_info['brand_raw']}\n")
        f.write(f"CPU Clock (Running): {my_cpu_info['hz_actual_friendly']}\n")
        f.write(f"CPU Clock (Manufacturer): {my_cpu_info['hz_advertised_friendly']}\n")
        f.write(f"CPU Cores: {psutil.cpu_count(logical=False)}\n")
        f.write(f"CPU Threads: {my_cpu_info['count']}\n")
        f.write(f"RAM: {psutil.virtual_memory().total / 1024**3:.0f} GB\n")
        f.write(f"GPU: {gpu_info.name}\n\n")

    with open(state_file, "a") as f:
        f.write("Completed successfully\n")

except Exception as e:
    with open(state_file, "a") as f:
        f.write(f"Failed: {e}\n")
