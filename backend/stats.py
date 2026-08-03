from time import sleep



for i in range(10):
    cpu = (open("/sys/class/thermal/thermal_zone0/temp")).read()
    print(round(float(cpu)/1000), 1)
    sleep(1)
