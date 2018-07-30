# read data by importing from csv file
#import numpy as np
#
#age = np.loadtxt("participants.tsv", skiprows=1, usecols=3)
#
#mean_age = sum(age)/len(age)
#
#np.savetxt("demeaned_age.txt", age-mean_age)
#
#print("done!")


# read data directly from command line
import sys
import numpy as np

age = np.loadtxt(sys.argv[1], skiprows=1, usecols=3)

mean_age = sum(age)/len(age)

np.savetxt("demeaned_" + sys.argv[1], age-mean_age)

assert mean_age < 100
assert mean_age > 10

print("done!")
