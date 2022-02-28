# Dictionary list can be changed, because of that a dictionary
# we need to find something that isn't changable. 
dictionary = {
    '123': [1,2,3],
    '123': 'hello'
    # True: 'hello'
    # [100]: True
}

print(dictionary['123'])

