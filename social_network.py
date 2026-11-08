class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network!")
            return
        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = ", ".join(friend.name for friend in person.friends)
            print(f"{name} is friends with: {friend_names}")

if __name__ == "__main__":
    network = SocialNetwork()

    # Add people (6+)
    for name in ["Alex", "Jordan", "Morgan", "Taylor", "Casey", "Riley"]:
        network.add_person(name)

    # Edge case: duplicate person
    network.add_person("Alex")  # "Alex already exists in the network!"

    # Create friendships (9 total)
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")
    network.add_friendship("Jordan", "Casey")

    # Edge cases: nonexistent people
    network.add_friendship("Jordan", "Johnny")  # "Friendship not created. Johnny doesn't exist!"
    network.add_friendship("Ghost", "Alex")     # "Friendship not created. Ghost doesn't exist!"

    # Edge case: duplicate friendship (should not double up)
    network.add_friendship("Alex", "Jordan")

    network.print_network()

"""
DESIGN MEMO

A graph is the right structure for a social network because friendships are
relationships between equals. People are nodes and friendships are edges, and
a friendship is bidirectional: if Alex is friends with Jordan, Jordan is
friends with Alex. A graph models this directly, and any person can connect
to any number of others with no required starting point or hierarchy.

A list wouldn't work well because it only stores items in a sequence. It has
no way to express who is connected to whom, so I'd have to search through
the whole list to find a person's friends. A tree wouldn't work either. Trees
have one root, a parent-child hierarchy, and no cycles. In my test network,
Alex, Jordan, and Taylor are all friends with each other, which forms a
cycle. Real social networks are full of these cycles, and a tree can't
represent them.

I used an adjacency list: each Person stores a list of their friends, and the
SocialNetwork stores a dictionary of people by name. This made lookups fast.
Checking whether a person exists, or fetching them to add a friendship, is
O(1) with the dictionary. Adding a friendship is also fast, though checking
for duplicates means scanning the friends list, which is O(d) where d is the
number of friends that person has. Printing the network is O(V + E) since it
visits every person and every friendship.

The main trade-off is memory versus lookup speed. An adjacency list only
stores friendships that exist, so it uses far less space than an adjacency
matrix for a large, sparse network like a social platform. The downside is
that checking whether two specific people are friends takes O(d) instead of
O(1).
"""