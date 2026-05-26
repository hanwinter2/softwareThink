import os
def scanFile(base, folder1, folder2):
    scannedFolder1 = os.scandir(base + folder1)
    scannedFolder2 = os.scandir(base + folder2)

    tupleSet1 = set()
    tupleSet2 = set()

    for i in scannedFolder1:
        tupleSet1.add((i.name, i.stat().st_size))
    
    for i in scannedFolder2:
        tupleSet2.add((i.name, i.stat().st_size))
    
    if len(tupleSet1) != len(tupleSet2):
        return False

    if tupleSet1 != tupleSet2:
        return False
    
    for name, size in tupleSet1:
            
        a = base + folder1
        b = base + folder2

        with open(a + "/" + name, "rb") as f1, open(b + "/" + name, "rb") as f2:
            if f1.read() != f2.read():
                return False
    
    return True
        

base = input()

folder1 = input()
folder2 = input()

if scanFile(base, folder1, folder2):
    print("같습니다")
else:
    print("다릅니다")