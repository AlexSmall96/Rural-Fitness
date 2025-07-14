# Rural Fitness
Rural Fitness is a fictional, state-of-the-art gym and spa. Located in the countryside as the name suggests, it aims to provide high-quality facilities to those who live / holiday in more rural areas, while also providing a luxurious spa experience for those looking to relax.

Note: The registration section requires a payment form to fill in, no functionality is set up to handle card details and no payments will be taken. This form is purely for visual effects. 
## Live Site 
[https://rural-fitness.onrender.com/](https://rural-fitness.onrender.com/)

The deployed project is currently on Render's free tier. Projects on this tier spin down during periods of inactivity, therefore, there may be a delay when loading the above URL.

![](documentation/amiresp.png)

## Repository 
[https://github.com/AlexSmall96/Rural-Fitness](https://github.com/AlexSmall96/Rural-Fitness)

## Author 
Alex Small
## Table of Contents
- [Rural Fitness](#rural-fitness)
  * [Live Site](#live-site)
  * [Repository](#repository)
  * [Author](#author)
  * [Table of Contents](#table-of-contents)
- [UX](#ux)
  * [Target Audience](#target-audience)
  * [Project Goals and Planning](#project-goals-and-planning)
    + [Database Schema](#database-schema)
  * [Wireframes](#wireframes)
  * [Colours](#colours)
  * [Typography](#typography)
  * [Images](#images)
  * [User Stories](#user-stories)
    + [Gym / Club Member](#gym---club-member)
    + [Gym / Club Admin](#gym---club-admin)
  * [Features](#features)
  * [Future Features](#future-features)
  * [Testing](#testing)
  * [Programming Languages, Frameworks, and Libraries used](#programming-languages--frameworks--and-libraries-used)
  * [Other programs used](#other-programs-used)
- [Deployment](#deployment)
    + [Deploying the Site to Heroku](#deploying-the-site-to-heroku)
    + [Forking the Repository on GitHub](#forking-the-repository-on-github)
    + [Cloning the Repository on GitHub](#cloning-the-repository-on-github)
- [Credits](#credits)
  * [Content](#content)
  * [Media](#media)
  * [Code](#code)
  * [Acknowledgements](#acknowledgements)
# UX
## Target Audience
The site is mainly targeted toward fitness enthusiasts living in rural areas, but the broader target audience is all adults.  The site aims to be welcoming and informal yet professional, with class descriptions being fun and engaging to draw in new members.
 
## Project Goals and Planning
The goal of the project was a website for a fictional state-of-the-art gym, complete with a user-friendly exercise class booking system. This aimed to display database management skills and proficiency in the Django framework, along with CSS and JS competency. The site aims to make the booking process as intuitive and smooth as possible, with clear feedback given to the user at each stage.
### Database Schema
To plan the structure of the database, the below schema was created. The Activity model is the base model, with the Session model inheriting values from it via a foreign key. The Booking model uses the Session model as a foreign key.

![Database Schema](documentation/planning/db_schema.png)

## Wireframes
To plan the site layout, the below wireframes were created for the Home, Timetable, Members Area, and Admin pages. For each page, the desktop view was sketched out in a wireframe, for pages where the mobile view differed significantly in layout, a mobile wireframe was also created. 

- Home

![Home](documentation/planning/Home.jpg)

- Timetable

![Timetable](documentation/planning/Timetable.jpg)

- Members Area

![Members Area](documentation/planning/MembersArea.jpg)

- Admin Page

![Members Area](documentation/planning/Admin.jpg)

- Membership Options / Registration Page

![Registration](documentation/planning/Registration.jpg)

- Login

![Registration](documentation/planning/Login.jpg)

## Colours
The main colors used throughout the site are given below. These colors were chosen to create a subtle, clean, professional look, which reflects the gym's ethos.
![Colours](documentation/planning/RFColours.png)

## Typography 
The font used throughout the site was [Mallana](https://fonts.google.com/specimen/Mallanna) from google fonts.  This was chosen due to its professional feel to again reflect the gym's style.
 
![Font](documentation/planning/font.jpg)

## Images
The site images were taken from [Pexels](https://www.pexels.com/). These were chosen as they were appropriate to the activities the gym hosts. There is also a wide demographic range in the selected images, making the gym appeal to a wide audience.

![Images](documentation/planning/images.jpg)

## User Stories
The project followed an agile methodology and implemented Issues on GitHub, which were aligned with the project's User stories. Details of the acceptance criteria of each user story can be found in [TESTING.MD](https://github.com/AlexSmall96/Rural-Fitness/blob/main/TESTING.MD).
### Gym / Club Member
- As a potential member, I can create an account so I can log in and view members-only pages.

- As a member, I can log in with my username and password after I have registered, and access members-only pages.

- As a member, I can book any available class from the timetable.

- As a member, I can view which classes I am booked into.

- As a member, I can cancel a booking If I can't/no longer wish to attend the class.

- As a member, I can view which classes I am booked into.

### Gym / Club Admin
- As an Admin, I can create a new class and save it to the timetable.

- As an admin, I can edit any field in any class in the timetable.

- As an admin, I can select any class from the timetable and delete it.

## Features
Below is a summary of all the features of the project, and the value they bring to the user. Features are recorded in [documentation](https://github.com/AlexSmall96/Rural-Fitness/blob/main/documentation/testing).

| Feature | Value to User|
|------|------------------|
|Logo| Visually pleasing first impression of the site|
|Navigation Bar| Allows the user to easily navigate all pages on the site|
|Hero Image| Clean professional looking image which gives the user an immediate impression of the standard of the facilities|
|About Section| Concise and engaging description of everything the gym and site have to offer|
|Footer| Provides further ease of navigation throughout the site as well as contact links to allow the user to find out more information or get in touch|
|Register Page| An intuitive, smooth process of signing up, allowing the user to browse different membership options and create an account|
|Login Page| Allows the user to easily log in and access members-only content|
|Timetable Date Tabs| Allows the user to easily navigate through the timetable, and helps them to plan their activities out in advance, without being overwhelmed with information|
|Timetable Help Button| Provides clear concise instructions on how to use the timetable page, which can be hidden if the user wishes to make the page cleaner|
|Booking Buttons| Allows the user to provisionally select a range of classes they wish to book|
|Timetable Confirmation Button| Allows the user to review and confirm their bookings|
|Timetable Cancellation Button| Allows the user to smoothly navigate from booking a class to canceling it on the same page if they wish|
|Timetable Feedback| Confirms to the user that their classes have been booked or canceled |
|Members Area Bookings List| Allows the user to review all upcoming bookings and easily cancel any|
|Members Area Feedback| Confirms to the user that their classes have been canceled |
|Members Area Ads| Provides engaging ways of informing the user of the site's Facebook community, as well as how to book a spa service|
|Admin Page| Allows the admin of the site to view any session they wish, and create, update, or delete sessions|
|Admin Feedback| Informs the admin of any incorrect inputs, such as session times not on the hour, or clashes in the timetable|
## Future Features
Future developments of this project may include implementing the following features:
- Email registration so members can be notified of changes or cancellations to sessions they are booked in for.
- Not allowing users to cancel bookings if it is within a certain period of the session starting.
- Developing the admin page to allow the Activity and Session models to be edited.
## Testing
Testing is detailed fully in [TESTING.MD](https://github.com/AlexSmall96/Rural-Fitness/blob/main/TESTING.MD).

## Programming Languages, Frameworks, and Libraries used
- HTML
- CSS, Javascript
    - The Bootstrap framework was used, mainly for its grid system. Several pages use buttons, modals, and tabs via Bootstrap.
- Python
    - The Django framework formed the basis of this project. It was used to create data models and to pass information back between the browser and the database. 
    - The DateTime Python library was used to record the current date to load the correct data into the timetable, members area, and admin pages.
## Other programs used 
- [CSV to JSON](https://www.convertcsv.com/csv-to-json.htm) was used to convert the timetable data from Excel into JSON format for loading into the database.
- [coolors. co](https://coolors.co/) was used to create the color palette image.
- [balsamiq](https://balsamiq.com/wireframes) was used to create the wireframe images.
# Deployment
### Deploying the Site to Heroku
1. Create an account on [Elephant SQL](https://www.elephantsql.com/) and log in.
2. Create a new database instance on Elephant SQL and copy the database URL
3. Create an account on [Heroku](https://id.heroku.com/login) and log in.
4. Create a new app on Heroku
5. Navigate to the 'Settings' tab, and click "Reveal Config Vars".
6. Add a config var with key DATABASE_URL and value equal to the database URL you copied from elephantSQL
7. Create an account on [Cloudinary](https://cloudinary.com/users/login) and upload all files in the static folder of this repository
8. Copy the Cloudinary URL.
9. Add another config var with the key CLOUDINARY_URL and the value of the Cloudinary URL you copied.
10. Add a final config var with key SECRET_KEY and set it to a chosen value.
11. Navigate to the 'Deployment' tab. For 'Deployment method', select Github.
12. Under 'Search for a repository to connect to, enter the appropriate GitHub username and repository name
13. To deploy the repository, either select 'Enable Automatic Deploys', which deploys the site after each push to GitHub, or Manually click 'Deploy Branch'
14. In both deployment methods, the main branch or any forked branches may be chosen, see [Forking the Repository on Github](#Forking-the-Repository-on-GitHub)

### Forking the Repository on GitHub
1. On GitHub.com, navigate to the main page of the [Rural Fitness](https://github.com/AlexSmall96/Rural-Fitness) repository.
2. In the top-right corner of the page, click Fork.
3. Select an owner for the forked repository.
4. By default, forks are named the same as their upstream repositories. You can change the name of the fork to distinguish it further.
5. Optionally, add a description of your fork.
6. Choose whether to copy only the default branch or all branches to the new fork. For many forking scenarios, such as contributing to open-source projects, you only need to copy the default branch. By default, only the default branch is copied.
7. Click Create Fork.
### Cloning the Repository on GitHub
1. On GitHub.com, navigate to the main page of the [Rural Fitness](https://github.com/AlexSmall96/Rural-Fitness) repository.
2. Above the list of files, click Code.
3. Copy the URL for the repository.
4. Open Terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier.
7. Press Enter to create your local clone.

# Credits
## Content
The content of this site is all original thought, with inspiration taken from popular gym sites and club booking systems. 
## Media
The images were taken from the stock image site, [Pexels](https://www.pexels.com/).
The icons were taken from [Font Awesome](https://fontawesome.com/).
## Code
- The code used to register a user was taken from the following tutorial:
https://overiq.com/django-1-10/django-creating-users-using-usercreationform/
- The code for the login process was taken from the below tutorial
https://learndjango.com/tutorials/django-login-and-logout-tutorial
- The styling for the ads on the admin image was taken from the below tutorial:
https://www.w3schools.com/howto/howto_css_image_text_blocks.asp
## Acknowledgements 
This application was created as a portfolio 4 project for the Diploma in Full Stack Software Development from [Code Institute](https://codeinstitute.net/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI+-+UK+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=1578649861&hsa_grp=62188641240&hsa_ad=635720257674&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAiA5Y6eBhAbEiwA_2ZWIUE0LRewvfAYnQS69Lujb5s2FrQjmX0Idzqj-Olbamn1DbS2D-R7gBoC-1AQAvD_BwE
)
I would like to thank my mentor Harry Dhillon for his encouraging support and detailed feedback throughout this pro
