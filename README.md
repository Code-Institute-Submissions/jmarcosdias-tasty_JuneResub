# <em>What's for Dinner</em> website

This project is about developing a recipe website.

## Table of Contents

1. [Design](#design)
2. [Project follow-up](#project-follow-up)

## Design

Putting myself in the user's position and trying to anticipate their needs, here are some example of questions I have asked myself:

* Why would a user wish to visit the <em>What's for Dinner</em> website?
* What would make the users return?

After some design thinking work, I came up with the following.

As a site user, I would like to:
* Take a look at a list of recipes, from where I can select a recipe to view.
* Spend some time viewing one recipe at a time, until I decide on one to prepare for dinner.
* Be able to use my smartphone to view the recipe I have selected, so that I can view any details of this recipe while I am cooking.
* Enjoy dinner, knowing I can count on <em>What's for Dinner</em> website next time.

I would return if I liked the user experience when browsing, reading, preparing/cooking the recipe and having dinner.

### User Stories

These are the users stories I have defined for the first version of the website.

* Welcome page: As a Site User I can view the welcome/landing page so that I can log in or create an account
* Create account: As a Site User I can create/register an account so that I can log in to the website
* Log in: As a Registered Site User I can log in to the website so that I can create a recipe, edit any recipe I created and delete any recipe I created
* Create recipe: As a Registered Site User I can create a recipe so that people can view this recipe in the website
* Edit recipe: As a Registered Site User I can edit a recipe I created so that people can view a better version of this recipe in the website
* Delete recipe: As a Registered Site User I can delete a recipe I created so that people can no longer view this recipe in the website
* View recipe list: As a Site User I can view a list of recipes so that I can select a recipe to view
* View recipe: As a Site User I can view a recipe I selected from the list of recipes so that I can learn how to cook this recipe

### Wireframes

Here are some of the wireframes I used to define what this first version of the <em>What's for Dinner</em> website will look like.

I decided to not include the edit and view recipe wireframes here, so as to not overload the this section. These wireframes are very similar to the create recipe wireframe, here included.

The log in and create account buttons are visible in the view recipe list page, in case the user is not logged in.

Together, the wireframes below are a great starting point for the development of the <em>What's for Dinner</em> website.

#### Create account

![image](https://user-images.githubusercontent.com/87392921/168344041-18c22795-d9e1-4bc3-a16a-f4a524a72b81.png)
![image](https://user-images.githubusercontent.com/87392921/168336912-b00816a5-f39a-4b38-bd31-109a8fc72a27.png)

#### View recipe list

![image](https://user-images.githubusercontent.com/87392921/168376267-d1926b42-ba3a-4613-ab98-d75a4848698f.png)
![image](https://user-images.githubusercontent.com/87392921/168343499-e5c7ccbf-5992-4bc1-83ad-e916ef1799ae.png)

#### Create recipe

![image](https://user-images.githubusercontent.com/87392921/168366511-061497bd-3983-4409-b4f5-132a579446f0.png)
![image](https://user-images.githubusercontent.com/87392921/168367108-16854308-335c-4a3d-88d9-526afbd10c9b.png)

## Project follow-up

This section presents the status of the development of the <em>What's for Dinner</em> website along the way.

### First set of user stories defined

![image](https://user-images.githubusercontent.com/87392921/168377764-24ce531b-60ae-4e17-8682-23b9382b96d0.png)

Before starting working on the user stories, the following steps were taken, to prepare the environment to work:

* Install django framework 
* Install gunicorn http server
* Install dj-database-url python package to use with postgresql
* Install psycopg2 postgresql data base adapter
* Install dj3-cloudinary-storage django package for integration with cloudinary
* Create a new django project, named tasty_project
* Create a new app, named whats_for_dinner_app
* Update settings.py with the new app, allowed hosts, cloudinary settings, getting of secret key and database url, templates dir, root url configuration, wsgi application, static url and media url configuration
* Update urls.py and admin.py to facilitate the use of django admin module
* Insert some recipe sample records to facilitate the development and dev-test of the recipe list functionality

### Starting with the view recipe list user story

![image](https://user-images.githubusercontent.com/87392921/168442707-5aba4960-23bb-4d9a-8983-f8be1292c173.png)










