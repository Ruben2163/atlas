import psutil

def cpu_temp():
    cpu_temp = round(psutil.sensors_temperatures().get('cpu_thermal')[0].current, 1)

    return cpu_temp

def cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=0.1)

    return cpu_usage

def ram_usage():
    return round(psutil.virtual_memory().used / 1024**3, 2)


def disk_usage():
    disk_usage = psutil.disk_usage("/").percent

    return disk_usage

def fan_usage():
    fan_usage = psutil.sensors_fans().get("pwmfan")[0].current

    return fan_usage
