# list of fruits
fruits=['apple','orange','mango']
# adding kiwi to the list
fruits.append('kiwi')
print(fruits)
# replacing mango with guava
fruits[2]='guava'
# adding berry to the list
fruits.append('berry')
print(fruits[3])
# inserting watermelon at 0th index
fruits.insert(0,'watermelon')
print(len(fruits))
print(fruits)

print(fruits.index('orange'))
# pop orange
fruits.pop(2)
print(fruits)