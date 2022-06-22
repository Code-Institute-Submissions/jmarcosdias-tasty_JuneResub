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
* Install psycopg2 postgresql database adapter
* Install dj3-cloudinary-storage django package for integration with cloudinary
* Create a new django project, named tasty_project
* Create a new app, named whats_for_dinner_app
* Update settings.py file inside tasty_project, adding the new app, allowed hosts, cloudinary settings, getting of secret key and database url, templates dir, root url configuration, wsgi application, static url and media url configuration
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

There is some time before the delivery day. This way the following new tasks were identified and placed into the Kanban board.

**TASK: Improve appearance of the landing page**

Landing page is working but not yet looking good. Some elements are very close together and this makes the website look unfinished. Some design work is needed in the landing page and then new similar tasks will be created for the remaining pages.

**TASK: Improve automated tests**

Automated tests were developed for view recipe list and view recipe but there are no automated tests for create, edit and delete recipe. The automated tests must be reviewed in order to cover at least the CRUD functionalities.

Mon May 23 21:32:50 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/169899937-1304d0f8-3994-48e8-aa0b-d73944d69fe4.png)

### Changes to the landing page contents and appearance done

The landing page is now with the intended design and content for this version of the project, to be delivered on 28th of May.

New tasks were created to style each of the remaining pages.

The automated tests task was moved back to the to do column. The tasks in the to do column are now being prioritized.

Wed May 25 02:35:00 2022 +0100
![image](https://user-images.githubusercontent.com/87392921/170159595-2bb948af-df14-485a-b00c-b4e073f851af.png)

### Styling the main pages

Tasks were updated and repositioned accordingly to the current need. One task was renamed to follow the naming convention of others (task #10). One task was created (task #16).

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

Tasks were updated and repositioned accordingly to the current need. One task was created (task #17).
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

The following manual testing scenarios were defined and successfully carried out along the development.

#### Navigation on the entire site

Navigate to each page, following the available links. Make sure the navigation works well.

Navigate to not authorized pages, typing directly the url to delete recipe, edit recipe and create recipe. Make sure an appropriate message is displayed. This test must be done:
1. With non-logged-in users trying to create, edit and delete recipes.
2. With logged-in users that are not owners of a recipe, trying to edit and delete that recipe.

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

The automated tests are currently developed in the test_models.py and test_views.py and they can be kicked off by the following command.

python3 manage.py test --keepdb

A separate testing database is used so that the data is not mixed up with the production data.

## Deployment

The website is deployed to [heroku](https://heroku.com).

Here is the link for the live site https://whats--for--dinner.herokuapp.com/

### How to deploy the site to heroku

The below instructions detail how to deploy the site to https://whats-for-dinner-new.herokuapp.com/. In other words, these instructions describe how to deploy this application to heroku, using the whats-for-dinner-new name for the heroku app.

When deploying, you can use any other available name for the heroku app. For example, this site is currently deployed to heroku, using the whats--for--dinner name for the heroku app (https://whats--for--dinner.herokuapp.com/).

1. Create a GitPod workspace based on the main branch of the [GitHub repository](https://github.com/jmarcosdias/tasty)

2. In the GitPod workspace

   1. Login to heroku
      ```
      heroku login -i
      ```
      ![image](https://user-images.githubusercontent.com/87392921/174455490-581e5017-b084-4f99-bd9c-3b942ca94b70.png)

   2. Create heroku remote for a new app choosing Europe region
      ```
      heroku create -a whats-for-dinner-new --region eu
      ```
      ![image](https://user-images.githubusercontent.com/87392921/174455668-ddde103b-07f4-4a7f-81a6-0c99063ec07f.png)

      You can then confirm that the heroku remote has been created, by using the following command and making sure you see those two heroku lines.
      ```
      git remote -v
      ```
      ![image](https://user-images.githubusercontent.com/87392921/174455691-22f1b20e-5406-4cb5-8d98-52a9a39c0731.png)
      
   3. Use heroku config to set the CLOUDINARY_URL variable
      ```
      heroku config:set CLOUDINARY_URL='<cloudinary details>'
      ```
      
      Use the value that is inside the "API Environment variable" section, available in the cloudinary account for cloudinary details. This starts with "cloudinary://".
      
   4. Use heroku config to set the SECRET_KEY variable
      ```
      heroku config:set SECRET_KEY='<a secret key you define>'
      ```
      
      You can use an online secret key generator to generate your secret key, for example https://django-secret-key-generator.netlify.app.
      
   5. Use heroku config to set disable collect static   
      ```
      heroku config:set DISABLE_COLLECTSTATIC=1
      ```
   
   6. Use heroku ```addons:create``` to create the main database
      ```
      heroku addons:create heroku-postgresql --as=DATABASE
      ```
      
   7. Use heroku ```addons:create``` to create the database for automated tests
       
       ```
       heroku addons:create heroku-postgresql --as=HEROKU_POSTGRESQL_AMBER
       ```
       ![image](https://user-images.githubusercontent.com/87392921/174456231-0754f991-d7c8-4b33-9531-2a629e77a93a.png)
       
      
   8. Update the settings.py file inside tasty_project, adding the URL of the application you are deploying
   
      1. Add 'whats-for-dinner-new.herokuapp.com' to the allowed hosts
         ![image](https://user-images.githubusercontent.com/87392921/174455886-0a5a5c8e-ef8c-4701-b645-9f791a978b81.png)
      
      2. Commit your changes
         ```
         git add .
         git commit -m "Update allowed hosts in settings.py file"
         ```
      
   9. Push to heroku git repository
      ```
      git push heroku main
      ```
      
   10. Use heroku config to unset disable collect static
      ```
      heroku config:unset DISABLE_COLLECTSTATIC
      ```
      
   9. Use heroku run to make migrations
      ```
      heroku run python3 manage.py makemigrations
      ```
      ![image](https://user-images.githubusercontent.com/87392921/174456190-2f3fe4a6-fb81-48be-8a7c-b003fc83a78b.png)
      
   10. Use heroku run to migrate
       ```
       heroku run python3 manage.py migrate
       ```
       ![image](https://user-images.githubusercontent.com/87392921/174456204-534ca8f2-8a91-4b73-bf64-3c817ee10db3.png)
       
   12. Use heroku run to run automated tests
       ```
       heroku run python3 manage.py test --keepdb
       ```
       ![image](https://user-images.githubusercontent.com/87392921/174456257-db071f6f-e726-4773-99e3-584165a70bb5.png)

   13. Congratulations! Your application is deployed to https://whats-for-dinner-new.herokuapp.com/ 

### How to deploy the site locally

1. Create a GitPod workspace based on the main branch of the [GitHub repository](https://github.com/jmarcosdias/tasty)

2. Install the required packages based on the requirements.txt file

   ```
   pip3 install -r requirements.txt
   ```
   
   Another option would be to install the following:
   
   1. Install the django framework and the gunicorn http server
   ```
   pip3 install 'django<4' gunicorn
   ```

   2. Install the dj_database_url library and the psycopg2 database adapter
   ```
   pip3 install dj_database_url psycopg2
   ```

   3. Install libraries to run cloudinary

   ```
   pip3 install dj3-cloudinary-storage
   ```

   4. Install the summer note WYSIWYG editor
   
   ```
   pip3 install django-summernote
   ```

   5. Install django-allauth package
   
   ```
   pip3 install django-allauth
   ```

   6. Install the witenoise package

   ```
   pip install whitenoise
   ```

3. Create a new file, named env.py, on the top level directory

4. Add the following three lines to the env.py file. 

   ```
   import os
   os.environ["SECRET_KEY"] = "<a secret key you define>"
   os.environ["CLOUDINARY_URL"] = "<cloudinary details>"
   ```
   
   Update the second line of the env.py file with a secret key you define. If you want, you can use a secret key generator, for example https://django-secret-key-generator.netlify.app/, to define the secret key.
   
   In the third line of the env.py file, include the cloudinary details. Use the value that is inside the "API Environment variable" section, available in the cloudinary account for cloudinary details. This starts with "cloudinary://".   

5. If you want to use local databases in your local installation, do the following, then ignore the step 6 and go to step 7

   1. In the tasty_project/settings.py file, comment the lines 114 to 126 and then add the following lines

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
    
    2. Make migrations and migrate

       ```
       python3 manage.py makemigrations
       ```
       
       ```
       python3 manage.py migrate
       ```


6. If you need to use in your local deploy the heroku databases that are currently used by the live site (https://whats--for--dinner.herokuapp.com/), add the following 2 lines to the env.py file

    ```
    os.environ["DATABASE_URL"] = "URL of the main postgres database."
    os.environ["HEROKU_POSTGRESQL_AMBER_URL"] = "URL of the postgres database used for automated tests"
    ```

    Notes:
    * Using the production DATABASE_URL is dangerous. You may accidentally delete or update production data. It would be better to use a local database as described in step 5.
    * This DATABASE_URL is the main database.
    * This HEROKU_POSTGRESQL_AMBER_URL is the database used for the automated tests.
    * You should not need to make migrations and migrate, but if you want you can do it
       ```
       python3 manage.py makemigrations
       ```   
       ```
       python3 manage.py migrate
       ```
    
7. Run the automated tests
   ```
   python3 manage.py test --keepdb
   ```
    
8. Congratulations. The website is deployed locally
    
    To run the server locally:
    ```
    python3 manage.py runserver
    ```

## Credits

### Background image

- The following picture was taken from [Pixabay](https://pixabay.com). This picture is free for commercial and noncommercial use:
   -  [https://pixabay.com/photos/kagyana-strapatsada-gdarta-2955466/](https://pixabay.com/photos/kagyana-strapatsada-gdarta-2955466/)

 
    
