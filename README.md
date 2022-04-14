# users_test
Application that just handles user registration and authentication
Used Django, Django-crispy-forms
Allows users to register, login, logout, and redirect to an index page.

# Index Page
![IndexPage](https://user-images.githubusercontent.com/64391008/163481234-682ff49b-8a50-4a1d-9907-f720aecf9a6f.PNG)
This is supposed to simulate a landing/index page for a website.
But because this is only supposed to be a registration/login application to plug into a website, I included nothing else but the navbar with the login and register links.

# User Registration
![RegisterPage](https://user-images.githubusercontent.com/64391008/163481420-20f3cfa5-d348-45ad-be0e-3814e6fea403.PNG)
Used django's UserCreationForm method and modified it to add an additional email field (not included).
This stores the user to an SQLite database, which can then be used to log in with.


![LoginPage](https://user-images.githubusercontent.com/64391008/163481408-c49b5ea5-d0ae-477f-a2c2-0b6467f66992.PNG)
Log in with an existing user.

![LogoutPage](https://user-images.githubusercontent.com/64391008/163482429-c393905b-40b4-4188-b8ae-8d661745a44e.PNG)
Simple logout page, which asks if you'd like to log in again.

# CSS
Included simple CSS designs to add a little flavor
