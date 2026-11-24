# given a sample population k,m,n positive intergers.
# k individuals are dominant homozygous,
# m are hetero
# n are recessive

#return prob 2 randomly selected will return a dominant allele, ignoring genders.




# inputting values:
k = 18
m = 23
n = 26

total_sample = k+m+n

# 1-p, so we will find p of being ONLY recessive. for all calculations below

# probability of individuals being recessive! (if from recessive)
p_recessive_r = (n/total_sample)*((n-1)/(total_sample-1))

# 1-p, probability of indivuduals being recessive if BOTH hetero:
p_recessive_hethet = (m / total_sample) * ((m - 1) / (total_sample - 1)) * 0.25
# 0.25 as per mendel square, not all offspring are actually recessive. 


# one het one recessive: 
p_recessive_hetr = (m/total_sample)*((n)/(total_sample-1)) *0.5
p_recessive_rhet = (n/total_sample)*((m)/(total_sample-1)) *0.5
#dominant and dominant:
p_recessive_RR = 0
# dominant and recessive:
p_recessive_hetR = 0
p_recessive_Rhet = 0
# dominant and hetero:
p_recessive_hetR = 0
p_recessive_Rhet = 0


total_recessive = p_recessive_r + p_recessive_hethet + p_recessive_hetr + p_recessive_rhet


#now doing 1-p, to find the chance of hetero in one of the offspring:
print (1-total_recessive)