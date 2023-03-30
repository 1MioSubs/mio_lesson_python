first_list = ['test1', 'python', 'java', 'minecraft']
print(first_list)
print(first_list[1])
print(first_list[1].title())
print(first_list[-1].title())

message = "My first video game - " + first_list[-1].title()
print(message)


print(first_list)
first_list[0] = "programing"
print(first_list[0].upper())
print(first_list)


print(first_list)
first_list.append("append-list")
print(first_list[-1].upper())
print(first_list)


new_list = []

new_list.append("game")
new_list.append("program")
new_list.append("windows")

print(new_list)

new_list.insert(1, "ubuntu")

print(new_list)

del new_list[0]
print(new_list)

new_pop_list = ['dota', 'cs', 'nfs', 'minecraft']
print(new_pop_list)
first_pop_del = new_pop_list.pop()
print(new_pop_list)
print(first_pop_del)


new_pop_list2 = ['dota', 'cs', 'nfs', 'minecraft']
print(new_pop_list2)
second_pop_del = new_pop_list2.pop(2)
print(new_pop_list2)
print(second_pop_del)


del_list_3 = ['1', '2', 'del3', '4']
print(del_list_3)
too_expensive = "del3"
del_list_3.remove(too_expensive)
print(del_list_3)