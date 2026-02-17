# Edit this program by calling the 'login' function
# - Ask the user for their username and password to use as arguments for the function call
def login(username: str, password: str):
    if username == "FunTech" and password == "secretPassword":
        print("Logged in!")
    else:
        print("Either your username or password is incorrect...")
