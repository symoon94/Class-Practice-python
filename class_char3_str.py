###
### Class method2
### - __str__
###

# For example,
# 영향력: (impressions/reach) * profile visits
# 팔로워 참여도: (좋아요/팔로워) * 100
# 인기도: (팔로워-팔로잉)/포스트

class instagram:
    def __init__(self, likes, follower, following, posts):
        self.likes = likes
        self.follower = follower
        self.following = following
        self.posts = posts

    def influence_score(self, impressions, reach, profile_visits):
        score = round((impressions/reach) * profile_visits, 2)
        return score

    def engagement_score(self):
        score = round((self.likes / self.follower) * 100, 2)
        return score

    def popularity_score(self):
        score = round((self.follower - self.following) / self.posts, 2)
        return score

    def __str__(self):
        return str(self.likes)  # string이 출력되도록 해야함. 그렇지 않을 경우 TypeError.


user1 = instagram(62, 169, 110, 27)
user2 = instagram(34, 302, 202, 106)

print(user2)    # 34

# 만약 __str__이 없다면,
# print(user2)
# e.g. <__main__.instagram object at 0x10a55bb00>

