#!/bin/bash
set +x

CSV_SKAT=$1
CSV_NORDNET=$2
CSV_BRUGBAR=$3
CSV_NORDNET_UTF8=nordnet_utf8.csv

# Echo parameters:
echo "----------- Aktiesparekonto ----------"
echo "Skats positiv liste:    $CSV_SKAT"
echo "Parirliste fra Nordnet: $CSV_NORDNET"
echo "Fil med brugbare papirer: $CSV_BRUGBAR"

# Konverter til UTF-8. Kræves af det efterfølgende
iconv -f UTF-16LE -t UTF-8 $CSV_NORDNET > $CSV_NORDNET_UTF8

# Tag overskriften med direkte
head -n 1 $CSV_NORDNET_UTF8  > $CSV_BRUGBAR

# Find elementer
awk -F',' '{print $2}' "$CSV_SKAT" | while IFS= read -r value; do
    if [ ${#value} -gt 10 ]; then
        echo "Searching for: $value in file $CSV_NORDNET_UTF8" 
        grep -aF "$value" "$CSV_NORDNET_UTF8" >> $CSV_BRUGBAR
    fi
done
rm $CSV_NORDNET_UTF8
echo "====================================================================="
echo "    Regneark med brugbare papirer kan nu importeres: $CSV_BRUGBAR"
echo "====================================================================="
