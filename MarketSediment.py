import tweepy

# Twitter API credentials
API_KEY = '(your key)'
API_SECRET = '(your secret)'
ACCESS_TOKEN = '(your token)'
ACCESS_TOKEN_SECRET = '(your token secret)'

# Keywords to listen for
keywords = ["market", "investment", "stock", "$AAPL"]

# Function to authenticate with Twitter API
def authenticate():
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

# Function to fetch tweets containing the keywords
def fetch_tweets(api, keywords):
    for keyword in keywords:
        print(f"Listening for tweets containing '{keyword}':")
        for tweet in tweepy.Cursor(api.search_tweets, q=keyword, tweet_mode='extended').items():
            print(tweet.full_text)

# Main function
def main():
    api = authenticate()
    fetch_tweets(api, keywords)

if __name__ == "__main__":
    main()
