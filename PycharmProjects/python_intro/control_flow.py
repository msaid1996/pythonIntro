age = input("what is your age?   ")

if 75>int(age)>70:
    print("you are between 70-75")
elif int(age) > 75:
    print("you are over 75")
else:
    print("you are less than 70")

#---ex
#greet - then --> tell me what films you can watch based on my age
#list all films available
#input rating - pg, 12, 15, u
#who is avaliable to view it
print("EX------")

print("Hello, I'm here to help you to find films based on age ratings")
print("Select age ratings: pg, u, 12, 15")
movie_rate = input("What is your age rating?  ")

if movie_rate == 'pg':
    pg_movies = ["smurf", "pets","dogs and cats"]
    print("parental guidance is needed!")
    print("The movies selected are:")
    print(pg_movies)
    print("Enjoy the movie!")

elif movie_rate == "u":
    u_movies = ["frozen", "bambi", "cars"]
    print("The movies selected are:")
    print(u_movies)
    print("Enjoy the movie!")

elif int(movie_rate) == 12:
    twelve = ["harry potter", 'ring', 'captain sparrow']
    print("Only above 12 years old are allowed!")
    print("The movies selected are:")
    print(twelve)
    print("Enjoy the movie!")

elif int(movie_rate) == 15:
    fiften = ["parasite", 'abcdef', 'invinsible man']
    print("Only above 15 years old are allowed!")
    print("The movies selected are:")
    print(fiften)
    print("Enjoy the movie!")

else:
    print("age rating is unknown. Please try again. Thank you")




