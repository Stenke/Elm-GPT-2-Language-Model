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
Elm is a languaged model based on the GPT-2 Simple library by Max Woolf. Before fine-tuning, Twitter data was cleaned, removing links, emojis, and hashtags. This data was then fed into GPT-2 Simple which has its own tokenizer for processing text data. The 355M paramater model was selected as we felt the improved performance as worth the longer training time. The model was trained using Google Colab's NVIDIA processor.<br /> <br />

After training for 10,000 steps, we generated 100,000 tweets with a temperature setting of 0.8. We then performed extensive EDA on the real and generated tweets to determine similarities and differences.

Normalized Top Words - Real vs. Generated Tweets:
<img src="https://github.com/Stenke/Tweets-to-Stories-to-Topics/blob/main/Visuals/word_freq_rvg2.png" width="1200" length="2000"/>

Following EDA, we decided to use an adhoc classification method of validating performance. The idea is if the classifiers perform at or near 50%, our generated tweets are good replicas of the real things. For the classification modeling, we randomly sampled 15,000 tweets from the real and generated datasets for an entire set of 30,000. We tested both Naive Bayes and Random Forest Classifiers.<br /> <br />

We were pleased with a classification accuracy of 62.52% for the random forest classifier after tuning via grid-search. The pre-tuned classifiers overfit the training set performing at or near perfect accuracy. After examiningg the feature importances, we realized this is likely because certain words appear in either the real or generated tweets that don't appear in the other (ex. emptywheel).

Random Forest Classifier: Feature Importance
<img src="https://github.com/Stenke/Tweets-to-Stories-to-Topics/blob/main/Visuals/rf-feature-import-plot.png" width="1200" length="2000"/>

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
