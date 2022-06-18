# <em>What's for Dinner</em> website

## Table of Contents

1. [Purpose](#purpose)
2. [Features](#features)
3. [Design](#design)
   1. [User Stories](#user-stories)
   2. [Wireframes](#wireframes)
   3. [Data Model](#data-model)
4. [Initial setup](#initial-setup)
5. [Project follow-up](#project-follow-up)
6. [Testing](#testing)
   1. [Manual tests](#manual-tests)
   2. [Validator tests](#validator-tests)
   3. [Automated tests](#automated-tests)
7. [Deployment](#deployment)
   1. [How to deploy the site to heroku](#how-to-deploy-the-site-to-heroku)
   2. [How to deploy the site locally](#how-to-deploy-the-site-locally)
8. [Credits](#credits)


## Purpose

The <em>What's for Dinner</em> web site invite people to share their favorite recipes to cook for dinner.

## Features 

### Existing Features

- Welcome Page

This is the website's landing page. 

For non-logged-in users, it presents an explanation of the site and invites the users to register.

For logged-in users, this page presents directly the recipe list.

- Recipe List

Presents a list of all recipes shared by the website users.

- View Recipe

Allows everyone to view each recipe that is in the website.

- Authentication

Includes registration, login and logout.

- Edit Recipe

Used to update a recipe. A recipe can only be updated by the user who created it.

- Create Recipe

Used to create a recipe. Only authenticated users can create a recipe.

- Delete Recipe

Used to delete a recipe. Only authenticated users can delete a recipe.

### Features Left to Implement

- Contents Review

This feature's objective is to avoid people sharing innapropriate or badly formatted contents in the website. 

A newly created recipe should automatically be included in a list to be reviewed and approved or rejected. 

Only approved recipes will be shared with all the site users.

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

### Data Model

The data model of the <em>What's for Dinner</em> website is composed of the Recipe entity that references the User entity provided by the django framework.

Here are the details of the Recipe entity.

<table style="width:100%">
  <tr>
    <th>Key</th>
    <th>Field Name</th>
    <th>Type</th>
  </tr>
  <tr>
    <td></td>
    <td>slug (unique)</td>
    <td>SlugField</td>
  </tr>
  <tr>
    <td></td>
    <td>title</td>
    <td>CharField</td>
  </tr>
  <tr>
    <td>ForeignKey</td>
    <td>author</td>
    <td>User model</td>
  </tr>
  <tr>
    <td></td>
    <td>short_description</td>
    <td>TextField</td>
  </tr>
  <tr>
    <td></td>
    <td>ingredients</td>
    <td>TextField</td>
  </tr>
  <tr>
    <td></td>
    <td>method</td>
    <td>TextField</td>
  </tr>
</table>

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

New done column was created in the Kanban board so that it is possible to see all the done user stories and tasks in one screenshot.

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

### Final styling and automated tests

Task #15 removed from the project. Task #11 renamed to style the view/edit/delete recipe pages. These pages are similar so they are better styled together.

Wed May 27 12:07:00 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/170820426-33b75915-3228-4f88-8037-e1681e4cf6bd.png)

### Project completed successfully

Automated tests have been revised but there is still work to do in this area. This work has been postponed to the release 2 of the <em>What's for Dinner</em> website.

Wed May 28 11:05:00 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/170820483-78fc785e-955b-4850-b51c-de3fb382a551.png)


## Testing

### Manual tests

The following manual testing scenarios were defined and successfuly carried out along the development.

#### Navigation on the entire site

Navigate to each page, following the available links. Make this navigation works good.

Navigate to not authorized pages, typing directly the url to delete recipe, edit recipe and create recipe. Make sure an appropriate message is displayed. This test must be done:
1. With non-logged-in users trying to create, edit and delete recipe.
2. With logged-in users that are not owner of a recipe, trying to edit and delete that recipe.

#### Broken links

Make sure all the links are good.

#### Ease of Navigation

In different devices, including desktop and mobile devices, navigate for the entire site and make sure your navigation is nice.

### Validator tests

In order to improve the readability and consistency of the Python code, I have used the http://pep8online.com code checker.

Files reviewd:

- tasty_project/settings.py
- tasty_project/urls.py
- whats_for_dinner_app/admin.py
- whats_for_dinner_app/apps.py
- whats_for_dinner_app/forms.py
- whats_for_dinner_app/models.py
- whats_for_dinner_app/test_models.py
- whats_for_dinner_app/test_views.py
- whats_for_dinner_app/urls.py

### Automated tests

The automated tests are currently developed in the test_models.py and test_views.py and the can be kicked off by the following command.

python3 manage.py test --keepdb

A separate testing data base is used so that the data is not mixed up with the production data.

## Deployment

The website is deployed to [heroku](https://heroku.com).

Here is the link for the live site https://whats--for--dinner.herokuapp.com/

### How to deploy the site to heroku

1. Create a GitPod workspace based on the main branch of the [GitHub repository](https://github.com/jmarcosdias/tasty)

2. In the GitPod workspace

   1. Login to Heroku

### How to deploy the site locally

1. Create a GitPod workspace based on the main branch of the [GitHub repository](https://github.com/jmarcosdias/tasty)

2. Install the django framework and the gunicorn http server

   ```
   pip3 install 'django<4' gunicorn
   ```

3. Install the dj_database_url library and the psycopg2 database adapter

   ```
   pip3 install dj_database_url psycopg2
   ```

4. Install libraries to run cloudinary

   ```
   pip3 install dj3-cloudinary-storage
   ```

5. Install the summer note WYSIWYG editor

   ```
   pip3 install django-summernote
   ```

6. Install django-allauth package
   
   ```
   pip3 install django-allauth
   ```

7. Install the witenoise package

   ```
   pip install whitenoise
   ```

8. Create a new file, named env.py, on the top level directory

9. Add the following three lines to the env.py file. 

   ```
   import os
   os.environ["SECRET_KEY"] = "a secret key you define"
   os.environ["CLOUDINARY_URL"] = "cloudinary://658724693665645:m6176WxJpqf2JKhLCRfdoZh1hOk@marcos-dias"
   ```

   You need to update the second line of env.py file with a secret key you define. If you want, you can use a secret key generator, for example https://django-secret-key-generator.netlify.app/, to define the secret key.

10. If you want to use local databases in your local installation, do the following, then ignore the step 11 and go to step 12

    1. In the settings.py file, comment the lines 114 to 126 and then add the following lines

       ```
       DATABASES = {
         'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
           'TEST': {
               'NAME': 'test_database',
           }
         }
       }
       ```  
    
    2. Run the migrations

       ```
       python3 manage.py makemigrations
       python3 manage.py migrate
       ```


11. If you need to use in your local deploy, the heroku databases that are currently used by the live site (https://whats--for--dinner.herokuapp.com/), add the following 2 lines to the env.py file

    ```
    os.environ["DATABASE_URL"] = "postgres://ldykbbxlynpvbu:3c2dc3ad004f84b932b67e75e299a7c618a12607c2400e82a9397ca8d7902549@ec2-54-170-90-26.eu-west-1.compute.amazonaws.com:5432/dd77cfpqto48el"
    os.environ["HEROKU_POSTGRESQL_AMBER_URL"] = "postgres://nbtoigxrzzdxgp:412963f5cb52081534480a65d581c03688f38312187b7428f7f94b4913683c8e@ec2-176-34-211-0.eu-west-1.compute.amazonaws.com:5432/d1q601nu0ev5kr"
    ```

    Notes:
    * Using this DATABASE_URL is dangerous. You may accidentaly delete production data. It would be better to use a local database as described in step 10.
    * This DATABASE_URL is the main database.
    * This HEROKU_POSTGRESQL_AMBER_URL is the database used by the automated tests.
    

12. Congratulations. The website is deployed.
    
    To run the automated tests:
    python3 manage.py test --keepdb

    To run the server:
    python3 manage.py runserver

## Credits

### Background image

- The following picture was taken from [Pixabay](https://pixabay.com). This picture is free for commercial and noncommercial use:
   -  [https://pixabay.com/photos/kagyana-strapatsada-gdarta-2955466/](https://pixabay.com/photos/kagyana-strapatsada-gdarta-2955466/)

 
    
