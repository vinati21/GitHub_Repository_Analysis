# GitHub Repository Analysis
## Title: Grouping the GitHub repositories and predicting the technology it is built in based on the repository features.

## Statement of the project problem: 

GitHub contains various types of repositories which may or may not correspond to individual projects and also, they could correspond to different types of software languages. Each repository will a have a purpose and could be different from one another. It is very important to understand the trends and characteristics of the repositories based on which we can filter the repositories and classify them into technology classes.

## Objectives of the project: 
1.To understand the trends of the GitHub repositories.
2.To explore the similarities and dissimilarities among the GitHub repositories.
3.To identify different groups based on purpose of creation of repositories.
4.To predict the technology on which the repository was built in.

## Data Description:

I have collected GitHub transactional data for the month of April in 2014.I have filtered repository data and collected repository features. We have a mixed type of data containing textual data, categorical data and discrete count data. Each of them have to be processed differently to encode them and use them for our analysis. The data we will be working on has about 500k rows and 5000 features.

## Workflow Design and Methodology:
![image](https://user-images.githubusercontent.com/48361933/81434781-5a6e7b80-912c-11ea-8113-6b02124c7f39.png)

## Some interesting Findings: 

![image](https://user-images.githubusercontent.com/48361933/81457549-23b05980-915c-11ea-83f8-5b0016de9240.png)

### Number of characters in Repository Descriptions: 

![image](https://user-images.githubusercontent.com/48361933/81457607-63774100-915c-11ea-85e7-fb680c5d0439.png)

### Most Frequent words for each repository language

![image](https://user-images.githubusercontent.com/48361933/81457633-87d31d80-915c-11ea-80f1-06871ae4f8b8.png)

### Example of Frequent word counts in for a language (PHP)

![image](https://user-images.githubusercontent.com/48361933/81457678-b94be900-915c-11ea-83d9-9da996101a25.png)

### Words in our clusters
![image](https://user-images.githubusercontent.com/48361933/81457727-ebf5e180-915c-11ea-9f3b-e8cd6b882c92.png)

### Clusters found in our repositories

![image](https://user-images.githubusercontent.com/48361933/81457756-029c3880-915d-11ea-9453-b259842a5cbd.png)

### The words that are most correlated to the target are:

1.'C' category:
	  Most correlated unigrams:
	 	. nginx	 
 	 	. firmware	 
 	 	. pebble	 
 	 	. linux	 
 	 	. kernel
	 Most correlated bigrams:
	 	. linux kernel
 	 	 . kernel source

 2.'CSS' category:
	  Most correlated unigrams:
	 	. theme	 
 	 	. site	 
 	 	. personal	 
 	 	. blog	 
 	 	. website
	 Most correlated bigrams:
	 	. personal site
 	 	 . personal website

 3.'Java' category:
	  Most correlated unigrams:
	 	. spring	 
 	 	. minecraft	 
 	 	. bukkit	 
 	 	. java	 
 	 	. android
	 Most correlated bigrams:
	 	. java library
 	 	 . android application

 4.'JavaScript' category:
	  Most correlated unigrams:
	 	. angularjs	 
 	 	. nodejs	 
 	 	. jquery	 
 	 	. node	 
 	 	. javascript
	 Most correlated bigrams:
	 	. chrome extension
 	 	 . jquery plugin

 5.'PHP' category:
	  Most correlated unigrams:
	 	. laravel	 
 	 	. symfony	 
 	 	. plugin	 
 	 	. mirror	 
 	 	. wordpress
	 Most correlated bigrams:
	 	. plugin mirror
 	 	 . wordpress plugin

 6.'Python' category:
	  Most correlated unigrams:
	 	. xbmc	 
 	 	. sublime	 
 	 	. flask	 
 	 	. django	 
 	 	. python
	 Most correlated bigrams:
	 	. written python
 	 	 . python library

 7.'Ruby' category:
	  Most correlated unigrams:
	 	. activerecord	 
 	 	. cookbook	 
 	 	. chef	 
 	 	. rails	 
 	 	. ruby
	 Most correlated bigrams:
	 	. ruby rails
 	 	 . chef cookbook

 8.'other' category:
	  Most correlated unigrams:
	 	. website	 
 	 	. clojure	 
 	 	. haskell	 
 	 	. scala	 
 	 	. emacs
	 Most correlated bigrams:
	 	. plugin mirror
 	 	 . wordpress plugin

## Scope for improvement: 

•	There is definitely a scope for improving the performance of this model. We can use other classification algorithms such as XGBoost,SVM,KNN and Gradient Boosting and see which one can fit better.  
•	We can find the best model by tuning their hyper parameters and using model selection algorithms such as Hyperpot.
•	We can increase the prediction power of the model by adding more data.
•	We can also use more features for training such as our Boolean and discrete features which we have not considered for model training along with the textual features.




## Results: 

