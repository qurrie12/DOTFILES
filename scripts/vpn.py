import subprocess

result = subprocess.run(['expressvpn', 'status'], stdout=subprocess.PIPE)
result = result.stdout.strip().decode("UTF-8")

if result == "Not connected":
    print("")
else:
    result = result.split(" ")
    print(result[2].upper().splitlines()[0])
