#!/bin/bash

# exit if any command returns code other than 0
set -e
which mpv >/dev/null || echo "please install mpv and yt-dlp"

# playlists files or directories 
playlists=($(ls $HOME/playlists/))
num=$((${#playlists[@]} - 1))

if [ ${#playlists[@]} -eq 1 ]; then
  echo "0 ${playlists[0]}"
else 
  for f in $(seq 0 $num)
  do
    printf "%d %s\n" $f ${playlists[$f]}
  done
fi

printf "Select which playlist to play: "
read selection

[ $selection -gt ${#playlists[@]} ] && exit 1

# to show video remove the --no-video flag from the command below
file=${playlists[$selection]}
while read f; do mpv --no-video "$f"; done < "$HOME/playlists/$file"
