# MS3-Tiny_Schedule
 A scheduling site for small teams to colaborate and manage

<img src="" alt="Image of screen-mockup on desktop, tablet and mobile screen sizes" />

## An Overview
For my third milestone project I have chosen to build a small teams messaging platform for small teams and businesses to stay in touch with eachother. This project is built using HTML, CSS, Javascript, python, mongoDB and accompanying frameworks. Show casing mobile first design, usage of API's and also a backend framwork for users to interact with the site.
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
   * [Features](#features)
   * [Technologies Used](#technologies-used)
   * [Feature and Technology Testing](#feature-and-technology-testing)
   * [Further Testing](#further-testing)
   * [Deployment](#deployment)
   * [Credits](#credits)

## UX
### The Experience:


### Journey of the Site:



### Colours:


## UI 
### The Interface:



## Objectives
### For the Site Owner:


### For the User:


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
   

### Middle
   

### Ongoing
   

## User Stories


## Features
### Current:



### Future:

## Technologies used:
* HTML5
* CSS
* Javascript
   * [Jquery](https://jquery.com)
* [Bootstrap](https://getbootstrap.com/) - for structure and extra features of the site
* [Fontawesome](https://fontawesome.com/)
* [MongoDB](https://www.mongodb.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [EmailJS](https://www.emailjs.com/)

## Feature and Technology Testing
### Manual testing:


## Further Testing:
### HTML
All HTML code has gone through https://validator.w3.org/ and no errors occur

### CSS
All CSS was tested using direct input with https://jigsaw.w3.org and no errors were returned
<img src="" alt="screenshot of CSS w3 Validation completion checks, passed" width="576" height="360" />

### JS
All Javascript has been passed through https://jshint.com and no errors occured

### Known issues


### Chrome developer tools
When building the site, during each section I used Chrome's inspect and developer tools (such as lighthouse) to validate my work and to ensure the site worked across multiple screen sizes.
This was also used to debug any structural and styling issues on the fly

### Buttons and Links
All buttons and links have been accounted for and directs to the right source

## Deployment:



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