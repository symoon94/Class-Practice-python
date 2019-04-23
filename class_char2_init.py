###
### Class method1
### - __init__
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

user1 = instagram(62, 169, 110, 27)
user2 = instagram(68, 370, 67, 9)
userlist = [user1, user2]

print(f"user 1 influence_score: {user1.influence_score(289, 101, 84)}")

for i in range(len(userlist)):
    print(
        f"user{i+1} engagement_score: {userlist[i].engagement_score()} \n"
        f"user{i+1} popularity_score: {userlist[i].popularity_score()}"
        )


