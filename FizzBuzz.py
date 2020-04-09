'''
Create a program to recreate FizzBuzz

One player starts by saying the number 1.
Each player then takes it in turns to say the next number, counting one at a time.
If the number is divisible by 3, instead of saying the number, the player should say, "Fizz".
If the number is divisible by 5, instead of saying the number, the player should say, "Buzz".
If the number is divisible by 3 and 5, instead of saying the number, the player should say, "Fizz Buzz".
If you make a mistake, you're usually eliminated from the game, and the game continues until there's only a single player remaining.
'''


for number in range(1,101):
	if number %3 == 0 and number%5:
		print("Fizz Buzz")
	elif number %3 == 0:
		print("Fizz")
	elif number %5 == 0:
		print("Buzz")
	else:
		print(number)