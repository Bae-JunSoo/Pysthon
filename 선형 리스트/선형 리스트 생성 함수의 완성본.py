katok = []

def add_data(friend) :

    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

i = 0
while i < 6:
    name = input("카톡친구 입력==>")
    add_data(name)
    i = i + 1

    print(katok)
