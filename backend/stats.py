from time import sleep

cpu = open("/sys/class/thermal/thermal_zone0/temp")

for i in range(10):
    print(cpu.read())
    sleep(1)
