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