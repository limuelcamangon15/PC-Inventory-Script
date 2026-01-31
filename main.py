import psutil
import wmi
import platform
import cpuinfo

my_cpu_info = cpuinfo.get_cpu_info()
pc = wmi.WMI()

os_info = pc.Win32_OperatingSystem()[0]
gpu_info = pc.Win32_VideoController()[0]

print(f"Architecture: {platform.architecture()}")
print(f"Network: {platform.node()}")
print(f"Operating System: {platform.platform()}")

print(f"Full CPU Name: {my_cpu_info['brand_raw']}")
print(f"CPU Clock Speed (Running): {my_cpu_info['hz_actual_friendly']}")
print(f"CPU Clock Speed (Manufacturer): {my_cpu_info['hz_advertised_friendly']}")
print(f"CPU Architecture: {my_cpu_info['arch']}")
print(f"CPU Bits: {my_cpu_info['bits']}")
print(f"CPU Threads: {my_cpu_info['count']}")

print(f"Total RAM: {psutil.virtual_memory().total / 1024 / 1024 / 1024:.0f} GB")

print(f"GPU: {gpu_info.name}")