# users_test
Application that handles user registration and authentication.

Used Django, and Django-crispy-forms for additional styling.

Allows users to register, login, logout, and redirect to an index page.

# Index Page
![IndexPage](https://user-images.githubusercontent.com/64391008/163488338-1996731f-34e4-41bc-b955-547212677316.PNG)

This is supposed to simulate a navigation bar landing/index page for a website with relevant Login/Register links.


# User Registration
![RegisterPage](https://user-images.githubusercontent.com/64391008/163488282-fcb92130-c36c-450c-b244-323967fe9d07.PNG)

Used Django's UserCreationForm method and modified it to add an additional email field (not included).
This stores the user to an SQLite database, which can then be used to log in with. Has additional Django-included requirements for verifying valid input, but chose to hide those in the CSS for visual simplicity for this example.

# Login
![LoginPage](https://user-images.githubusercontent.com/64391008/163488415-f0c41495-1148-4f9f-b429-8976310705d0.PNG)

Log in with an existing user.

# Logout
![LogoutPage](https://user-images.githubusercontent.com/64391008/163488464-c992e39b-7cc6-40d6-b368-4ce98d18a4ae.PNG)

Simple logout page, which asks if you'd like to log in again. (Appears at top of page similar to a navbar).

# CSS
Created some simple CSS designs to add a little styling.
