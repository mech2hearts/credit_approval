# credit_approval
This program is part of a group study conducted by Chang Kim, Julian Sosa, Victoria Nguyen, and Roger Williams for their Data Mining course. The Naïve Bayes analysis of the data was conducted by Chang Kim while the Decision Tree Classifier analysis was conducted by Roger WIlliams.

## Installation
Install the following packages:

>h2o (pip install h2o)

>pandas (pip install pandas)

Run on Jupyter notebook for optimal results

## H2O

H2O, an open-source machine learning and predictive analytics platform, was utilized in order to streamline the production of code. H2O's REST api allows for use for languages such as R and Python. Many models are provided by the platform and are easy to implement especially for beginners of data analytics/machine learning. The Naïve Bayes model was used for this program.

Pandas was used to organize and clean the data as required.

## Data Set

Credit approval records provided by the UC Irvine Machine Learning Repository. Each attribute name and value are listed as random symbols in regards to customer confidentiality. An attribute could possibly be a name, yearly salary, or occupation but there is no way of knowing what each attribute represents. In order provide personal readability and organization, each attribute was provided a label based on their data type.

![labeled data](https://i.imgur.com/W97bVV0.png)

The data types for the attributes are all either numeric or nominal. Each instance has 15 attributes and a class label with two possible values: ‘approved’ or ‘not approved’. Additionally, a small percentage of the values are missing (0.0065%). Lastly, the distribution of the data is fairly evenly split, with 307 instances labeled ‘approved’ and 383 instances labeled ‘not approved’.

![approval results](https://i.imgur.com/wjlpu1M.png)

Goal and Results
The goal was to predict the accuracy of the model with the data provided. 80% of the total data set was used to train the model and the rest (20%) used to predict the approval outcome. In the end the model was able to have about an 88% accuracy.

![Confusion matrix of test records](https://i.imgur.com/cZTJFJv.png)
