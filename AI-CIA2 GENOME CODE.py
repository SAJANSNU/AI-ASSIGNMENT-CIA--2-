#!/usr/bin/env python
# coding: utf-8

# In[5]:


def calculate_gene_score(gene1, gene2):
    score = 0
    
    
    if len(gene1) != len(gene2):
        return "Gene codes have different lengths. Cannot calculate score."
    
    
    for i in range(len(gene1)):
        if gene1[i] == gene2[i]:
            score += 5
        elif gene1[i] == '-' or gene2[i] == '-':
            score += 1
        else:
            score -= 4
    
    return score

gene1=input("Enter the gene 1 :")
gene2=input("Enter the gene 2 :")
score = calculate_gene_score(gene1, gene2)

print("Score of the matching of genes (+5 if matches, -4 if doesnt match and -1 if missing):", score)


# In[ ]:





# In[ ]:




