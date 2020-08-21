#!/bin/bash
# Created by: Ewerton Lima
# this script's job is to sort onetab exported
# links by domain and remove duplicates

# obtaining domains to create groups

touch temp sorted_tabs;
grep  -e http $1 | grep -v '127.0' | grep -v 'chrome:' | grep -v 'file:' |  awk -F '[/]' '{print $2$3}' > domains;
# Remove duplicates
vim -c ':sort u | wq' domains;
# Remove "notifications" on page title
vim -c ':%s/([0-9][0-9])//ge | wq' "$1";
vim -c ':%s/([0-9])//ge | wq' "$1";
vim -c ':sort u | wq' "$1";

while read line; do
  # Filter by domain
  grep "$line" "$1" > temp &&
  # Write filtered webpages on sorted_tabs
  cat temp >> sorted_tabs &&
  echo '' >> sorted_tabs;
done < domains

rm domains temp
