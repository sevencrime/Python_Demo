
import subprocess

line = subprocess.getstatusoutput("adb devices")

# line = line[1]
print(type(line))
print(line)
print(len(line))
str1 = line[1]
print(type(str1))
print(str1)

