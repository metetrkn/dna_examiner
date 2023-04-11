# DNA Matching

    This repository contains a Python script that analyzes DNA sequences to identify a person based on their DNA. The script reads a CSV file containing known DNA sequences and a text file containing a DNA sample to be analyzed. It then looks for the longest consecutive sequence of short tandem repeats (STRs) in the DNA sample and compares it to the known DNA sequences to find a match.

## Usage

    Clone this repository.
    Ensure that you have Python 3.x installed.
    Run the Python script with the appropriate command-line arguments. The first argument should be the CSV file containing the known DNA sequences, and the second argument should be the text file containing the DNA sample to be analyzed.

    bash

    python3 dna.py databases/XXX.csv sequences/YYY.txt

## Input Files

    databases/XXX.csv: A CSV file containing known DNA sequences. Each row represents an individual, and each column represents an STR.
    sequences/YYY.txt: A text file containing a DNA sample to be analyzed.

## Output

The script outputs the name of the individual whose DNA matches the analyzed sample. If there is no match, the script outputs "No match".

## Dependencies

    Python 3.x

## Contributing

    Contributions are welcome. Please open an issue or submit a pull request to suggest changes or improvements.


## Credits

    Mete Turkan
    linkedIn : linkedin.com/in/mete-turkan
    Inst : m_trkn46
