import io
import csv
with open('sequences.fasta', 'r') as f:
    file = io.StringIO(f.read())
print('Read file:')
for i in file.readlines():
    print(i.strip())
file.seek(0)
newfile = io.StringIO()
for line in file.readlines():
    if line.startswith('>'):
        newfile.write(line)
    else:
        newfile.write(line.lstrip('X'))
newfile.seek(0)

print('Read new file:')
for i in newfile.readlines():
    print(i.strip() + ' length:', len(i))
newfile.seek(0)
with open('sequences_processed.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in newfile.readlines():
        writer.writerow([i.strip()])


with open('sequences_processed.fasta', 'w') as f:
    f.write(newfile.getvalue())
