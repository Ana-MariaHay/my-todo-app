import webbrowser

user_term = input("enter a search term: ").replace(" ", "+")

webbrowser.open(f"https://google.com/search?q={user_term}")