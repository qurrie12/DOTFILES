import subprocess

result_volume = subprocess.run(['pamixer', '--get-volume'], stdout=subprocess.PIPE).stdout.strip().decode("UTF-8")
result_muted = subprocess.run(['pamixer', '--get-mute'], stdout=subprocess.PIPE).stdout.strip().decode("UTF-8")

if result_muted == "false":
    print(result_volume + "%")
else:
    print("MUTED")
