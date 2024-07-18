strs = ["flower","flow","flight"]
res = ''
lens = []
count = 0
let = strs[1][1]
for i in strs:
    lens.append(len(i))

for k in range(min(lens)):
    while True:
        for word in strs:
            now_let = word[k]
            if now_let == let:
                count += 1
            if count == len(strs):
                try:
                    res += now_let
                    let = strs[k+1]
                    break
                except:
                    break

print(res)