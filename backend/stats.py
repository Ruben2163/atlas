from time import sleep



for i in range(10):
    cpu = open("/sys/class/thermal/thermal_zone0/temp")
    print(cpu.read())
    sleep(1)
