def main():
    # Open sample sentiment words score file
    afinnfile = open("AFINN-111.txt")
    scores = {}  # initialize an empty dictionary
    for tweet in afinnfile:
        term, score = tweet.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    print(scores)  # Print every (term, score) pair in the dictionary

    # Open Tweets file
    tweetFile = open("output.txt")
    for tweet in tweetFile:
        tweet_words = tweet.split()
        sentiment_score = 0
        # Find Sentiment Score for each tweet
        for word in tweet_words:
            if word in scores:
                sentiment_score += scores[word]
        print(tweet + " : " + str(sentiment_score))


if __name__ == '__main__':
    main()
