import pandas as pd
from pyteomics.mass import mass


def protein_fragment():
    a = 'MGSGHHHHHHHHSDSEVNQEAKPEVKPEVKPETHINMLGRMPNLMLMAKESLYSQLPMD'
    seq = []
    mass_a = []
    for i in range(0, len(a)+1):
        for j in range(i+1, len(a)+1):
            seq.append(a[i:j])
            mass_a.append(mass.fast_mass(a[i:j]))
    b = pd.DataFrame(seq, mass_a)
    return(b)