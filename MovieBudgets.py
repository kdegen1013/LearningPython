'''
For this project, your program should do the following:

1. Calculate the average budget of all movies in the data set.
2. Print out every movie that has a budget higher than the average you calculated.
3. You should also print out how much higher than the average the movie's budget was.
4. Print out how many movies spent more than the average you calculated.

Challenge:
If you want a little extra challenge, allow users to add more movies to the data set before running the calculations.

You can do this by asking the user how many movies they want to add, which will allow you to use a for loop and range
to repeat some code a given number of times. Inside the for loop, you can write some code that takes in some user input
and appends a movie tuple containing the collected data to the movie list.

'''

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

print("Welcome to the movie budget problem.")
answer = input("Would you like to add your movies? Enter Yes or No.").upper()

if answer == 'YES':
    more_movies = int(input("How many movies do you wish to enter? "))
    for num_answer in range(1, more_movies + 1):
        name = input("Enter name: ")
        budget = int(input("Enter budget: "))
        movies.append((name, budget))

print("\n")
num_movies = 0
sum_movies = 0
num_abovemovies = 0

for eachmovie in movies:
    num_movies = num_movies + 1
    sum_movies = sum_movies + eachmovie[1]

avg_movie = sum_movies / num_movies

print(f"The average movie budget was ${avg_movie:,.2f}")
print("\n")
for eachmovie in movies:
    if eachmovie[1] > avg_movie:
        num_abovemovies = num_abovemovies + 1
        print(
            f"{eachmovie[0]} had a budget of ${eachmovie[1]:,.2f} which was ${(eachmovie[1] - avg_movie):,.2f} more than the average budget.")
print("\n")
print(f"This means there were {num_abovemovies} movies above the average budget.")
