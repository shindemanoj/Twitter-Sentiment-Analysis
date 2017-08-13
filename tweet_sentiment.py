import sys
import json


def hw():
    print('Hello, world!')


def lines(fp):
    print(str(len(fp.readlines())))


def main():
    # sent_file = open(sys.argv[1])
    # tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    afinnfile = open("AFINN-111.txt")
    scores = {}  # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    print(scores)  # Print every (term, score) pair in the dictionary

    tweetFile = open("output.txt")
    tweets = {}  # initialize an empty dictionary
    for line in tweetFile:
        tweets = json.loads(line)
        print(tweets)

if __name__ == '__main__':
    main()
