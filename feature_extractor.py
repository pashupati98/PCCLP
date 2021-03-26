import pandas as pd
import numpy as np

def fearure_extractor(rus):
    
    # defining chemical spaces for the backbone
    CH2 = []
    CO = []
    NH = []
    DB = []
    O = []

    # defining chemical spaces for the backbone
    CHOH = []
    CHCH3 = []
    CHCL = []
    CHF = []
    C6H4 = []
    CF2 = []
    CHCN = []
    CCH32 =[]
    CCH3D = []

    ch2 = 0
    choh = 0
    chch3 = 0
    chcl = 0
    chf = 0
    c6h4 = 0
    cf2 = 0
    o =0
    chcn = 0
    cch3d = 0
    cch32 = 0
    co = 0
    nh = 0
    db = 0
    
    for ru in rus:
        print(ru)
        feature = ru.split('_')
        print(feature)
        for group in feature:
            if group == 'CH2':
                ch2 = ch2 + 1
            if group == 'CH(OH)':
                choh = choh + 1
            if group == 'CH(Cl)':
                chcl = chcl + 1
            if group == 'CH(F)':
                chf = chf + 1
            if group == 'CH(CH3)':
                chch3 = chch3 + 1
            if group == 'CF2':
                cf2 = cf2 + 1
            if group == 'O':
                o = o + 1
            if group == 'CH(CN)':
                chcn = chcn + 1
            if group == 'CH(CH3)2':
                cch32 = cch32 + 1
            if group == 'CO':
                co = co + 1
            if group == 'NH':
                nh = nh + 1
            if group == '(=)':
                db = db + 1
            if group == 'C6H4':
                c6h4 = c6h4 + 1
            if group == 'C(CH3)':
                cch3d = cch3d + 1
            else:
                pass
        CH2.append(ch2)
        CHOH.append(choh)
        CHCH3.append(chch3)
        CHCL.append(chcl)
        CHF.append(chf)
        CF2.append(cf2)
        O.append(o)
        CHCN.append(chcn)
        CCH32.append(cch32)
        CO.append(co)
        NH.append(nh)
        DB.append(db)
        C6H4.append(c6h4)
        CCH3D.append(cch3d)
        ch2 = 0
        choh = 0
        chch3 = 0
        chcl = 0
        chf = 0
        c6h4 = 0
        cf2 = 0
        o =0
        chcn = 0
        cch32 = 0
        co = 0
        nh = 0
        db = 0

return list(CH2[0], CO[0], NH[0], DB[0], O[0], CHOH[0], CHCH3[0], CHCL[0], CHF[0], C6H4[0], CF2[0], CHCN[0], CCH32[0], CCH3D[0])
    