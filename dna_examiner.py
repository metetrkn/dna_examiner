import csv
import sys


def main():
    # checking if not less than 2 cmd-argument given
    try: 
        len(sys.argv[2])

    except:
        print("Usage: python3 databases/XXX.csv sequences/YYY.txt")
        sys.exit(1)

    
    # checking and prompting user to input 1st of argv as '.csv' and 2nd '.txt' and not more than 3 cmd-argument
    if ".csv" not in sys.argv[1] or ".txt" not in sys.argv[2] or len(sys.argv) != 3:
        print("Usage: python3 databases/XXX.csv sequences/YYY.txt")
        sys.exit(1)

    # reading dna sample to memory
    with open(sys.argv[2]) as file:
        dna = file.read()

    # reading STR samples of people to memory
    with open("databases/large.csv") as f:
        csv_reader = csv.reader(f)

        # STR samples to examina dna
        for row in csv_reader:
            samples = row
            samples = samples[1:]
            break
        
        # database samples of people
        next(csv_reader)
        str_ = [rows for rows in csv_reader]

        # dna sample decoded
        decoded = []
        for sample in samples:
            decoded.append(str(longest_match(dna, sample)))
    
        # checker if no math
        checker = 0
        
        # checking if decoded and databases math
        for i in str_:
            if i[1:] == decoded:
                print(i[0])
                checker+=1

        # if no match with examinated dna sample and databases    
        if checker == 0:
            print("No match")
            
        return

        




def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

    
if __name__ == "__main__":
    main()
