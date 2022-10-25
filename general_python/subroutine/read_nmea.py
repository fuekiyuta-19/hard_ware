from subroutine import conversion

def read_GGA_VTG(DATA):
    X = []
    Y = []
    V = []
    key1 = '$GPGGA'
    key2 = '$GPVTG'
    for i in range(len(DATA)):
        sumple = DATA[i]
        if DATA[i][0] == key1 and DATA[i][6] == '4':
            X.append(conversion.convert(float(DATA[i][2]), float(DATA[i][4]))[0])
            Y.append(conversion.convert(float(DATA[i][2]), float(DATA[i][4]))[1])
        
        elif DATA[i][0] == key2:
            V.append(float(DATA[i][7]))

        else:
            pass
        
    return X, Y, V