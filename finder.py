import os
to_find = input('Enter file or directory to find: ')
partation2searchin = input('Enter partation letter to search in: ').upper()
findings = []
for dirpath,direnames,filenames in os.walk(f'{partation2searchin}:\\'):
    if to_find in filenames or to_find in direnames:
        findings.append(dirpath)
for finding in findings: print(finding)
