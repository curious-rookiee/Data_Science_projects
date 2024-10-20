# main.py

from operations import readName, loadMatrix, convertToColumnMajor, calculateCharacterLength, storeListAsString

def main():
    str1 = []
    mat = []
    
    readName(str1)  # Reading the file
    loadMatrix(str1, mat)  # Loading the matrix from the string
    print("Loaded matrix:", mat)

    convertToColumnMajor(mat)  # Converting to column-major format
    print("Column-major matrix:", mat)

    calculateCharacterLength(mat)  # Calculating the total character length
    storeListAsString(mat)  # Storing the result in a file

if __name__ == "__main__":
    main()
