def clean_dist(df, preproc_pipe='preproc_pipe'):  
    """
    Simple function for printing metrics for ML classification score.
    
    Parameters:
    df: full dataframe
    series: series with tweet as string, default is 'tweet'
    test_labels: labels for y_test
    
    Libraries:
    import spacy
    from nltk.corpus import stopwords
    import string
    import time
    import re


    Returns:
    Training + Testing scores for: precision, recall, accuracy, F1, average-precision.
    """
    
    total_vocab = []

    for tweet in df[preproc_pipe]:
        for word in tweet:
            total_vocab.append(word)
    print(len(total_vocab))
    print(len(set(total_vocab)))
    
    tweets_concat = []
    
    for tweet in df[preproc_pipe]:
        for word in tweet:
            tweets_concat.append(word)
    print(tweets_concat[0:5])
    len(tweets_concat)
    
    stops = ['i',
             'me',
             'my',
             'myself',
             'we',
             'our',
             'ours',
             'ourselves',
             'you',
             "you're",
             "you've",
             "you'll",
             "you'd",
             'your',
             'yours',
             'yourself',
             'yourselves',
             'he',
             'him',
             'his',
             'himself',
             'she',
             "she's",
             'her',
             'hers',
             'herself',
             'it',
             "it's",
             'its',
             'itself',
             'they',
             'them',
             'their',
             'theirs',
             'themselves',
             'what',
             'which',
             'who',
             'whom',
             'this',
             'that',
             "that'll",
             'these',
             'those',
             'am',
             'is',
             'are',
             'was',
             'were',
             'be',
             'been',
             'being',
             'have',
             'has',
             'had',
             'having',
             'do',
             'does',
             'did',
             'doing',
             'a',
             'an',
             'the',
             'and',
             'but',
             'if',
             'or',
             'because',
             'as',
             'until',
             'while',
             'of',
             'at',
             'by',
             'for',
             'with',
             'about',
             'against',
             'between',
             'into',
             'through',
             'during',
             'before',
             'after',
             'above',
             'below',
             'to',
             'from',
             'up',
             'down',
             'in',
             'out',
             'on',
             'off',
             'over',
             'under',
             'again',
             'further',
             'then',
             'once',
             'here',
             'there',
             'when',
             'where',
             'why',
             'how',
             'all',
             'any',
             'both',
             'each',
             'few',
             'more',
             'most',
             'other',
             'some',
             'such',
             'no',
             'nor',
             'not',
             'only',
             'own',
             'same',
             'so',
             'than',
             'too',
             'very',
             's',
             't',
             'can',
             'will',
             'just',
             'don',
             "don't",
             'should',
             "should've",
             'now',
             'd',
             'll',
             'm',
             'o',
             're',
             've',
             'y',
             'ain',
             'aren',
             "aren't",
             'couldn',
             "couldn't",
             'didn',
             "didn't",
             'doesn',
             "doesn't",
             'hadn',
             "hadn't",
             'hasn',
             "hasn't",
             'haven',
             "haven't",
             'isn',
             "isn't",
             'ma',
             'mightn',
             "mightn't",
             'mustn',
             "mustn't",
             'needn',
             "needn't",
             'shan',
             "shan't",
             'shouldn',
             "shouldn't",
             'wasn',
             "wasn't",
             'weren',
             "weren't",
             'won',
             "won't",
             'wouldn',
             "wouldn't",
             '!',
             '"',
             '#',
             '$',
             '%',
             '&',
             "'",
             '(',
             ')',
             '*',
             '+',
             ',',
             '-',
             '.',
             '/',
             ':',
             ';',
             '<',
             '=',
             '>',
             '?',
             '@',
             '[',
             '\\',
             ']',
             '^',
             '_',
             '`',
             '{',
             '|',
             '}',
             '~',
             "''",
             '""',
             '...',
             '``',
             'im',
             'https',
             'http',
             "'s",
             "n't",
             'https',
             'http',
             'amp']
    
    stops += ["'s", "n't", "like", "'m", "get", "'re", "day", "going", "good", 'something', 'look'
                   "new", "would", "today", 'today', 'would', 'one', '’', 'thank', 'back', 'go', 'make',
                   'want', 'right', 'know', 'see', 'way', 'really', 'let', 'first', 'say', 'rt', 'could',
                   'ca', "'ll", 'much', 'never', "'ve", 'take', 'every', 'got', 'man', 'year', 'yes', 'even',
                   'twitter', 'still', 'amp', 'thing', 'everyone', 'guy', 'im', 'talk', 'last', 'show', 
                   'look', 'made', 'need', 'also', 'two', 'book', 'https', 'http', 'well', 'come', 'little', 'watch',
                   'new', 'use', 'call', 'tweet', 'read', 'may', 'great', '\ufeff1', 'try', 'old', 'big', 'com',
                   'long', 'night', 'week', 'mean', 'keep', 'ask', 'name', 'lot', 'tonight', 'hard', 'always', 'sure',
                   'someone', 'ever', 'meet', 'stop', 'post', 'movie', 'eat', 'put', 'wait']
    
    tweets_nostops = [word for word in tweets_concat if word not in stops]
    
    tweets_dist = FreqDist(tweets_nostops)

    top_words = tweets_dist.most_common(32)

    x_val = [x[0] for x in top_words]
    y_val = [x[1] for x in top_words]

    twords = pd.DataFrame(y_val, index=x_val, columns =['Top_Words'])

    twords.plot(kind='bar', alpha=0.7, color='seagreen', figsize=(18,10), fontsize=16)
    plt.xlabel('Top Words')
    plt.ylabel('Word Frequency')
    plt.title('Most Frequent Words', fontsize=20)
    plt.xticks(rotation=70)
    plt.show()