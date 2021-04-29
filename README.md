# MS3-Tiny_Schedule
 A scheduling site for small teams to colaborate and manage

<img src="" alt="Image of screen-mockup on desktop, tablet and mobile screen sizes" />

## An Overview
For my third milestone project I have chosen to build a small teams messaging platform for small teams and businesses to stay in touch with each other. This project is built using HTML, CSS, Javascript, python, mongoDB and accompanying frameworks. Show casing mobile first design, usage of API's and also a backend framework for users to interact with the site.
I decided on building a site for small businesses or teams to be able to easily message each other because of how much time we have spent at home over the past year. This site gives a basic and easy way for people to keep in touch and utilise it like a digital white board.

In this document I will go through what I've built and why, as well as future goals and testing that's been done to make sure this site is functional in what it offers as well as across multiple device types, from mobile to desktop.

View a live version of my site [here](https://tinyschedule.herokuapp.com/)

## Table of content
   * [UX](#ux) 
   * [UI](#ui)
   * [Objectives](#objectives)
      * [For The Site Owner](#for-the-site-owner)
      * [For The User](#for-the-user)
   * [Wireframe](#wireframe)
   * [Scope](#scope)
      * [Start](#start)
      * [Middle](#middle)
      * [Ongoing](#ongoing)
   * [User Stories](#user-stories)
   * [Technologies Used](#technologies-used)
   * [Feature and Technology Testing](#feature-and-technology-testing)
   * [Further Testing](#further-testing)
   * [Deployment](#deployment)
   * [Credits](#credits)

## UX
### The Experience:
I wanted to create a site which has animalistic and clean look. It has a modern colour tone which is calming and the removal of a standard white background, it creates a unique look.
Corners are rounded on most UI elements and even the Navigation Bar at the top is separated from the top to create a different look.

### Journey of the Site:
As a new user with no account, you are greeted with a run down on what the site is and what you can expect from using this website.
From there you can see the different tiers that are offered and what features a user can expect from different tiers.

The login page is present for users that have already been signed up and there is a contact page tab for users to reach out for more information.

Once reached out to the developer, users will be have an admin account created for them. As an admin you can create and delete users, see what users are in your team as well as all the functions of a standard user, such as creating messages, seeing your basic profile page and any future options.

Messaging section:
* Nice and simple feature where users can utilise the site as a digital white board. In times where we're spending more time at home, this is a great options for users to collaborate ideas like they might do on a meeting room whiteboard.

User sections (admin access)
* This is a place where the admin can view everyone's name and user name. Quick and easy place for admins to check in on their team's details

Management section
* this is treated like a homepage once someone has logged in. 
    
    * For admins, it is a place to view their users, create new users and to check their own profile. 
        * Within the User section (explained above) managers can also remove users from the space if someone changes or is no longer with the team
        * The new user section is a sign-up page for admins to create new users by entering their name, username and password
        * The profile page is similar to the one for basic users where it's a quick stop to check if you're signed into the right account.
    
    * For standard users, this is treated as a basic home screen to easily access their own profile as a welcome screen.

### Colours:

#EDF6F9 - This is used as the base background colour of the site to stand out from other white background based sites.

#006D77 - This is a darker variant of the background colour to create a familiar tone but offers contrast not only for an accessibility point of view but also for general viewing.

#BADEDA - This is an in between colour between the top two colours. This is used for hover style colours to again be different to being just white. 

#FFDDD2 - This colour offers a change in the colour pallet so is mainly used for text colouring to offer the text a bit of a "pop" out moment.

#E29578 - Offering the starkest difference in colour, this orangy colour is used for hover states on assets that use #FFDDD2 as a font colour

## UI 
### The Interface:

The site is built to be modern and mobile first. Its features are also supported across multiple browsers. This is shown in different parts of the site:

* The nav bar features a disjointed design where it's not connected to the top of the site like normal nav bars typically do. It is scalable and changes accordingly to device and screen size to what it shows.

* The messaging section is treated like sticky notes on a white board. On a large screen device it holds two notes side by side. 
    * On mobile / small screen devices, it shows the messages in a list view that is available to scroll, this is done with `col-12` on small devices.

* The management page differs between different users but the UI is similar across the board. Different sections withing the management page are separated by individual cells that span across the container with `col-12`. 

* The profile page features a nice and basic `jumbotron` that floats in the middle of the page. This is designed to quickly let users see if they're logged into the right account.


## Objectives
### For the Site Owner:
For the site owner, the main objective is to get more people signing up to accounts and for people on the base tier to sign up for the higher tiers. With extra features that can be built on top of the higher tiers, this will drive users who start off with the base tier to upgrade. 
The other objective for the site owner is to ensure users get a smooth experience whilst collaborating with their team.
Ensuring accounts admin creates are functional and there are little to no down time for seamless collaboration.

### For the User:
For the user the main goal is to have an easy to use interface to talk and share ideas with their team members, no matter the size.
Another objective would be to have the ability for admins / managers to easily talk to their team members without the need for video calls.

## Wireframe:
For my wireframes, I used Balsamiq Wireframes to mockup and create the site in different device sizes. Shown below are the different wireframes for Mobile, Tablet and Desktop. I started with the mobile site and worked from there to scale up the design. You can click on the image for a larger size.

<img src="" alt="Wireframes of small, medium and large screen sizes" width="576" height="360" />

## Accessibility
The site was built with accessibility needs in mind. 
   * All images have the correct alt tags
   * Colours throughout the site offer contrast from on another to ensure easier readability
   * Tested with Lighthouse to improve and fix accessibility concerns

## Scope
### Start
At the planning stage of this project, I planned out the features that I wanted to implement and chose the colour scheme of the site. This was then plotted down on my wireframe to give a skeleton look of where everything would go.
Planning:
* Message board feature
* The ability to create users
* The ability for admins to delete users
UI/UX.
* With the basic HTML skeleton I layed out
    * The admin section
    * Messaging section
    * Connected to MongoDB and imported the relevant frameworks (flask)

### Middle
* Content and connection
    * After connecting MongoDB, I started testing the implementation of the mongoDB data with manual entry directly within MongoDB's site and then moved onto building a user input option on my project to inject and remove data at will
        * I created the messaging section where users can post notes to a digital messaging board
        * I created the admin functionality where admins can create new users to join their team
        * Deletion functionality was added as well for admins to remove team members from their team
        * A profile page was added for users to check if they're logged into the right account.
* Styling
    * Colour style for the site is mentioned above, I have chosen these colours to create a calm and relaxing tone for users to work with whilst they're collaborating with each other.
    * The style of the page like mentioned above is suppose to feel like it's modern and different. Which is why the nav bar is not connected to the top of the page and all elements are rounded off to fit the device types we use these days

### Ongoing
* For future ideas to add on for the different tier plans, I want to build:
    * Direct to person messaging
    * Further addition to profile page
    * File upload for message board

## User Stories
* As an Admin I expect to be able to:
    * Create new users
    * Send messages to the team
    * Remove users 
    * Have a space where it's easy to use and understand

## Technologies used:
* HTML5
* CSS
* [Bootstrap](https://getbootstrap.com/) - for structure and extra features of the site
* [Fontawesome](https://fontawesome.com/)
* Javascript
   * [Jquery](https://jquery.com)
* [EmailJS](https://www.emailjs.com/)
* Python
* [MongoDB](https://www.mongodb.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

## Feature and Technology Testing
### Manual testing:
Each feature set was tested on mobile, medium and large screen, natively and also via developer inspection on Chrome and Safari.
- Log in functionality
- Create user functionality
- Contact form
- User interface and scalability of elements on site
- Messaging functionality
- Delete message functionality
- Delete user functionality
- Individual log in functionality for users that are not admins

## Further Testing:
### HTML
All HTML code has gone through https://validator.w3.org/ and no errors occur

### CSS
All CSS was tested using direct input with https://jigsaw.w3.org and no errors were returned
<img src="static/assets/Screenshot2021-04-29at19.01.10.png" alt="screenshot of CSS w3 Validation completion checks, passed" width="576" height="360" />

### JS
All Javascript has been passed through https://jshint.com and no errors occurred

### Known issues
Currently the contact us section is functional, but does not notify the user that their request has been sent - working on a fix.

### Chrome developer tools
When building the site, during each section I used Chrome's inspect and developer tools (such as lighthouse) to validate my work and to ensure the site worked across multiple screen sizes.
This was also used to debug any structural and styling issues on the fly

### Buttons and Links
All buttons and links have been accounted for and directs to the right source

## Deployment:
During this project, I made sure that I spent some of my time focusing on how to properly manage and deploy my project. I used my own IDE (VSCode), Github's desktop app and the IDE's (VS Code) terminal to create branches, test and deploy my code. I primarily did my work in my testing branch as I knew that I would commit to my main branch closer to the time I made my site public. Within the IDE:

I used the built in terminal to get git status, git add, git commits and git push
Within Github's desktop app:

I used to push to github and change/create branches when I wanted to test out new features / layouts. An example of this was when I was creating the hero carousel and wanted to test how different screen sizes would affect the provided images

- Code has been published to github using git and terminal.
- Code history is managed via github as well.
- Site is deployed to heroku - http://tinyschedule.herokuapp.com


## Credits:
   * [Bootstrap](https://getbootstrap.com/)
   * [ColorTools](https://www.colortools.net/color_complementary.html) for picking complementary and contrasting colours
   * My mentor Spencer for helping me along the way on my first project.
   * [W3School](https://www.w3schools.com/howto/howto_css_smooth_scroll.asp) for safari smooth scrolling: 
      ``` 
      $(document).ready(function(){
      // Add smooth scrolling to all links
      $("a").on('click', function(event) {

         // Make sure this.hash has a value before overriding default behaviour
         if (this.hash !== "") {
            // Prevent default anchor click behaviour
            event.preventDefault();

            // Store hash
            var hash = this.hash;

            // Using jQuery's animate() method to add smooth page scroll
            // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
            $('html, body').animate({
            scrollTop: $(hash).offset().top
            }, 800, function(){

            // Add hash (#) to URL when done scrolling (default click behaviour)
            window.location.hash = hash;
            });
         } // End if
      });
      });
      ```
   * [Favicon](https://favicon.io/emoji-favicons/flag-wales/) for favicon generator
   * [W3School](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp) for back to top button
   * Dev Ed on youtube for tutorial on Javascript
   * [Markdown Tables](https://www.tablesgenerator.com/markdown_tables) for generating markdown table template

### [Back to Top](#an-overview)