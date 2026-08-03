def cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp") as f:
        cpu = float(f.read()) / 1000
    return round(cpu, 1)

print(cpu_temp())
