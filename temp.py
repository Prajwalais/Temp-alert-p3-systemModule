import sys

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    temp = int(sys.argv[1])
else:
    script_name = sys.argv[0]
    temp = 100

print(f"script_name: {script_name}\nTemperature: {temp}")

if temp < 15:
    print("Cold")
elif temp < 30:
    print("Normal")
else:
    print("Hot")
