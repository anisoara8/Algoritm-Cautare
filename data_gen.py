import random
def generator():
    global ZZ, LL, AA, S, JJ, NNN
    ZZ = str(random.randint(1, 31))
    if len(ZZ) == 1:
        ZZ= '0' +ZZ
    LL = str(random.randint(1, 12))
    if len(LL) ==1:
        LL = '0'+LL
    AA = str(random.randint(1900, 2099))
    if int(AA) in range(1900, 1999):
        S = random.choice(['1', '2'])
    elif int(AA) in range(2000, 2099):
        S = random.choice(['5', '6'])
    JJ = str(random.choice([random.randint(1, 46), 51, 52]))
    if len(JJ) == 1:
        JJ = '0' + JJ
    NNN = str(random.randint(0, 999))
    if len(NNN) == 1:
        NNN = '00'+NNN
    elif len(NNN)==2:
        NNN = '0' + NNN
    AA = str(int(AA) % 100)
    if len(AA) == 1:
        AA = AA + '0'
    cn = S+AA+LL+ZZ+JJ+NNN+'0'
    suma = 0
    z = 0
    for j in '279146358279':
        suma = suma + int(j)*int(cn[z])
        z = z + 1
    rest = suma % 11
    if rest == 10:
        C = '1'
    else:
        C = str(rest)

    CNP = S+AA+LL+ZZ+JJ+NNN+C
    return CNP

if __name__== "__main__":
    with open('cod.txt','r') as f:
        f1= f.read()


    with open('date_generate.txt','w')as g:
        for i in range(0,1000):
            s=generator()
            g.write(s)
            g.write('\n')


