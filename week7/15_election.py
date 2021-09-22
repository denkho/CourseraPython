fin = open("input.txt", "r", encoding="utf-8")
candidates = fin.readlines()
fin.close()

cands_count = dict()

for candidate in candidates:
    cands_count[candidate.strip()] = cands_count.get(candidate.strip(), 0) + 1

first_candidate = sorted(cands_count, key=cands_count.get, reverse=True)[0]

fout = open("output.txt", "w", encoding="utf-8")

if (cands_count[first_candidate] / len(candidates)) * 100 > 50:
    fout.write(first_candidate)
else:
    fout.write(first_candidate + "\n")
    fout.write(sorted(cands_count, key=cands_count.get, reverse=True)[1])
fout.close()
