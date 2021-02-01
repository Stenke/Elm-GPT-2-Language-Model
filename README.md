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
<br />
Twitter Account Contributors:
<br /> 
<img src="https://github.com/Stenke/Tweets-to-Stories-to-Topics/blob/main/Visuals/account-names-tweet-count.png" width="700" length="500"/>

<br />

# Methods
Elm is a languaged model based on the GPT-2 Simple library by Max Woolf. Before fine-tuning, Twitter data was cleaned, removing links, emojis, and hashtags. This data was then fed into GPT-2 Simple which has its own tokenizer for processing text data. The 355M paramater model was selected as we felt the improved performance as worth the longer training time. The model was trained using Google Colab's NVIDIA processor.<br /> <br />

After training for 10,000 steps, we generated 100,000 tweets with a temperature setting of 0.8. We then performed extensive EDA on the real and generated tweets to determine similarities and differences.

Normalized Top Words - Real vs. Generated Tweets:
<br /> <br />
<img src="https://github.com/Stenke/Tweets-to-Stories-to-Topics/blob/main/Visuals/word_freq_rvg2.png" width="1000" length="700"/>

Following EDA, we decided to use an adhoc classification method of validating performance. The idea is if the classifiers perform at or near 50%, our generated tweets are good replicas of the real things. For the classification modeling, we randomly sampled 15,000 tweets from the real and generated datasets for an entire set of 30,000. We tested both Naive Bayes and Random Forest Classifiers.<br /> <br />

We were pleased with a classification accuracy of 62.52% for the random forest classifier after tuning via grid-search. The pre-tuned classifiers overfit the training set performing at or near perfect accuracy. After examiningg the feature importances, we realized this is likely because certain words appear in either the real or generated tweets that don't appear in the other (ex. emptywheel).

Random Forest Classifier: Feature Importance
<br />

<img src="https://github.com/Stenke/Tweets-to-Stories-to-Topics/blob/main/Visuals/rf-feature-import-plot.png" width="600" length="400"/>
<br /> <br />

We then dove into a comparison of correctly versus misclassified data to understand the differences.<br /> <br />
<img src="https://github.com/Stenke/Tweets-to-Stories-to-Topics/blob/main/Visuals/class-vs-misclass-freq-dist.png" width="1400" length="1000"/>

# Findings
Include Tweet Examples

## Conclusion
Our goal was to create an optimistic and witty language model to produce Tweets catered to our preferences. Though there were some goofy tweets (as GPT-2 is prone to do), we were very happy with the overall performance. You can see when the model would get into a "groove" writing more witty or Dalai Lama-esque tweets. Though the model may not possess consciousness, it wrote some inspirational messages unique to the personalities it was trained on.

As a next step, we'll see how users react to these generated tweets. Getting access to GPT-3 would obviously improve performance as well. 
