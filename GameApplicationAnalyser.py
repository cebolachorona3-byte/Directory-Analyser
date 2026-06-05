import os
import csv

var_directory = input("Insert the directory for analysis: ")

var_estatistics = {"Images": 0, "Audio Files": 0, "Scripts": 0, "Total": 0}
var_estatisticssize = {"Images": 0, "Audio Files": 0, "Scripts": 0, "Total": 0}
var_filetypes = {".png": "Images", ".mp3": "Audio Files", ".cs": "Scripts"}
var_estatisticsreadable = {}
var_biggestarquives = []
var_top5biggestarquives = []

def func_convertsize(bytes):
    if bytes >= 1024 ** 3:
        return f"{bytes / (1024 ** 3):.2f} GB"
    elif bytes >= 1024 ** 2:
        return f"{bytes / (1024 ** 2):.2f} MB"
    elif bytes >= 1024:
        return f"{bytes / 1024:.2f} KB"
    else:
        return f"{bytes} B"

def func_initiateanalysis():
    for folder, subfolder, files in os.walk(var_directory):
        for file in files:
            nome, ext = os.path.splitext(file)
            if ext in var_filetypes:
                var_estatistics[var_filetypes[ext]] += 1
                var_completepath = os.path.join(folder, file)
                var_arquivesize = os.path.getsize(var_completepath)
                var_estatisticssize[var_filetypes[ext]] += var_arquivesize
                var_biggestarquives.append([file, var_arquivesize])

def func_calculatetotals():
    var_estatistics["Total"] = sum(
    value 
    for filetype, value in var_estatistics.items()
        if filetype != "Total"
                                )
    var_estatisticssize["Total"] = func_convertsize(sum(
        value 
        for filetype, value in var_estatisticssize.items()
            if filetype != "Total"
                                    ))
    for filetype, value in var_estatisticssize.items():
            if filetype != "Total":
                var_estatisticsreadable[filetype] = func_convertsize(value)
def func_writecsvfile():
    with open("Analysis_report.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["File Name", "Size"])
        for name, size in var_top5biggestarquives:
            writer.writerow([name, func_convertsize(size)])
def func_reportdata():
    print (f"Amount of files:{var_estatistics}")
    print (f"Amount of files (Size):{var_estatisticsreadable}")
    print (f"The biggest files are:")
    for name, size in var_top5biggestarquives:
        print(name, "-", func_convertsize(size))

func_initiateanalysis()
func_calculatetotals()

var_biggestarquives = sorted(var_biggestarquives, key=lambda item: item[1], reverse=True)
var_top5biggestarquives = var_biggestarquives[:5]

func_writecsvfile()
func_reportdata()
