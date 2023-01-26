# -*- coding: utf-8 -*-
"""Python8_Protein_Composition

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18P3qt_WVFanVou4LRhYYnBOgb6FZrF_1
"""

# Taking DNA sequence as input
dna=input("Enter a sequence: ")

# Calculating length of sequence
length = len(dna)
print(length)
dna=dna.upper()
print(dna)

# Counting A, T, G, C
g=dna.count('G')
c=dna.count('C')
a=dna.count('A')
t=dna.count('T')

# Printing the results
print("Length= ",length,"G= ",g,"C= ",c,"A= ",a,"T= ",t)

nucleotides=["A", "T", "G", "C"]
for i in nucleotides :
  print(i)

# Lets say you have a protein sequence
# Protein has 20 amino acids-
# You cannot be writing 20 count statements - that's not programming
# We combine for loop with the function in string

# Create a list of amino acids
amino_acids = ["G","A","V","L","I","P","M","F","W","Y","S","T","N","Q","C","D","E","K","R","H"]

# Take protein sequence as input
protein=input("Input protein sequence: ")
print(protein)

# Use for loops to access individual amino acids and query the system for percentage composition
for i in amino_acids :
  count1=protein.count(i)              
  percent=(count1/len(protein))*100

# In order to print only to the first decimal place, we use the following command:
# NOTICE {0:.1f} is to 1 decimal place, {0:.2f} to 2 decimal place, {0:.3f} to 3 decimal place, and so on.
  print(i, "{0:.1f}".format(percent),"%")