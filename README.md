# AI-ASSIGNMENT-CIA--2-

## ASSIGNMENT - 1
CONSISTING OF ALL SEARCH ALGORITHMS AND CODE AND OUTPUT OF ALL THE PROGRAMS
## ASSIGNMENT - 2(IMPLEMENATION USING PYTHON)
CONSISTING OF PYTHON CODE WHICH TAKES IN TWO GENOME TYPES AND COMPARES AND GETS THE SCORE.

# Gene Score Calculation
## ALGORITHM: 

This code calculates the similarity score between two genetic sequences represented as strings, gene1 and gene2. The score is based on specific rules:

If the genes have different lengths, the function returns an error message: "Gene codes have different lengths. Cannot calculate score."

If the corresponding characters in both genes match, a score of +5 is added for each matching character.

If either gene1 or gene2 has a dash '-' at the same position, a score of -1 is added for each dash.

If none of the above conditions are met, a score of -4 is subtracted for each mismatched character.

