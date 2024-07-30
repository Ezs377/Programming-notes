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

### Statistical learning (from The Elements of Statistical Learning Second Edition) (unfinished notes):  
#### Introduction:  
Supervised learning: Outcome variables are used to guide the learning process.
Unsupervised learning: Observe features of data only and no outcome, instead finding how the data is organized or clustered.

Example: Develop a spam detector that can filter out spam messages based on the email text contents. For a given email dataset, available true outcomes are either *email* or *spam*. The outcome variable is email or spam, and hence it is a supervised learning problem, and also known as a classification problem. 
![[Pasted image 20240716120552.png]]
The table shows the biggest average differences between emails that are separated as spam and email (dataset).  

Using supervised learning we can set the example outcome rule based on probability or frequency, e.g.  
![[Pasted image 20240716160554.png]]  

Essentially having inputs makes it supervised learning.

Qualitative variables are typically represented numerically by codes. The easiest to label is when we only have 2 classes/categories, e.g. Success and Failure. These classes can be represented as a binary value 0 and 1 instead. Numeric values used to code 2 categories are sometimes referred to as targets.

When we have more than 2 categories, we have alternative codings. A common one is using dummy variables. A K level qualitative variable is represented by a vector of K binary variables (or bits) of which only one is 'on' at a time. 

An input variable is commonly denoted as X. If X is a vector, then its components are denoted as X<sub>j</sub>
for every jth component. Quantitative outputs are denoted as Y, and qualitative outputs are denoted as G. 

Capital letters X, Y, G are used to refer to generic aspects of a variable. 
Lowercase letters x, y, g are sued to refer to observed values, e.g. The ith observed value of X is referred to as x<sub>i</sub>
Matrices are represented by bold capitals, e.g. A set of N input p-vectors x<sub>i</sub> where i = 1, 2... N would be represented as an N x p matrix **X**
Vectors are typically not bold unless they have N components. All vectors are assumed to be column vectors, the ith row of **X** is x<sub>i</sub><sup>T</sup> which is the vector transpose of x<sub>i</sub>. 

The basic learning task: Given the value of an input vector X, make a good prediction on of the output Y, where the prediction is referred to as Ŷ (Y with hat). For categorical outputs G the prediction should be Ĝ and should use the same set of categories given which is denoted as
![[Pasted image 20240721125323.png]]
(can't find character for this so it will be called ɠ

For a 2 class ɠ (i.e. Two categories) one approach is to denote the binary coded target as Y and then treat it as a quantitative output. The predictions Ŷ will be somewhere between \[0, 1] and then assign Ĝ to a class label based on whether ŷ is more pr less than 0.5, e.g. If less than 0.5 then it is success, if more than 0.5 then it is failure. 

The training data is comprised of a set of measurements (x<sub>i</sub>, y<sub>i</sub>) or (x<sub>i</sub>, g<sub>i</sub>) where i = 1, 2... N which will be used to construct the prediction rule.  

#### Approaches to prediction:  
There are 2 simple but powerful prediction methods: Least squares and Nearest neighbors. 

###### Least squares:  
**The linear model:**  
Develops a linear model. For a given input of X<sup>T</sup> = (X<sub>1</sub>, X<sub>2</sub>... X<sub>p</sub>) We predict the output Y to be:  
![[Pasted image 20240721224247.png]]
Where B̂<sub>0</sub> = Y intercept of the linear model, also known as bias in machine learning. Typically this model is more easily written by including a constant of value 1 in X, include B̂ in the vector of coefficients B (note B is beta symbol but can't find beta with hat symbol) and then write the model in vector form as an inner product:
![[Pasted image 20240721225022.png]]  
Where X<sup>T</sup> denotes a vector or matrix transpose (X being a column vector). We are modelling a single output so Ŷ is scalar; Generally Ŷ is typically a K vector, then B would be a p x K matrix of coefficients.  

In a (p + 1)-dimensional input-output space (whatever that is), (X, Ŷ) represents a hyperplane (a subspace that is one dimension lower than the space it is in, e.g. A 2D line is a hyperplane in 3D space). If the 1 constant is included in X then the hyperplane includes the origin is a subspace, otherwise it is an affine set (where any two points in the set will make a line that passes through the same set) that intersects the Y axis at (0, B̂<sub>0</sub>). We also assume the intercept B̂<sub>0</sub> is included in B̂.

Over p-dimensional space, f(X) = X<sup>T</sup>B is linear, and the gradient f'(X) = B is a vector in input space that points to the steepest hill. 

**Least squares method:**
We can use least squares to fit training data over this model. In this method we pick the coefficients of B to minimize the residual sum of squares (RSS),  
![[Pasted image 20240721231616.png]]  
We can convert this equation into matrix notation,  
![[Pasted image 20240722143027.png]]  
Where **X** is an N x p matrix with each row as an input vector, and **y** is an N vector of outputs in the training set. Differentiating with respect to B we get:  
![[Pasted image 20240722143129.png]]  
If **X**<sup>T</sup>**X** is non singular (i.e. Determinant is non-zero) then the unique solution is given by:  
![[Pasted image 20240722143211.png]]  
And the fitted value at the ith input x<sub>i</sub> is ŷ<sub>i</sub> = ŷ(x<sub>i</sub>) = x<sub>i</sub><sup>T</sup>B̂. 

Example:  
The following plot is a scatter plot of training data based on a pair of inputs X<sub>1</sub> and X<sub>2</sub>. 
![[Pasted image 20240722143826.png]]  
The output class G has the values BLUE or ORANGE, and is also show in the scatterplot. There are 100 points in each class. The linear regression model was fitted to the data, with Y coded as 0 for BLUE and 1 for ORANGE. The fitted values Ŷ are converted to the fitted class Ĝ by the rule
![[Pasted image 20240722143813.png]]  
The set of real number points classified as ORANGE corresponds to \{x : x<sup>T</sup>B̂ > 0.5} and the decisive boundary that separates ORANGE and BLUE is \{x : x<sup>T</sup>B̂ = 0.5} which is linear in this case.  

Note that in the scatterplot some points are misclassified, i.e. Some BLUE points are in the ORANGE region and etc.  

###### Nearest neighbor model:  
The nearest neighbour method uses observations in the training set T closest in input space to x to form Ŷ. Specifically, the k-nearest neighbour fit for Ŷ is:  
![[Pasted image 20240722144921.png]]  
Where N<sub>k</sub> is the neighborhood of x defined by k closest points x<sub>i</sub> in the training sample. By 'closeness' we mean Euclidean distance, i.e. Distance between two points (the usual way of measuring distance). Essentially we find k observations with x<sub>i</sub>, closest to x in the input space, and average the responses.  

For example, using the same training data in the least squares example, 
![[Pasted image 20240722145215.png]]
Using 15-nearest-neighbour averaging of the binary coded response, we fit a boundary on the plot. Hence Ŷ is the proportion of ORANGE in the neighborhood, and so if we assign ORANGE to Ĝ if Ŷ > 0.5 

(I give up)

### Terms:    
- Predictors/features: Essentially inputs, or independent variables
- Responses: Essentially outputs, or dependent variables
- Qualitative variables: Discrete or categorical variables, not defined by numerical values
- Quantitative variables: Numerical values, able to be counted
- Ordered categorical variables: Ordered categories without usage of numerical values (e.g. Small, medium, large)
- Regression: Predicting quantitative outputs
- Classification: Predicting qualitative outputs
- Target: A numeric code used to encode a class/category
- Bias: The Y intercept of the linear model







 

### 306 notes:
306 notes are derived from 306 slides which I lost track of during lectures hence they're placed here.

#### Intro:  
Pattern recognition is a scientific discipline that focuses on classifying objects into a number of categories/classes. The objects are typically referred to by a generic term "patterns", and classified by using the object's features to fit a category/class. 

An example of pattern recognition is using a machine learning to identify people recorded on camera, the people are objects and the people faces are features. Other features could be person height, race, gender, etc.  

The first step to pattern recognition is to identify measurable qualities (features) that distinguish object samples from each other. 

For example, with this set of images,  
![[Pasted image 20240730121339.png]]  
Some features could be standard deviation and mean of the images. A vector is used to represent the features, which becomes a vector of two coefficients, one for mean μ z and one for standard deviation σ. For N images we have matrix M of dimension 2xN

For reminder, a vector of coefficients is a vector that represents the coefficients of a linear equation, e.g.  
![[Pasted image 20240730121717.png]]  
In our case the matrix M represents the a terms in a linear equation.  

When we plot standard deviation against mean (i.e. Plot features against each other) and plot the values of these features for each image we get:  
![[Pasted image 20240730121917.png]]
We see that there are two distinct groups of images, which happen to be grouped based on their class. Hence there is a clear difference between the images of each category, and we can develop a straight line model to distinguish between the two classes of images. 

We can use the straight line model to predict which class a new image would be. If we measure the values of mean and standard deviation of the image we can plot it on the graph, where it will be under or above the straight line. Since below the line is region for class B and above the line is region for class A then we can effectively predict which class a new image will be. This is the basic process of pattern recognition. 

The mean and standard deviation are used as features in the example. In general though the features will be collected in a feature vector, where:  
![[Pasted image 20240730123150.png]]  
Features and feature vectors are normally treated as random variables as they can pop up anytime and are suscept to noise.  

The straight line model in the previous example is known as the decision line, which classifies objects based on their features. This is done by using the line to divide the feature space into two regions, where each region represents a class/category. So if the feature values of an object falls into a region then we can say it belongs to that class. 

However this may not always be true, and if the prediction is wrong it is a misclassification. With the example we provided labels for each class and we used a set of objects where we knew what their classes were, and use that data to form the decision line. The initial feature vectors (or patterns) used to develop the decision line is referred to as training patterns (training feature vectors).

The number of features, i, depends on the object, and also the type of features to use. The decision line is also often not straight, and is optimized with a optimality criterion. Also the grouped objects on the feature space is often not so tidily grouped, and often we get some points that cross over regions, forming non linear decision lines. Designing a classifier (decision line) is part of the classification design stage, and finding the classification error rate is part of systems evaluation stage.  

The stages of designing a classification system:  
![[Pasted image 20240730130232.png]]  
Each stage is not independent and can rely on other stages to develop the stage, and even go back to previous stages to improve performance.  

Supervised learning is utilizing prior known information to develop the classifier. The previous example used supervised learning because we had a set of images which we knew the class of and developed the decision line using that data.  

