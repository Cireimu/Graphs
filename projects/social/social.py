import random
from util import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        if num_users < avg_friendships:
            print("Number of users must be greater than average num of friendships")
            return

        # add users, with user name being based on num_users
        # generate friendship combinations
        # shuffle all possible friendships
        # create friendships for first pairs based off of total // 2
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        potential_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                potential_friendships.append((user_id, friend_id))

        random.shuffle(potential_friendships)
        for i in range(num_users * avg_friendships // 2):
            friendship = potential_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT

        # set up queue
        # queue up user_id
        # while queue is not empty, continue going through
        # initialize path and dequeue it
        # get the last id from the path and make it cur_id
        # check if cur_id has been visited
        # if not then add cur_id as a key and the path as value
        # go through the friends of cur_id
        # create a copy of the path, append each friend, enqueue the new path
        # return visited

        q = Queue()
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()

            cur_id = path[-1]

            if cur_id not in visited:
                visited[cur_id] = path

                for friend in self.friendships[cur_id]:
                    new_path = list(path)

                    new_path.append(friend)

                    q.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 3)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
