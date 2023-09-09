# https://leetcode.com/problems/design-twitter/

from typing import List
import heapq
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)  # user -> set of folowees
        self.tweets = defaultdict(list)  # user -> list of [time, tweetId]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        self.follow(userId, userId)
        for followeeId in self.followers[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(
                    maxHeap, [count, tweetId, followeeId, index - 1])
        while maxHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(
                    maxHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(666, 1)
obj.postTweet(777, 2)
obj.postTweet(777, 555)
obj.postTweet(777, 7657)
obj.postTweet(777, 9808)
obj.postTweet(888, 3)
obj.postTweet(999, 4)
obj.postTweet(999, 5435)
obj.postTweet(123, 5)
obj.follow(666, 777)
obj.follow(666, 888)
obj.follow(666, 999)
obj.follow(999, 123)
obj.follow(312, 999)
obj.follow(222, 777)
obj.unfollow(222, 777)
param_2 = obj.getNewsFeed(666)
