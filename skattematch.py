import sys
import os
import csv
import subprocess

def main():
    # Get input parameters
    CSV_SKAT = sys.argv[1]
    CSV_NORDNET = sys.argv[2]
    CSV_BRUGBAR = sys.argv[3]
    CSV_NORDNET_UTF8 = 'nordnet_utf8.csv'

    # Echo parameters
    print("----------- Aktiesparekonto ----------")
    print(f"Skats positiv liste:    {CSV_SKAT}")
    print(f"Parirliste fra Nordnet: {CSV_NORDNET}")
    print(f"Fil med brugbare papirer: {CSV_BRUGBAR}")

    # Convert to UTF-8. Required by the following steps
    with open(CSV_NORDNET, 'rb') as source_file:
        data = source_file.read()
    data_utf8 = data.decode('utf-16le').encode('utf-8')
    with open(CSV_NORDNET_UTF8, 'wb') as dest_file:
        dest_file.write(data_utf8)

    # Take header directly
    with open(CSV_NORDNET_UTF8, 'r', encoding='utf-8') as source_file:
        header = source_file.readline()
    with open(CSV_BRUGBAR, 'w', encoding='utf-8') as dest_file:
        dest_file.write(header)

    # Find elements
    with open(CSV_SKAT, 'r', encoding='windows-1252') as skat_file:
        reader = csv.reader(skat_file)
        for row in reader:
            value = row[1]
            if len(value) > 10:
                print(f"Searching for: {value} in file {CSV_NORDNET_UTF8}")
                with open(CSV_NORDNET_UTF8, 'r', encoding='utf-8') as nordnet_file:
                    for nordnet_row in nordnet_file:
                        if value in nordnet_row:
                            with open(CSV_BRUGBAR, 'a', encoding='utf-8') as brugbar_file:
                                brugbar_file.write(nordnet_row)

    # Remove temporary UTF-8 file
    os.remove(CSV_NORDNET_UTF8)

    print("=====================================================================")
    print(f"    Regneark med brugbare papirer kan nu importeres: {CSV_BRUGBAR}")
    print("=====================================================================")

if __name__ == '__main__':
    main()
