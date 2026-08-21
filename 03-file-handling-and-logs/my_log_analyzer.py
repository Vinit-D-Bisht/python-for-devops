from pathlib import Path
import json

def file_open():
    log_file = Path(__file__).parent / "app.log"
    with open(log_file,"r") as file:
        return file.readlines()

def analyze(Line):
    lines={
            "INFO":0,
            "WARNING":0,
            "ERROR":0
            }
    for l in Line:
        if "INFO" in l:
            lines["INFO"] += 1
        elif "ERROR" in l:
            lines["ERROR"] += 1
        elif "WARNING" in l:
            lines["WARNING"] += 1
        else:
            pass

    return lines

def output_gen(C):
    with open("log_summary.json","w+") as opfile:
        json.dump(C,opfile)

try:
    log_list = file_open()
    content = analyze(log_list)
    output_gen(content)
except FileNotFoundError as e:
    print(f"error occured {e}")
