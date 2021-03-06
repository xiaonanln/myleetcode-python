class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """


twitter = Twitter()

#  User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

#  User 1's news feed should return a list with 1 tweet id -> [5].
print twitter.getNewsFeed(1);

#  User 1 follows user 2.
twitter.follow(1, 2);

#  User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

#  User 1's news feed should return a list with 2 tweet ids -> [6, 5].
#  Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
print twitter.getNewsFeed(1);

#  User 1 unfollows user 2.
twitter.unfollow(1, 2);

#  User 1's news feed should return a list with 1 tweet id -> [5],
#  since user 1 is no longer following user 2.
print twitter.getNewsFeed(1);