#printing variables with strings
'''
likes = input("what do you like")
hates = input("what do you hate")

print("he likes:",likes)
print("he hates:",hates)
'''

'''
output: what do you like - user input
what do you hate - user input

he likes: user input
he hates: user input
'''
'''
#printing variables between strings

name = input("what is your name:")

print('hi',name,'welcome')

print("Hi %s ,welcome" %name)
'''

#efficient method

name = input("what is your name:")
age = input("what is your age \n")

gender = input("what is your gender \n")

print("Hi %s, welcome. You are %s years old %s" %(name,age,gender))
