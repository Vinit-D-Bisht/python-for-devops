import psutil

def cpu_checkup():

    try:
        cpu_threshold=int(input("Enter the cpu threshold for your cpu: "))
    except ValueError:
        print("That was not a valid number")

    current_cpu = psutil.cpu_percent(interval=1)
    current_mem = psutil.virtual_memory().percent
    current_Disk = psutil.disk_usage("/").percent

    if current_cpu < cpu_threshold: 
        print("CPU threshold is under control and safe ")
    else:
        print("Alert! CPU threshold is reached....")


cpu_checkup()
