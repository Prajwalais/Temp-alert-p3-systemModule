import sys

if len(sys.argv)==2:
  script_name=sys.argv[0]
  temp=float(sys.argv[1])
else:
  script_name=sys.argv[0]
  temp=100
print(f"script_name: {script_name}\nTempeture: {temp}")

if temp <15:
  print(f"Cold")

elif temp <30:
  print(f"normal")
  else
  print(f"Hot")
