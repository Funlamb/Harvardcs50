import csv
import sys

# data.csv

# name,AGATC,AATG,TATC
# Alice,2,8,3
# Bob,4,1,5
# Charlie,3,2,5

# sequence.txt
# AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG

def main():
    # Ensure correct usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
    
    suspects = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        # top = reader.fieldnames
        # print(top)
        for row in reader:
            suspects.append(row)

    for sus in suspects:
        print(sus)
        for item in sus:
            if item != "name":
                sus[item] = int(sus[item])
            # print(sus[item])
            # for key, value in item:
            #     print(key)
            #     print(value)
    print(suspects)

if __name__ == "__main__":
    main()