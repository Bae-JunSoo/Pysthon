katok[지정위치] = None

for 현재위치 in range(지정위치+1, 마지막위치+1) :
    katok[현재위치-1] = katok[현재위치]
    katok[현재위치] = None

del(katok[마지막위치])
