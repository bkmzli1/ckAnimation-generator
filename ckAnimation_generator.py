#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    ckAnimation generator by Felucca24.
    https://github.com/Felucca24/ckAnimation-generator
"""

import ckAnimation_algorithms as aa
import time

fileExt = ".ckAnimation"
description = "File generated by ckAnimation_generator\nhttps://github.com/Felucca24/ckAnimation-generator"
filepath = ""
filename = ""
selAlgName = ""

bloodyPath = "C:\\Program Files (x86)\\KeyDominator2\\KeyDominator2\\Data\\RES\\English\\SLED\\NumberPadAtRight\\"
bloodySettingsPath = "C:\\Program Files (x86)\\KeyDominator2\\KeyDominator2\\UserLog\\B857Rcir_395CE287\\English\\Settings\SLED\\NumberPadAtRight\\Setting.ini"

print("Enter file name. (Skip - standard algorithm name)")
filepath = input("Filename > ")


print("\nSelect the algorithm:")
_i = 0
for alg in aa._registeredAlgorithms:
    print(str(_i) + " - " + alg.getName(alg) )
    _i += 1

algNum = 0
try:
    algNum = int(input("number > "))
except:
    algNum = 0


activeAlgorithm = aa._registeredAlgorithms[int(algNum)]()
print("")
activeAlgorithm.start()

selAlgName = activeAlgorithm.getName()

if len(filepath) == 0:
    filepath = activeAlgorithm.getName()
if filepath[-len(fileExt):] != fileExt:
    filepath += fileExt

frameStrings = []
print("Generating strings...")
for frame in activeAlgorithm.frames:
    num = frame.number+1
    tmpstr =   "\n    <Frame"+str(num)+">\
                \n        <ColorPicture>"

    for button in frame.buttons:
        tmpstr += button.rgb2hex()
        if button.number != aa.KEY_COUNT-1:
            tmpstr += ","

    tmpstr +=  "\n        </ColorPicture>\
                \n        <DisplayTime>"+str(frame.displayTime)+"</DisplayTime>\
                \n    </Frame"+str(num)+">"

    frameStrings.append(tmpstr)



startString =  "<Root>\
                \n    <Description>"+description+"</Description>\
                \n    <Time>0</Time>\
                \n    <BackgroundColor>000000</BackgroundColor>\
                \n    <FrameCount>"+str(activeAlgorithm.frameCount-1)+"</FrameCount>"
                
endString =    "\n</Root>"

print("Done.")

f = open(filepath, "w")
f.write(startString)
for i in range(activeAlgorithm.frameCount):
    f.write(frameStrings[i])
f.write(endString)
f.close()

print("File saved.")



print("\nWould you like to install the file just generated? (Enter - skip)")
slot = None
try:
    slot = int(input("Fn + slot > "))
    if slot > 9:
        print("Value is too big!")
        assert(False)
except:
    slot = None



if slot is not None:
    array = []
    filename = filepath.split("\\")[-1]
    print("Setting \""+filename+"\" to slot Fn+"+str(slot))


    fileToCopy = open(filepath, "rb").read()

    open(bloodyPath+filename, "wb+").write(fileToCopy)


    with open(bloodySettingsPath, "r") as file:
        array = [row for row in file]
        array[slot+1] = "FnKey"+ str(slot) + "=" + filename + "\n"

    with open(bloodySettingsPath, "w") as file:
        file.writelines(array)

###################

print("Closing.")
time.sleep(3)