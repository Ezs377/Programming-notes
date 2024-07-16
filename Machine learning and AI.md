--- 

### Linear regression:  
Linear regression is predicting the value of a variable based on another variable. In this case the predicted variable is the dependent variable, the independent variable is used to predict the dependent variable.  

Linear regression was taught in 211. 

Standard deviation: Is a measure of the variability (spread) of data. 

Standard error: It is the estimate of variability between samples taken. It is the standard deviation of the sample divided by the square root of the amount of samples, i.e.  
![[Pasted image 20240705162937.png]]  
Essentially how likely the population (overall) mean is different to the sample mean. The sample means are typically sampled from the same population, and the new population mean would depend on the standard error.

**Standard deviation:** The possible differences between SAMPLES from the sample mean. Standard deviation is calculated on existing data samples and a normal distribution graph of data samples (bell shaped curve) can be used to express standard error, and if the data follows a normal distribution we can use the empirical rule, where 
around 68% of values are within the range of the first single standard deviation of the mean,
around 95% of values are within the range of the first two standard deviations of the mean, 
around 99.7% of values are within the range of the first three standard deviations of the mean. E.g. 
![[Pasted image 20240715091746.png]]  
Note that standard deviation is the chance that a sample will be different from the mean. Depending on our dataset the mean could either be the sample mean or the population mean, depends on where we take out data from. If we take data from everything in the chosen population then it is population data, if we take a portion of the population then it is sample data.

**Standard error:** Tells us our accurately our data represents the entire population. Whereas standard deviation tells us how each sample differs from the mean, standard error tells us how accurate our samples chosen are to the population. This is otherwise known as probability as we cannot say for sure how our data samples represent the entire population.  

Generally speaking the more samples we use for analysis the lower the standard error. Lower standard error is better as it means our samples are more accurate to the population.  

Also standard deviation is a descriptive statistic and we can calculate it using our data samples, while standard error is a inferential statistic and only estimates. 

### Statistical learning (from The Elements of Statistical Learning Second Edition):  
###### Introduction:  
Supervised learning: Outcome variables are used to guide the learning process.
Unsupervised learning: Observe features of data only and no outcome.  

Example: Develop a spam detector that can filter out spam messages based on the email text contents. For a given email dataset, available true outcomes are either *email* or *spam*. The outcome variable is email or spam, and hence it is a supervised learning problem, and also known as a classification problem. 
![[Pasted image 20240716120552.png]]
The table shows the biggest average differences between emails that are separated as spam and email (dataset).  






 
