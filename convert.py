inp = open("styles.css","r")
outp = open("converted.css","w")
for line in inp:
    line = list(line)
    i = 0
    length = len(line)
    while i < length:
        if line[i] == "{" or line[i] == ";":
            line.insert(i+1,'\n\t')
            i+=1;length+=1
        elif line[i] == "}":
            line.insert(i+1,'\n\n')
            i+=1;length+=1
        i = i+1
    line = ''.join(line)
    line = str(line)
    outp.write(line)
outp.close()
inp.close()
