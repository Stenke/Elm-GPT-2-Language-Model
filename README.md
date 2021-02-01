# Elm: Emotional Language Model for Personalized Tweets
Elm is an optimistic language model based on your favorite Twitter accounts.
We trained our language model on social contributors who exemplify humor and optimism with a willingness to be vulnerable.
<br /> <br />
<p align="center">
  <img src="https://github.com/Stenke/Tweets-to-Stories-to-Topics/blob/main/Visuals/pirate-cat.jpg" width="600"   length="800" />
</p>


# Business Problem
The digital social community is said to be tailored to you - but it’s filled with hate. Try as we might, we cannot escape the outrage of the attention economy.
We understand for most people, a social media exodus is not an option. <br /> <br />
Enter Elm.<br /> <br />

# The Data
Data was sourced from Twitter using Twint. The accounts were selected for their ecletic humor, inspirational quotes, and emotional intelligence. <br /> <br />
The following accounts were sourced to fine-tune our GPT-2 language model:
1. Simon Sinek
2. Brene Brown
3. Conan O'Brien
4. Lex Fridman
5. Tim Siedell
6. Dalai Lama
7. Pourmecoffee
8. Steve Martin

<img src="https://github.com/Stenke/Less-Fake-More-Good-News-Classification/blob/main/Images/pd-data-table-example.png" width="1100" length="1600"/>



# Methods
Elm is a languaged model based on the GPT-2 Simple library by Max Woolf. 
 

Analysis of frequency distributions:
<img src="https://github.com/Stenke/Less-Fake-More-Good-News-Classification/blob/main/Images/real-fake-top-words.png" width="1200" length="2000"/>

Next, Train-Test-Split was employed with a 20% test size. Our dependent variable was the labeled data columm where 1 is Real and 0 is Fake (changed using LabelEncoder). Processed text data was used for explanatory variables with 300,000+ columns. Using Sci-Kit Learn's TF-IDF Vectorizer, trigrams were created and word count limits were tested with best results at 200,000. And now we're ready for modeling...

<img src="https://github.com/Stenke/Less-Fake-More-Good-News-Classification/blob/main/Images/tfidf-params.png" width="1200" length="2000"/>

In order to classify our text data, seven classifier models were explored:
  1. Logistic Regression
  2. Decision Tree
  3. Gaussian Naive Bayes
  4. Random Forest
  5. Gradient Boosting
  6. XGBoost
  7. SVM - Sigmoid & Linear Kernels
  
Model performance was evaluted based on various metrics - Accuracy, Precision, Recall, F1-Score, and Average Precision. Additionally, computational speed was considered since the viability of our model in production will depend on how quickly we can run the model. In the case of our business problem, a model to help classify text so that real news rises to the top in a recommender system, Precision seems the most important. Precision in our case means that news that we label as real is truly real (with little false positives). Validating misinformation is dangerous and worse than no information at all (shoutout to Naruto for that notion - watching it with my lil' sis over the holiday).

A few models were chosen for GridSearchCV based on out-of-box performance. The winners were Logistic Regression, Gradient Boosting, and SVM. XGBoost was toyed with but turns out the model is smarter than my parameter tuning attempts. An example of performing GridSearch can be found below:

<img src="https://github.com/Stenke/Less-Fake-More-Good-News-Classification/blob/main/Images/Gradient-Boost-GridSearch.png" width="2000" length="2200"/>

# Findings
A couple models made the final cut and deserve further exploration in the context of a greater system. These include Logistic Regression, for its speed and over-indexing for precision (which could prove to be a boon). The other model was SVM using a sigmoid kernel. This ran at a relatively fast speed, had the highest accuracy, and a better balance between precision and recall.

### 1. Logistic Regression:

#### Over-Indexing for Precision
<img src="https://github.com/Stenke/Less-Fake-More-Good-News-Classification/blob/main/Images/log-reg-high-precision.png" width="700" length="900"/>

#### Highest Accuracy & F-1 Score
<img src="https://github.com/Stenke/Less-Fake-More-Good-News-Classification/blob/main/Images/log-reg-high-accuracy.png" width="700" length="900"/>

### 2. SVM - Sigmoid Kernel


#### Highest Overall Accuracy & F-1 Score
<img src="https://github.com/Stenke/Less-Fake-More-Good-News-Classification/blob/main/Images/svm-high-accuracy.png" width="700" length="900"/>

As mentioned earlier, each of these models could be selected as the top model depending on the context and first-order goals. Logistic Regression's strength is its speed and minimal computational complexity. Depending on parameter tuning, Logistic Regression has the highest Precision (95.2%) with fake news labeled as real or the second-highest overall Accuracy (81.5%) and F1-Score (70.3%) of any model (even the fancy ensemble ones).

SVM using a Sigmoid Kernel performed best overall in terms of Accuracy (82.2%) and F1-Score (72.5%) with a compute time of just over 5 seconds. Is a 0.70% increase in accuracy worth it for an additional 4.7 second compute time? Well, I think that question may be above my pay grade, but I'd say no. Which means the winning model (that I almost chose not to even bother with) is the winner of the great news classification marathon.

## Conclusion
Addressing misinformation in the digital era is one of the most consequential challenge members of the tech community face. My brief foray into classification has shown me just how difficult this problem is. On one end, we have to create classifiers and recommender systems in the attention economy of today with  its huge swaths of text-based information. On the other hand, we have to remember that any decision we make has nuanced consequences - if you choose to optimize only real news rising to the top, what happens to posts that were classified as fake when they were in fact real? Even further, at what point do we step on First Amendment rights by pushing away posts (even if it's malicious)? 

At the end of the day, we created a model that is able to classify news text as fake or real with 81.5% accuracy in just about half a second. On a perosnal note, this was an informative first step towards addressing the issue of disinformation on the web while expanding my knowledge of NLP and the murky waters of this issue.

Again, it is our intention that such a classifier is used in conjunction with a recommender system. In this way, the classifier is out of site allowing for real news (even if biased) to rise to the top of the feed. This is a different approach than others which choose to label posts with a warning after the fact or remove  retroactively - both which causes outrage and further entrenches a user's belief.

As a side note, the best solution may be to create multiple classifiers that address different topics and increase focus on information that has the potential for large consequences. 

Finally, there are clear ways in which we could improve our classifier. First, increase the diversity of text data - many of our posts were related to the 2016 election which reduces the generalizability of our model. Second, increase the amount of text data overall - 2050 rows of posts are not enough for a robust classifier. Third, improve the quality of data through hand-labeling by experts - though expensive, it is important considering the implications. Fourth, different NLP techniques could be used along with additional algorithms such as a CNN. I'm sure there are more, but I'll stop here.

A special thanks to Ibiki Morino from Naruto for the apropos inspiration for this project.
