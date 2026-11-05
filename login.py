def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login successful"
    else:
        return "Invalid credentials"

print(login("admin", "admin123"))
