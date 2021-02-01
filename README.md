# Tweets-to-Stories-to-Topics
Potential for phase 4 project. First, scape Twitter data from people whose minds' I admire. Then, train GPT-2 on said Tweets using Google Colab. Next, generate short stories from Tweets (280 characters is a bit too short-from for my tastes... we could use a bit more attention). Finally, we'll topic model to explore our stories and prepare to feed as recommended reads. <br /> <br />
<p align="center">
  <img src="https://github.com/Stenke/Tweets-to-Stories-to-Topics/blob/main/Visuals/pirate-cat.jpg" width="600"   length="800" />
</p>


# Business Problem
Misinformation and disinformation is an increasing consideration in the public sphere. For the past 5 years, we've seen governments, news agencies, and social media companies grapple with misleading news and social posts. As we enter 2021, it seems more important than ever to find a consensus on information - what is true and factual. 

Social media is ingrained in societies across the world - billions of people turn to their Facebook groups, Twitter "subject-matter" experts, and other digital social outlets for news that shapes their view on the world. And with the potential virality of one false tweet, misinformation can become "factual" in the eyes of millions; a 21st-century threat that we need to grapple with. 

One common method social media companies have employed is labeling information as "disputed" or "false". Another is to take down information after the fact. Both of these have an adverse effect - those who've had posts labeled or removed are made more sure that their information is true.

I've decided to try another tactic: focus on the good, show less bad. To do so, I've compared various classification models to label text (both social posts and website news stories) as either "Real" or "Fake". The intention is to find a classification model that is both accurate and lightweight enough to be useful in production cases.

Once we have a trained classifier, we can combine it with a recommender system to rank truth and substantive content over false and inflaming. This is a key differentiation with the current norm of the attention commodity which often leads to division and outrage (as these better hold ones attention). The actual recommender system is beyond the scope of this project - we will stick to the first step of identifying the good news so that we can hype up our better angels.

# The Data
The data was sourced from Kaggle's Source Based Fake News Classification. It contains text and metadata scraped from 244 websites and labeled with the BS Detector Chrome Extension by Daniel Sieradski.

Note: We will be training our classifiers on data labeled by a classification algorithm (pretty meta, I know). In an ideal situation, we would have large datasets hand-labeled by experts.

<img src="https://github.com/Stenke/Less-Fake-More-Good-News-Classification/blob/main/Images/pd-data-table-example.png" width="1100" length="1600"/>

<img src="https://github.com/Stenke/Less-Fake-More-Good-News-Classification/blob/main/Images/news-text-example.png" width="12000" length="1800" />

Source: https://www.kaggle.com/ruchi798/source-based-news-classification

# Questions
The following questions will guide our analysis and modeling as we evaluate performance.

1. How to best use NLP to process text data?

2. What aglorithm(s) will perform best on text data?

3. What aglorithm(s) best balance computational costs and accuracy?

# Methods
Text data was initially explored with visualizations showing differences in real versus fake text data. Around 50 rows were removed due to NaN values leaving us with 2050 rows of text. Data was then processed through various NLP techniques including stopword removal, tokenization, and vectorization using TF-IDF. There is a class imbalance of 2/3 'fake' to 1/3 'real'. Initially, this imbalance was left as is. Later, SMOTE was explored though without any overall improvements. There was a similar experience with dimensionality reduction using TruncatedSVD. 

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
