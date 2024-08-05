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
*Pattern recognition* is a scientific discipline that focuses on classifying *objects* into a number of *categories/classes*. The objects are typically referred to by a generic term "patterns", and classified by using the object's features to fit a *category/class*. 

An example of pattern recognition is using a machine learning to identify people recorded on camera, the people are objects and the people faces are features. Other features could be person height, race, gender, etc.  

The first step to pattern recognition is to identify measurable *qualities (features)** that distinguish object samples from each other. 

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

The straight line model in the previous example is known as the *decision line*, which classifies objects based on their features. This is done by using the line to divide the feature space into two regions, where each region represents a class/category. So if the feature values of an object falls into a region then we can say it belongs to that class. 

However this may not always be true, and if the prediction is wrong it is a misclassification. With the example we provided labels for each class and we used a set of objects where we knew what their classes were, and use that data to form the decision line. The initial feature vectors (or patterns) used to develop the decision line is referred to as *training patterns (training feature vectors)*.

The number of features, i, depends on the object, and also the type of features to use. The decision line is also often not straight, and is optimized with a optimality criterion. Also the grouped objects on the feature space is often not so tidily grouped, and often we get some points that cross over regions, forming non linear decision lines. Designing a *classifier (decision line)** is part of the classification design stage, and finding the classification error rate is part of systems evaluation stage.  

The stages of designing a classification system:  
![](Pasted%20image%2020240804111556.png)
Each stage is not independent and can rely on other stages to develop the stage, and even go back to previous stages to improve performance.  

*Supervised learning* is utilizing prior known information to develop the classifier. The previous example used supervised learning because we had a set of images which we knew the class of and developed the decision line using that data.  

In *unsupervised learning*, instead we are given a set of feature vectors **x** and the goal is to cluster/group 'similar' vectors together. 
![](Pasted%20image%2020240804131111.png)  

For example, using a satellite to scan EM energy from the Earth's surface that where certain wavelength bands correspond to a type of terrain. One surface vector x for each 'cell' (Region) from the sensed Earth surface is made, and the elements x<sub>i</sub> where i = 1, 2... l of the vector x are the corresponding image pixel intensities in representing the spectrum of wavelengths, which varies across the entire wavelength spectrum.  

A clustering algorithm can be used to reveal the groups where features are clustered in l-dimensional space (where l = elements of x representing pixel intensities). Once clustered we can apply labels to different groups, such as water terrain, mountain terrain, etc using available references (e.g. Existing maps). 
![](Pasted%20image%2020240804152318.png)  
Unsupervised learning requires a good metric to calculate 'similarity' or 'distance' between two feature vectors, as well as choosing a suitable algorithm to cluster the vectors. 

*Semi supervised learning* is similar to unsupervised learning, we have unknown classes (unlabeled data) but we also have true classes (labelled data). The labelled data is sued to improve the classification performance of unlabeled data.

### What is AI:
Artificial intelligence, as a term, was conceptualized in 1950 to describe the effort the automate intellectual tasks usually performed by humans. As a general field AI covers machine learning and deep learning, and other things. Symbolic AI was an older form of misinterpreted AI where instead a computer was programmed with enough rules that it could emulate intelligence (e.g. Chess AI). 

*Machine learning* is the science of programming computers so they can learn from data. It allows a computer to learn without being explicitly programmed. More specifically, a computer program can learn from experience E with respect to task T and some performance measure P, if the performance of task T, measured with P, improves with each experience E. Basically P is used to measure the performance of a task T, and if T improves every experience E then the computer program can 'learn'.

For example, an algorithm to detect spam emails. A bunch of normal emails and spam emails, which were explicitly labelled as normal or spam by the users, can be used as the training set. Each training example is called a training instance, i.e. A sample. 

In this case the task T is to identify spam emails, experience E is the training data, and we need to define the performance measure P. An example of P would be the ratio of correctly classified emails to misclassified emails - This type of measure is called accuracy and is often used for classification tasks.  
![](Pasted%20image%2020240804161647.png)  
![](Pasted%20image%2020240804161654.png)  

Machine learning algorithms can derive features from given data without programmer interference, and develops its own rules for automating the task. To do machine learning we need three things:  
- Input data points: The type of data used to train the model. This varies depending on the application, e.g. For speech recognition it could be sound files
- Examples of the expected output: The expected output from the machine. This determines how the output is produced and received, e.g. For image processing, an output could be "cat" or "dog" when identifying the image  
- A suitable metric to indicate whether the algorithm is doing a good job: Is used as feedback to adjust how the algorithm works to improve accuracy. This adjustment step is what we refer to as learning  

We can say that the main problem in machine learning is to meaningfully transform data: I.e. To learn good representations of the given input data; Representations that gets us closer to the expected output. 

### Deep learning:  
The 'deep' in deep learning refers to the layering method to allow a model to 'learn'; Multiple 'layers' are applied to the model where each layer improves the model further.

The amount of layers is called the depth of the model. Modern deep learning can have tens or hundreds of layers, exposed to large amounts of data.  

Other methods of machine learning usually only take one or two layers of representations of data (e.g. Analyze a pixel histogram then apply classification rule); This is called shallow learning.  

**Deep learning example:**  
We want to develop a model to interpret handwritten numbers based on images of a certain size
![](Pasted%20image%2020240805141358.png)
Each layer successively process the input until reaching the final output which is a vector that can be used as data.
![](Pasted%20image%2020240805141900.png)  

The AI hierarchy is often represented as:  
![](Pasted%20image%2020240805141936.png)  

### How machine learning works:  
Machine learning is about mapping inputs (such as images) to targets (such as labels, e.g. "cat") and this is done by observing many examples (samples) of the input and targets. Each layer can 'memorize' the attributes of the presented data, and this 'memory' is attributed as the strength, or weight, of the connections between layers.  

*Weights* are also called the parameter of the layer. In this context, learning means finding a set of values for the weight of all layers in a network such that the network will correctly map inputs to their associated targets. The *neural network* can contain thousands or millions of parameters, which we cannot find manually. 

Instead we use a successive learning procedure that iterates over several layers. We set an initial weight for the first layer, and we need to find a way to measure how far the targeted output is from what can be found using the initial weights, which is set at small random values. 

The difference between the calculated outputs and the targeted outputs is the job of the *loss function*, or the *objective function*. The loss function computes a *distance score* to determine how good the network has done on this specific example using the initially proposed weights. Then the distance score is sent back and used as feedback to adjust the value of weights in a direction that will lower the loss score for the current example. This adjustment is the *optimizer*'s job, which implements the *backpropagation* algorithm which is an important algorithm in the learning process (learnt later).
![](Pasted%20image%2020240805144953.png)  
With each example processed, the weights are adjusted with the optimizer, that uses the loss score from the loss function. By *training* the model we reduce the loss with each successive example. A network with minimal loss is one where the outputs are as close as possible to the targets, forming a trained network.  

Machine learning can be applied to a variety of scenarios, such as:
- Simplifying tasks that would otherwise require a lot of work to program a traditional computer, e.g. Identify dogs and cats from an image (would only need images of dogs/cats to train the model, instead of coding specific rules to cover all cases)
- Solving complex problems that don't have a specific solution or rules
- Fluctuating problems, since models can adapt to new data
- Processing large amounts of data
Machine learning is about developing rules using inputs and outputs, instead of finding an output based on a rule

In particular, the ability to extract features from data allows machine learning to perform predictive tasks, such as weather forecasting, fixing corrupted data, and error detection.  

### Classical pattern recognition:  
Pattern recognition is closely related to machine learning, and can be said to be an application of machine learning. Pattern recognition is the process of recognizing patterns by using machine learning algorithms, and both terms fall under the artificial intelligence topic.
![](Pasted%20image%2020240805151346.png)

**Fish example:**  
A fish factory wants to be able to automatically sort fish based on species on a conveyor belt, using a camera. We want to separate bass fish from salmon fish.

Some physical differences between the fish types include length, width, number and shape of fins, shininess of scales, position of mouth, etc. These are possible attributes, or features, for the classifier which will use them to identify the fish type. Things that can get in the way of such identification include the orientation of fish, light level, visibility, multiple fish visible, etc. These things are called *noise* and we want to eliminate noise before providing the images as an input to the model.  

A prototype model process:
1. The camera captures image of fish
2. Images are pre processed to simplify the next operations without losing data
	- In particular, we could use a *segmentation* operation, where images of different fish are somehow isolated from one another and the background
3. The pre processed data is sent to a *feature extractor*, which reduces the data by measuring certain features or properties 
4. Measured features/properties (which are processed as values) are passed to a *classifier* that evaluates the data and produces an output

The preprocessor might edit the image taken from the camera to remove as much noise as possible. All preprocessing takes place outside the model. This could be  either cropping the image to remove the background, or adjusting the light levels, or etc. 

Let's say for example, that we know that a sea bass is typically longer than a salmon. Thus we could use length as a feature for the classifier, by using length l and whether the length exceeds a critical length \*l which acts as the threshold between bass and salmon lengths. To choose the threshold \*l we could analyze some samples of the fishes and inspect the results. 
![](Pasted%20image%2020240805170218.png)  
For example, we could get the following histograms for fish lengths:  
![](Pasted%20image%2020240805170905.png)  
This is very inaccurate because while sea bass are typically longer, it is not always guaranteed and fish will typically vary in size regardless of species. 

So another metric we could try to use is scale shininess. We'll take the average shininess of a fish from the image, remove environmental light, and assign x as our shininess level, with \*x as our critical value for shininess. Using shininess as a feature provides this histogram:  
![](Pasted%20image%2020240805171155.png)
While it is better than using length it is still generally quite inaccurate, as we have some misclassifications. 

However, one of our assumptions is that the cost of deciding a bass is equal to deciding a salmon. But in business, the factory owners have determined they want to favor salmon more often than bass, because customers complain if they find bass in salmon cans, but like to get occasional salmon pieces in bass cans (since salmon is more valuable in this case). Hence we need to adjust our *decision boundary* (which is our critical value \*x) to favor lesser shininess, and possible adjust it further depending on customer feedback on products.  

This means that we have an overall cost attributed to our decisions chosen by the model. By cost, we mean that one output is more favorable than the other. So no we need to design a *decision rule* that sets the decision boundary (critical values of \*x) 



