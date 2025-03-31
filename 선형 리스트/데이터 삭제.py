katok = ["다현","정연","쯔위","미나","사나","지효"]
print(katok)

katok.append(None)
print(katok)

katok[6] = "모모"
print(katok)

katok[4] = None
print(katok)

katok[4] = katok[5]
print(katok)

katok[5] = None
print(katok)

katok[5] = katok[6]
print(katok)

katok[6] = None
print(katok)

del(katok[6])
print(katok)
