# calculate_with_mordred
Calculates descriptors for an array of molecules in the SMILES format using library Mordred (https://doi.org/10.1186/s13321-018-0258-y)

# Usage

python3.8 mordred_descriptors.py --i ./smiles.csv --o ./output

the input CSV should contain a single column containing the molecules in SMILES format



# Mordred reference:

Moriwaki H, Tian Y-S, Kawashita N, Takagi T (2018) Mordred: a molecular descriptor calculator. Journal of Cheminformatics 10:4 . doi: 10.1186/s13321-018-0258-y
