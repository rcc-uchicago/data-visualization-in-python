import sys

print("Python Version:")
print(sys.version)

import cpuinfo

def get_cpu_info():
    info = cpuinfo.get_cpu_info()
    return info

def get_cpu_manufacturer(info):
    if 'GenuineIntel' in info['brand_raw']:
        return 'Intel'
    elif 'AuthenticAMD' in info['brand_raw']:
        return 'AMD'
    else:
        return 'Unknown'

if __name__ == "__main__":
    info = get_cpu_info()
    manufacturer = get_cpu_manufacturer(info)
    print(f"CPU Model: {info['brand_raw']}")
    print(f"CPU Manufacturer: {manufacturer}")

