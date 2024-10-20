# operations.py

def readName(str1):
    with open("text.txt") as file:
        str1.append(file.read())
    print("The read file:", str1)


def loadMatrix(str1, mat):
    mat.extend(str1[0].strip().split('\n'))


def convertToColumnMajor(mat):
    temp = []
    n = max([len(i) for i in mat])
    for i in range(n):
        res = ""
        for j in range(len(mat)):
            try:
                res += mat[j][i]
            except Exception:
                res += " "
        temp.append(res.rstrip())
    mat.clear()
    mat.extend(temp)


def calculateCharacterLength(mat):
    res = sum([len(i) for i in mat])
    print("Total character length:", res)


def storeListAsString(mat):
    with open("output.txt", "wt") as file:
        for i in mat:
            file.write(i.strip())
