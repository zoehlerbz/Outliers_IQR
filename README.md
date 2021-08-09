# Outliers_IQR
IQR method of identifying outliers

Some observations within a set of data may fall outside the general scope of the other observations. Such observations are called outliers. 

We can use the IQR method of identifying outliers to set up a “fence” outside of Q1 and Q3. Any values that fall outside of this fence are considered outliers. To build this fence we take 1.5 times the IQR and then subtract this value from Q1 and add this value to Q3. This gives us the minimum and maximum fence posts that we compare each observation to. Any observations that are more than 1.5 IQR below Q1 or more than 1.5 IQR above Q3 are considered outliers. This is the method that Minitab Express uses to identify outliers by default (PennState Eberly College of Science).
