"""look for X-DSPAM-Confidence: in mbox-short.txt
and calculate the average of those values without using sum()"""

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("AHH damn")
    quit()
count = 0
sith = 0.0
for line in fname:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count += 1
    sith += float(line[20:])
    ave = sith / count
print("Average spam confidence:", ave)
