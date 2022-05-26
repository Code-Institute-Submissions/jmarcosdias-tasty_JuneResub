# <em>What's for Dinner</em> website

This project is about developing a recipe website.

## Table of Contents

1. [Design](#design)
2. [Initial setup](#initial-setup)
3. [Project follow-up](#project-follow-up)
4. [Testing](#testing)
   1. [Validator tests](#validator-tests)
   2. [Automated tests](#automated-tests)

## Design

Putting myself in the user's position and trying to anticipate their needs, here are some examples of questions I have asked myself:

* Why would a user wish to visit the <em>What's for Dinner</em> website?
* What would make the users return?

After some design thinking work, I came up with the following.

As a site user, I would like to:
* Take a look at a list of recipes, from where I can select a recipe to view.
* Spend some time viewing recipes, one recipe at a time, until I decide on one to prepare for dinner.
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

I decided to not include the edit and view recipe wireframes here, so as to not overload this section. These wireframes are very similar to the create recipe wireframe, here included.

The log in and create account buttons are visible in the view recipe list page, in case the user is not logged in.

Together, the wireframes below were a great starting point for the development of the <em>What's for Dinner</em> website.

#### Create account

![image](https://user-images.githubusercontent.com/87392921/168344041-18c22795-d9e1-4bc3-a16a-f4a524a72b81.png)
![image](https://user-images.githubusercontent.com/87392921/168336912-b00816a5-f39a-4b38-bd31-109a8fc72a27.png)

For a better user experience, the create account user story is implemented with a Username field instead of the initially wireframed First Name and Last Name fields. This makes the registration process smoother and more likely to register a larger number of users.

The text here presented in the create account wireframe was moved to the view recipe list page which was also decided to be the the landing page. This decision was taken at a final stage of the project. The wireframes here presented helped a lot to kick off the development but this does not mean things cannot change.

#### View recipe list

![image](https://user-images.githubusercontent.com/87392921/168376267-d1926b42-ba3a-4613-ab98-d75a4848698f.png)
![image](https://user-images.githubusercontent.com/87392921/168343499-e5c7ccbf-5992-4bc1-83ad-e916ef1799ae.png)

#### Create recipe

![image](https://user-images.githubusercontent.com/87392921/168366511-061497bd-3983-4409-b4f5-132a579446f0.png)
![image](https://user-images.githubusercontent.com/87392921/168367108-16854308-335c-4a3d-88d9-526afbd10c9b.png)

## Initial setup

Before starting working on the user stories, the following steps were taken, to prepare the environment:

* Install django framework 
* Install gunicorn http server
* Install dj-database-url python package to use with postgresql
* Install psycopg2 postgresql data base adapter
* Install dj3-cloudinary-storage django package for integration with cloudinary
* Create a new django project, named tasty_project
* Create a new app, named whats_for_dinner_app
* Update settings.py with the new app, allowed hosts, cloudinary settings, getting of secret key and database url, templates dir, root url configuration, wsgi application, static url and media url configuration
* Update urls.py and admin.py, allowing django admin module to manage recipes
* Insert some recipe sample records, preparing for the development of the view recipe list functionality

## Project follow-up

This section presents the status of the development of the <em>What's for Dinner</em> website along the way.

### Start the project with 8 user stories to do

Fri May 13 20:40:28 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/168377764-24ce531b-60ae-4e17-8682-23b9382b96d0.png)

### Start working on the view recipe list user story

Fri May 13 20:40 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/168442707-5aba4960-23bb-4d9a-8983-f8be1292c173.png)

### Recipe list user story done

Tue May 17 01:25:41 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/168701190-04a767c6-c4ab-40da-836f-082288f5e7e2.png)

### Start working on the view recipe user story

Tue May 17 22:12:05 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/168908599-94cd32ba-0ef3-43e2-ac74-d0b5298a61b1.png)

### View recipe user story done

Tue May 17 23:57:00 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/168925325-f6e48f7c-cd82-4efb-9eca-2f783cf19bb9.png)

### Start working on the account management user stories

Wed May 18 22:58:06 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/169162297-8dfc8815-2ca1-4063-9881-414b5d80d287.png)

### Account management user stories done

Thu May 19 01:06:10 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/169174789-4f0d161c-e1d7-47ba-b0b6-5d4f09d1ab90.png)

### Start working on the delete recipe user story

Fri May 20 11:13:08 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/169505968-070db246-463f-48e1-8a3c-2ce45293eeee.png)

### Start working on the create recipe user story

Fri May 20 17:34:00 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/169572344-c5537216-93b4-439b-bf73-088f10793026.png)

### Start working on the edit recipe user story

Sun May 22 11:14:15 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/169690266-99ff194d-55c2-4bc6-ad39-e6a7c0396556.png)

### Create, edit and delete recipe user stories done

Mon May 23 20:54:13 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/169895704-81e96644-0103-480f-92f7-35666739a9cb.png)

### Create tasks for improving automated tests and for a better design of the landing page

At this stage, the application is working.

There was only one user story in the to do column of the Kanban board so it was moved to the in progress column.

**USER STORY: Welcome page**

It was decided to implement the welcome page in the view recipe list page. This way a new user and a returning user will have access to a quick explanation about the website each time they visit it. This user story consists in updating the view recipe list with a welcome explanation.

There is some time before the delivery day. This way the following new tasks were indentified and placed into the Kanban board.

**TASK: Improve appearance of the landing page**

Landing page is working but not yet looking good. Some elements are very close together and this makes the website look unfinished. Some design work is needed in the landing page and then new similar tasks will be created for the remaining pages.

**TASK: Improve automated tests**

Automated tests were developed for view recipe list and view recipe but there are no automated tests for create, edit and delete recipe. The automated tests must be reviewed in order to cover at least the CRUD functionalities.

Mon May 23 21:32:50 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/169899937-1304d0f8-3994-48e8-aa0b-d73944d69fe4.png)

### Changes to the landing page contents and appearance done

The landpage is now with the intended design and content for this version of the project, to be delivered on 28th of May.

New tasks were created to style each of the remaining pages.

The automated tests task was moved back to the to do column. The tasks in the to do column are now being prioritized.

Wed May 25 02:35:00 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/170159595-2bb948af-df14-485a-b00c-b4e073f851af.png)

### Styling the main pages

Tasks updated and repositioned accordingly to the current need. One task was renamed to follow the naming convention of others (task #10). One task was created (task #16).

The focus now is on styling the main pages of the project.

Wed May 25 21:25:00 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/170360558-e4c97f7b-5eec-4edc-a36c-67e469946588.png)

### Landing page, recipe list and create recipe are styled

Wed May 26 00:27:00 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/170385433-fc2750c2-0524-4beb-aaf8-24334cfebd6a.png)

### View and edit recipe pages are styled

Wed May 26 01:42:00 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/170392040-e75f599e-de9b-4a1c-b5c3-f633c38424e9.png)

### Styling the login, logout and register pages

Tasks updated and repositioned accordingly to the current need. One task was created (task #17).
The focus now is on styling the authentication-related pages.

Wed May 26 12:52:00 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/170482563-bb187a72-c8b2-4933-ad65-47c67a7d52f6.png)

## Testing

### Validator tests

In order to improve the readability and consistency of the Python code, I have used the http://pep8online.com code checker.

![image](https://user-images.githubusercontent.com/87392921/169820413-28dc900d-6301-4a53-9154-58250be27b84.png)


### Automated tests

python3 manage.py test --keepdb













