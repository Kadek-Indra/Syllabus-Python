# itterable and membership

movies = {"Avengers" : "1",
          "Spider-man" : "2",
            "Fantastic four" : "3",
              "Thunderbolts" : "4",
                "X-men" : "5"}

print("WELCOME TO XXI CINEMASS")
print("MOVIES OF THE MONTH  ")
for title, studios in movies.items():
    print (f"-{title:15} > {studios}")
choice = input("Enter the movie's title : ").capitalize()

if choice in movies:
    print(f"Your movies is {choice} in studios {movies[choice]}")
else:
    print(f"{choice} are not in the cinemas")