# six positive integers are given, denoting the number of couples within a population with the following genotypes:
# 1 AA-AA
# 2 AA-Aa
# 3 AA-aa
# 4 Aa-Aa 
#5 Aa-aa
#6 aa-aa

# E(X) = ∑k*Pr(X=k)

def calculating_expected_offspring(population):
    """
    k is simply the population of each phenotype. Pr(X=k) can be calculated by evaluating the mean.
    """

    xi = list(map(int, population.split()))
    total=len(xi)
    probabilities=[]
    sigma = []
    for i in xi: 
        probabilities.append(i*i/total)

    return sum(probabilities)

population = '18997 17892 16058 17375 18284 18475'
print(calculating_expected_offspring(population))


