import subprocess
import os

# get current song's data
metadata = subprocess.run(['playerctl', 'metadata'], stdout=subprocess.PIPE).stdout.strip().decode('UTF-8').split()
# remove all instances of the player's name
metadata = [item for item in metadata if item != metadata[0]]

try:
    # artist's name is next to this tag, so we have to add 1 to the index
    artist_index = metadata.index("xesam:artist") + 1
except ValueError:   # ValueError if music is not playing
    quit()

title_index = metadata.index("xesam:title") + 1

output = ""
# read as long as we dont hit the next tag ('xesam' in the first 5 characters)
while metadata[artist_index][:5] != "xesam":
    output += metadata[artist_index] + " "
    artist_index += 1

output += "- "
while metadata[title_index][:5] != "xesam":
    output += metadata[title_index] + " "
    title_index += 1

print(output)
