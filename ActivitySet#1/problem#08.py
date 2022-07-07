# Files

filename = "dataset/mbox-short.txt"
fname = input("Enter file name: ")
fh = open(fname)
count = 0
flt_tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos=line.find(':')
    flt = float(line[pos + 1: ])
    flt_tot = flt_tot + flt
    count = count + 1

print('Average spam confidence:', flt_tot/count)
