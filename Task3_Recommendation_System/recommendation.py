print("Movie Recommendation System")

movies = {
    "action": ["Avengers", "Batman", "Mission Impossible"],
    "comedy": ["Mr Bean", "The Mask", "Home Alone"],
    "romance": ["Titanic", "The Notebook", "La La Land"],
    "horror": ["Conjuring", "Annabelle", "Insidious"]
}

user = input("Enter your favorite genre (action/comedy/romance/horror): ").lower()

if user in movies:
    print("Recommended movies:")
    for movie in movies[user]:
        print("-", movie)
else:
    print("Sorry, genre not found.")
