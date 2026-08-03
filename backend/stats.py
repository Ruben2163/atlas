cpu = open("/sys/class/thermal/thermal_zone0/temp")

print(cpu.read())
