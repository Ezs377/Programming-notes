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
- **Predictors/features**: Essentially inputs, or independent variables
- **Responses**: Essentially outputs, or dependent variables
- **Qualitative variables**: Discrete or categorical variables, not defined by numerical values
- **Quantitative variables**: Numerical values, able to be counted
- **Ordered categorical variables:** Ordered categories without usage of numerical values (e.g. Small, medium, large)
- **Regression**: Predicting quantitative outputs
- **Classification**: Predicting qualitative outputs
- **Target**: A numeric code used to encode a class/category
- **Bias**: The Y intercept of the linear model
- **Hyperplane**: A subplane that is n-1 dimensions in n dimensional space, e.g. In 3D space a hyperplane is a 2D plane inside 3D space. A hyperplane is typically used to 'divide' the dimensional space into two half spaces, e.g. A 1D line (hyperplane) separates 2D space into two 2D regions
- **Hyperparameter:** A parameter that specifies details about the learning process of a model, whereas standard parameters define the model itself. 
- **Linear model:** A type of AI model that forms a polynomial curve, but has the same vector coefficient for all unknown parameters, in the form of y(x, **w) = w<sub>0</sub> + w<sub>1</sub>x + w<sub>2</sub>x<sup>2</sup>+...+w<sub>M</sub>x<sup>M</sup>
- **Error function**/J(θ): Minimizes the difference between the output of a polynomial function/AI model and the training dataset points for each given input
- θ/w/**w**: Known as parameters, or weights, which are the coefficients to a polynomial model
- 


 

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

###### Fish example: 
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

This means that we have an overall cost attributed to our decisions chosen by the model. By cost, we mean that one output is more favorable than the other. So no we need to design a *decision rule* that sets the decision boundary (critical values of \*x) that minimizes the cost effects of favoring one outcome over another. *Risk analysis* is the analysis of such decisions, for example we could base our decision boundary at lightness = 2 which guarantees no bass will be leaked out, but the majority of identifications would also be salmon so the company takes a loss.

Assuming that no single feature is good enough for us to develop a good model performance, we can start using multiple features to develop our model. Another feature we could try is the fact that sea bass are typically wider than salmon. Now we will use two features: Shininess and width. Ignoring the practical means of measured, eventually we can develop a 2D feature vector **x** that holds a feature value for each element, i.e. **x** = \[x<sub>1</sub>, x<sub>2</sub>] where x<sub>1</sub> represents the feature value shininess level of a fish, and x<sub>2</sub> represents another feature value which is width of fish. This vector can be plotted as a point in 2D feature space, where the features are applied as the axes of the graph (e.g. Shininess on X axis, width on Y axis).  

When we plot our vectors in 2D feature space we expect to see feature vectors representing bass grouped together in one region, and feature vectors representing salmon grouped in another region. Thus we'll need to divide our feature space into two regions to indicate which region belongs to what fish. We get the following graph:
![](Pasted%20image%2020240806121759.png)  
We can see that the feature vectors of bass and salmon are roughly grouped in their own regions. Then we develop a straight line model for the decision boundary, and classify points below the boundary as salmon, and points above the boundary as bass. Hence we've developed a model using two features. It's not 100% accurate but better than the previous models. We could use even more features to better the model but using more features requires more resources, and some features could be redundant - E.g. All fish have the same eye color regardless of species.

For this model we used a straight line model for the decision boundary, which we see is good but still misclassifies some points. We could use a complicated model for the decision boundary so that is 100% accurate based on training data,  
![](Pasted%20image%2020240806123355.png)  
However since this is based on training data, if given real data the model will not accurately predict points since the decision boundary was formed on training data only. This is the issue of *generalization*, where our model needs to be generalized enough so that a similar performance is recorded for any given data. Also complicated models are harder to work with in general.  

Getting more samples could solve this issue since we would get a better overall pattern for the model, but often data is limited. Instead we accept the fact that our model will not be 100% accurate in favor of simplifying the model and adaptability of model. 

### Pattern representations:
This is one of the main problems of *statistical pattern recognition* where we need to decide the balance between complexity and accuracy, as well as ensuring our model performs well on new data and is generalized well enough without making the model too complicated.
![](Pasted%20image%2020240806130239.png)
We might also need to change the model function for the same data, e.g. If we want to separate fish by gender instead of species. Different decision tasks may require different features and give different decision boundaries. This means that our decisions are based on our objective task, or cost oriented. Creating a single general purpose artificial pattern recognition device that can do everything is difficult, compared to humans who can switch tasks easily. 

In order to determine how 'complex' our model should be to give the best result between accuracy and efficiency we need a good *representation* which allows good pattern classification. Every pattern recognition problem needs a good representation. Patterns could be represented as vectors of number values, an ordered list of attributes, etc.

When we don't have enough training data one common technique is to use knowledge of the data itself. With less data, more knowledge becomes more important. One method is using *analysis by synthesis*, where we have a model of how each pattern is generated in the data. 

For example, in speech recognition, when a person pronounces the sound 'dee' people commonly pronounce it by opening the mount and putting their tongue on the roof of their mouth. And we can assume that the differences in pitch may be due to the talker being male, female, old, young, etc. If we can determine how a particular pattern is produced, then the classification itself can be based on this fact, e.g. Determine the person's gender using the 'dee' sound received, using the fact that females produce a higher pitch while males produce a lower pitch.  

Another example is recognizing a chair - There are many types of chairs such as beanbags, office chairs, stools, etc. Instead of trying to find a chair based on their features (which is hard since all chairs can have varying features) we can instead look for their functionality - that is, a stable object that can support a person sitting down.  

Basically speaking, real-world pattern recognition utilizes some knowledge regarding how the patterns were made in reality, or consider the real world facts about the pattern. For example, if we have a model that looks at handwriting and tries to interpret the letters, we can give it the information that each letter was done in strokes rather than a stamp, so it can help the pattern recognition.  

Some issues that could rise with pattern recognition are:
- Feature extraction: A perfect feature extractor can practically identify objects barring the need for a classifier, and conversely a perfect classifier would be able to identify features without a feature extractor. Hence developing the feature extraction is more dependent on the problem and domain than the classifier, since we can recycle classifiers but not necessarily feature extractors. For example, a feature extractor for a camera based interface is useless for a audio based, but the classifier could be simply modified to take audio instead of pictures
- Noise: The input to a model is typically rife with unnecessary information, which we need to filter out. More specifically, noise is a property of the sensed pattern that occurs due to randomness in nature or hardware/software. The challenge however is knowing which differences between objects are caused by noise and which are caused by the object features
- Overfitting: We can develop complex models to further increase 'accuracy'. But too complex and the pattern is only suited on the test data, and cannot derive an accurate pattern from other sources of data. We have to consider what degree of complexity is suited to provide best accuracy without sacrificing performance  
- Model selection: Sometimes using different model classes can provide better performance/accuracy, either due to the way these classes and features are captured (which may be easier) or to the model's method of pattern recognition. Hence how do we know we have a good model? Is there another model that could do a better job? This can take time to figure out, or use an automated process to figure out the best model  
- Prior knowledge: Applying prior knowledge into the model can be harder than expected, such as analysis by synthesis or underlying categories or specific attributes of patterns (e.g. Knowing how a sound is produced)
- Missing features: It is common for a feature to be missing or corrupted when taking in data, which needs to be accounted for and the model needs to be able to figure out what to do
- Segmentation: When taking in data using an external device (e.g. Photos through a camera) often we have to segment the data into sections that can be interpreted with features. For example, identifying what part of an image is the background and which is the desired object. With speech recognition segmentation is particularly difficult, as we need to identify each noise made and correspond it with a letter or word. And difference sounds can be produced with the same letter depending on the word
- Context: We can use the context the model is applied in to improve it, e.g. When analyzing fish, the fish usually comes in batches of the same fish, so if salmon comes out then the following fish is more likely to be salmon, which can be used if the next fish is ambiguous (i.e. Very close to the decision boundary) as it is likely to be salmon. But context can also differ in scenarios and often different things mean differently to other people, e.g. Saying "bleh" can mean bored or yuck when spoken by someone  
- Invariances: We want a representation of data to be invariant to certain factors, e.g. For a fish image we don't care about its rotation and translation on the conveyor belt, as we just want the fish features. Similarly with speech recognition we want our representation to be invariant to accents and dialects. Rotation is an example of invariance to two dimensional rotation. Ideally we want an invariance to 3D rotation, which may prove difficult as objects appear differently from all angles. We may also want our recognizer to be invariant to the rate a pattern evolves, such as a hand waving quickly or slowly. This is particularly difficult with speech as some people talk faster or slower than others. So the question is how do we know when invariance is present? And how do we implement this in the recognizer?
- Evidence pooling: We can use multiple features to improve recognition, and conversely we can also improve recognizer by using multiple component classifiers. If all categorizers agree on an object then all is fine, but with disagreements then we need a 'master' classifier that collects (pools) evidence from the multiple recognizers to make a decision. E.g. If 10 doctors analyze a person, one person says they're sick and 9 say they're healthy, what are the chances the single doctor knows something the others don't? This is a problem that needs to be implemented in the model
- Costs and risks: A classifier rarely operates by itself - usually it is used to make judgements and recommend actions with the associated costs and risks. One of the common risks is classification error, the percentage of new patterns that are incorrectly labelled. Hence how does this knowledge affect the classification decisions?

###### The machine learning approach:  
1. Learning and adaptation: Any method that uses information from training samples to design a classifier uses the process of learning. The development of classifiers starts with designing a general model/structure and the utilizing training patterns to learn or estimate the unknow parameters of the model. Learning uses various logarithmic approaches that try to minimize the error on a given set of training data. Many gradient descent algorithms have been formulated over time to improve classifier parameters to reduce error measure. The process of learning usually appears in many general forms, each tailored to address a specific problem characteristics and data requirements. These forms utilize various learning paradigms and methodologies. So we have plenty of options to find a suitable algorithm to improve the accuracy and performance of classifiers
2. Supervised learning: It is the approach that involves providing the model some category labels/costs for each pattern in the training set through a teacher, and the objective is to minimize the sum of these costs. We have to ensure that the learning algorithm 'power' which includes its capacity to capture complex relationships and handle intricate patterns in the data. We need to also assess the algorithm's stability against variations with the parameters while still producing consistent and reliable results. Convergence of the algorithm is important to assess if the algorithm can reach an optimal solution or satisfactory approximation, and we also need to consider the scalability of the algorithm that allows it to continue its operation when faced with varying factors, such as different training patterns, dimensions of input features, or the complexity of the problem. Understanding how the algorithm scales with these factors helps us manage computational resources effectively. Finally we want the learning algorithm to favor simpler solutions over complex ones, since complex solutions tend to badly reflect unseen data (overfitting)
3. Unsupervised learning: Also known as clustering, we let the algorithm develop its own patterns based on the given input data by finding natural groupings or clusters within input patterns without relying on a teacher. Without any labelled data we need different ways to finding patterns. With unsupervised the two key challenges are finding the optimal number of clusters and avoiding inappropriate representations. Finding the right amount of clusters utilizes different algorithms and techniques. A good cost function helps guide the clustering process into generating meaningful clusters. 
4. Reinforcement learning: Category labels aren't given, instead a learning system, aka the agent, interacts with data and receives rewards or punishments depending on the actions performed, which are determined by the supervisor or teacher. The agent adjusts its behaviour to maximize the amount of rewards over several iterations, which allows the agent to make decisions in different environments. The agent receives feedback from the environment and supervisor to learn. 

### Modelling data:
Modelling data involves the process of training and optimizing specific parameters in a predetermined process to capture the underlying behaviour of the data. The objective is to develop a model, typically a function, that best represents the patterns and characteristics of a given dataset. Basically we try to fit the available data to a chosen model which can accurately describe relationship/data distribution between variables. We want to minimize the differences between predicted values and actual observed values in the dataset by fine-tuning the parameters of the model. For example, a regression model can be used to find the relationship between variables by plotting a set of samples to a mathematical function, or use a classification model to assign data samples to predefined categories based on their features and previously labelled examples. 

#### Polynomial curve fitting:
Let's say we have a real valued input variable x, and we want to use this to predict the value of a real value target variable t. For example, if we take the generated data as results from the function sin(2πx) with some random noise. Then the input values {x<sub>n</sub>} are generated randomly in the range (0, 1) which will cause the resulting outputs to be between 0 and 2π. The corresponding target values {t<sub>n</sub>} are obtained by first calculating the values of the function sin(2πx) and then adding random noise with a Gaussian distribution having a standard deviation of 0.3. 

Now if we get a training set with N observations of x, written as a vector set of x ≡ \[x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, ... x<sub>N</sub>]<sup>T</sup> and couple it with the corresponding observations of the values of t, written as another vector set of t ≡ \[t<sub>1</sub>, t<sub>2</sub>, t<sub>3</sub>, ... t<sub>N</sub>]<sup>T</sup> (note that these are transposed vectors, meaning that both are actually arranged as a single column instead of row). Plotting the points for N = 10 gives:  
![](Pasted%20image%2020240913175238.png)
The points were plotted by choosing values for x as x<sub>n</sub> where N = 1, 2, 3, ... 10 spaced uniformly in the range (0, 1). The target t was obtained by passing values of N into the sin function, then adding a small Gaussian distribution to obtain t<sub>n</sub> for each N value. Hence the final equation is  
y = sin(2πx) + N(0, 0.3) where N = Gaussian function, and it indicates a mean around 0 with a standard deviation (σ) of 0.3. Variance of Gaussian noise is dictated as σ<sup>2</sup> so the variance of Gaussian noise is 0.09. 
![](Pasted%20image%2020240915151522.png)
We want to use the training set to make predictions of the value t^ (t with hat) using some input value x^ (x with hat). Basically if we can derive the equation sin(2πx) using the AI model and training set then we have success. 

First attempt uses the following equation,  
![](Pasted%20image%2020241005224553.png)  
Where M is the polynomial order, and x<sup>j</sup> is x raised to power of j. The polynomial coefficients comes from the vector **w**. While y(x, **w**) is a nonlinear function of x, the equation itself is linear with coefficients of **w**. This type of function are linear in their unknown parameters and are known as **linear models.** The values of coefficients will be determined by fitting the polynomial to the training data.  

This can be done by minimizing an error function that measures the difference between the output of y(x, **w**) for a given **w** value and the training set data points. A simple straightforward error function is the sum of squares of errors between predictions of y(x<sub>n</sub>, **w**) for each data point x<sub>n</sub> and the corresponding target t<sub>n</sub> from the training set such that:  
![](Pasted%20image%2020241005231400.png)  
The error function E(**w**) is always positive and hits zero if the prediction functions passes exactly through every single training data point.  
![](Pasted%20image%2020241005232004.png)  
We want to pick a value for **w** that reduces E(**w**) as much as possible. Since the error function is linear in elements of **w** then we can find a unique solution in terms of **w**. Then we just need to find a suitable M value (which denotes the order of the polynomial). With this example M = 3 provides the most accurate predictions.
![](Pasted%20image%2020241006004148.png)
With high numbers of M we can get a polynomial that goes through every point, but the actual function oscillates wildly, and example of overfitting. While we can guarantee perfect accuracy with the training set we cannot use to model for other data. 

To achieve good generalization of the data we need to measure the dependence of the generalization performance of M by using a separate test set that is generated in the same manner as the training set, except with differing noise values. For each choice of M we re-evaluate the residual value of **w**** for the test data set. It may be easier to use the RMS error:  
![](Pasted%20image%2020241006011310.png)  
Where N allows comparison with different sizes of datasets equally, and the square root equalizes the scale and units for E<sub>RMS</sub> with the target variable t.  

Once we get the error values for the test and training data sets against the model we can tune our model even more. We calculate the error value for each value of M used.
![](Pasted%20image%2020241006012342.png)
We see that for smaller values of M we get larger error. For M = 3 to 8 the error values are relatively low. At M = 9 the training set error becomes zero, but the test set error becomes super high, which means overfitting.  
![](Pasted%20image%2020241006012714.png)  
Theoretically a higher order polynomial should contain all lower order polynomials within so that it becomes more accurate, and hence the higher M value the more accurate predictions (which is also proven that we can estimate a sin wave by using a power series). When M is increased, the values of coefficients **w** get much larger to match the data points. So the reason we get high error with higher orders is because the polynomial is trying to fit to random noise as well as data points. 

Another thing to note is that the more data points we have the mode accurate the model becomes with higher values of M, i.e. Higher order.  
![](Pasted%20image%2020241006014142.png)  
Essentially the more data we have the more 'flexible' (complex) the model can be. A rough rule of thumb is that the number of data points should not be less than a multiple (e.g. 5 or 10) of adaptive parameters of the model (i.e. The parameters that dictate the complexity of a model, such as the initial value, learning rate, etc). 
![](Pasted%20image%2020241006014914.png)  









#### Regularization:  
To control overfitting we can do regularization, which is adding a penalty term to the error function to prevent coefficients from reaching large values (which result in overfitting). 

The simplest penalty term is the sum of squares of all coefficients, i.e.  
![](Pasted%20image%2020241006015256.png)  
The coefficient λ determines the importance of the regularization term compared to the sum of squares error term. w<sub>0</sub> is typically ignored in the regularizer as it causes the results to depend on the choice of origin for the target variable, or it comes with its own regularization coefficient. 
![](Pasted%20image%2020241006021227.png)
![](Pasted%20image%2020241006022711.png)
![](Pasted%20image%2020241006022720.png)
With a value of λ = -18 we can reduce the overfitting even with M = 9. However if λ is too large we get a poor fit once more, as shown on the right graph.

Plotting RMS error of both training and test datasets against ln(λ) gives the impact of the regularization term on generalization error. So λ controls the overall complexity of the model and the degree of overfitting.  

The standard modelling procedure takes the available data and separates it into two sets, training and testing. The training data is sued to set **w** coefficients, and the testing data is used to optimize the model, setting M and λ values.  


### Supervised learning: 
![](Pasted%20image%2020241006040255.png)  
Regression is used to predict continuous variables. When a predicted variable can only be assigned into a number of discrete values then it is a classification problem.  

Input data can have more than one feature and each feature is represented as a vector of ith values. 
![](Pasted%20image%2020241006040508.png)  
E.g. **X<sub>1</sub>** and **X<sub>2</sub>** represent two features where the ith element corresponds to the same object the data was taken from.  

The regression function is essentially the polynomial equation that forms the model.  
![](Pasted%20image%2020241006040742.png)  
![](Pasted%20image%2020241006040802.png)  
The optimum coefficients (in the example θ) will minimize the error between the actual target values and the predicted output values. A cost function is used to optimize the coefficients, where m = number of samples. The above cost function is also known as the least squares model.  
![](Pasted%20image%2020241006041018.png)  

#### Model optimization:  
Gradient descent is an optimization algorithm for finding the minimum of a function. For example:
![](Pasted%20image%2020241006041056.png)  
It works by starting at some point X<sub>0</sub>, then approaching the next point X<sub>1</sub> by using the gradient descent algorithm which depends on calculating the derivative f'(X<sub>0</sub>). The derivative is the slope of the tangent line (gradient) to the function at that point, i.e. X<sub>0</sub>. The direction taken to the next point is the negative of the gradient (since we want to hit a minimum, then gradient should converge to zero, since a positive gradient means we are past the minimum (sloping upwards) and negative gradient means we are behind the minimum (sloping downwards)). 
![](Pasted%20image%2020241006041351.png)  
n is also known as the learning rate, that controls the 'speed' of the descent. 

We also have to consider if we are approaching a global minimum or a local minimum, since the local minimum would not be the optimal minimum.
![](Pasted%20image%2020241006041551.png)

The same approach applies for multidimensional functions.  
![](Pasted%20image%2020241006041650.png)  
![](Pasted%20image%2020241006041717.png)  

Gradient descent is best used when we can't find the parameters can't be found analytically (e.g. Using calculus). When using it we start at some point on the function then iteratively move along the function until the algorithm calculates the minimum, then we take the parameters from the gradient descent algorithm equation.  
![](Pasted%20image%2020241006041856.png)  
a in this case is the learning rate. A high learning rate means we can accidentally skip over the actual minimum, while a smaller learning rate means it will take longer to find the minimum. Sometimes we can optimize the learning rate by setting it high initially then lowering it as it approaches the minimum.  

Example:  
![](Pasted%20image%2020241006042058.png)  
The recursive formula, known as LMS algorithm, optimizes the coefficient θ by using the cost function J(θ). 


Two approaches can be used to use a generalized one example training to include multiple examples:
- Batch gradient descent: ![](Pasted%20image%2020241006042355.png)Basically while not at the minimum or not at the iteration limit, start at j = 1. Then we perform recursive formula (LMS algorithm) on the jth coefficient, then increment j, then loop.
- Incremental gradient/stochastic gradient descent: ![](Pasted%20image%2020241006042557.png)Basically while not at the minimum or not at the iteration limit, for 1 to n (where n is number of parameters for θ), perform the LMS algorithm for j = 1 to n, then increment j. Once the j loop is done then increment i and repeat.

Essentially the batch gradient descent we update parameters through every example every loop, while in stochastic gradient descent we converge the cost function for each example before moving onto the next example.  

Convergence may also not perfectly hit the minimum, so we want to set a range that we can consider the minimum with a small threshold value to prevent the algorithm going on forever, like J(θ) < ε. We can also set the limit of iterations to prevent recursion from repeating forever.  

###### Convex:  
A real valued function on n dimension is considered convex if a straight line between two points is higher than the actual function line, i.e.  
![](Pasted%20image%2020241006145038.png)  
A double differentiable function of a single variable is convex only if the second derivative is non-negative across the whole domain. Common examples of a convex function is x<sup>2</sup> and e<sup>x</sup>. Essentially a convex function is a smiley face and a concave function is a hill shape. A useful property of convex functions is that there is only one minimum.  
![](Pasted%20image%2020241006145257.png)  
E.g. f(x) = x<sup>2</sup>, the second derivative is 2 which is a non negative constant, hence strongly convex. If the second derivative is not a constant but has other terms, e.g. f''(x) = 2x then it is strictly convex no strongly convex, as it is possible to get negative points.  
![](Pasted%20image%2020241006145529.png)  




#### Linear regression approach:  
Another way to reduce the error function J(θ) is to take the derivatives of J(θ) with respect to θi and setting the derivative to zero. This is an analytical approach that is more efficient then the iterative approach, which might not be guaranteed to find a minimum. 

Linear regression is a technique that can be used to solve regression problems. The object of linear regression is to develop a system that takes input vectors **x** and predicting the corresponding scalar value h(x) as the output. In linear regression, the output is a linear function of the input. The output prediction h(x) is denoted as:  
![](Pasted%20image%2020241006150843.png)  
**y**^ (y with hat) is the outputs, **w**<sup>T</sup> is the weights vector, **x** is the input features vector. We have to optimize the weights vector **w** (note that θ and **w** are used interchangeably for weights vector). 

Parameters are values that control the behaviour of the system. 