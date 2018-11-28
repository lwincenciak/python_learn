friends = ["Freddie", "Brian", "Roger", "John", "Mary", "Roger", "Jim"]
print(friends)
print(friends[1])  # [index] starts with 0
print(friends[-1])  # last element
print(friends[1:])  # lists elements from index 1 to end
print(friends[1:3])  # list elements from index 1 to 3 not including 3
friends[0] = "Mercury"
print(friends[0])
friends[0] = "Freddie"
lucky_numbers = [44, 8, 5, 17, 13, 2, 98, -5]
# friends.extend(lucky_numbers)
friends.append("Phoebe")
friends.insert(1, "Leszek")
print(friends)
friends.remove("Leszek")
print(friends)
print(friends.index("John"))
print(friends.count("Roger"))
friends.sort()
lucky_numbers.sort()
lucky_numbers.reverse()
friends2 = friends.copy()
print(friends)
print(friends2)
print(lucky_numbers)
friends.pop()  # delete last element
friends.clear()  # delete all elements
