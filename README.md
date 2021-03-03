# T4A2-A: Island Bike Rentals
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#overview">Overview</a>
      <!-- <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul> -->
    </li>
    <!-- <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li> -->
    <li><a href="#user-stories">User Stories</a></li>
    <li><a href="#wireframes">Wireframes</a></li>
    <li><a href="#dataflow-diagram">Database Diagram</a></li>
    <li><a href="#dataflow-diagram">Dataflow Diagram</a></li>
    <li><a href="#application-architecture-diagram">Application Architecture Diagram</a></li>
    <li><a href="#project-management">Project Management</a></li>
  </ol>
</details>

## Overview

Island Bike Rentals is a holiday goers dream come true. The Super73 Electric Bikes are a fun and exciting way to get around the island. They are great to ride through the town and on the lucious island roads and sandy beaches. This booking system is a stress free way to book your holiday fun and the bikes are a great way to tour the island!

![](docs/images/super73.png)

<!-- about the project -->
<!-- ### Built With -->
<!-- list any major frameworks that you built your project using (bootstrap...) -->

<!-- ## Getting Started -->
<!-- instructions on setting up your project locally -->
<!-- ### Prerequisites -->
<!-- list things you need to use the software and how to install them -->
<!-- ### Installation -->
<!-- clone repo... -->

<!-- ## Usage -->
<!-- useful examples of how a project can be used. Additional screenshots, code examples and demos -->

## User Stories
<!-- organize by feature -->
**rental form**
- As a _holiday goer_ I want a simple rental form so I can have a stress free way to rent a bicycle.
- As a _holiday goer_ I want a simple stress free way to rent a bicycle so I can easily get around and explore the island.
- As a _holiday goer_ I want a straightforward rental system so I can focus on relaxing and having fun.
- As a _holiday goer_ I want a quick and easy rental because I'm already overwhelmed by my holiday planning.

**payment**
- As a _holiday goer_ I want to be able to pay beforehand so I can grab and go my bike without any hassle.

**validation**
- As a _holiday goer_ I want to be able to keep track of my rentals.
- As a _holiday goer_ I want to receive an email from my booking with a reference number & the details of my booking so I can keep track of my rentals.

**login**
- As _admin_ I want to be able to login so I can securely look at bookings.

**bookings**
- As _admin_ I want to be able to view all bookings so I can get people their bikes.
- As _admin_ I want to be able to modify bookings because life happens and people change their minds.
- As _admin_ I want to be able to check off bookings once they are complete so they don't pile up in the bookings list.

**for a later time**
- As a _holiday goer_ who travels to the island often I want to be able to login so that I can have my details saved for an easier booking experience.
- As _someone who visits the island often_ I want my details to be stored so I don't have to fill out a form each time.

## Wireframes
### Customer 
**Home Page**
![](./docs/wireframes/home.png)

**Bike Rental Form**
- "Continue to Payment" sends user to the bike payment form page.
![](./docs/wireframes/rent.png)

**Bike Payment Form**
- After clicking the "Pay $##" button the user is redirected to the successful rental page where they will be given a reference number.
![](./docs/wireframes/payment.png)

**Successful Rental Page**
![](./docs/wireframes/rent_success.png)

### Admin
**Login**
- Accessed from the top right hand corner of any page. 
- The login screen shows above the current screen that the user is on.
![](./docs/wireframes/login.png)

**Bookings**
![](./docs/wireframes/bookings.png)

**Single Booking**
![](./docs/wireframes/single_booking.png)

## Database Diagram
![](./docs/diagrams/database.png)

## Dataflow Diagram
![](./docs/diagrams/dataflow.png)

1. Customer enters personal details into rental form. 
2. Customer enters payment details into payment form.
3. If payment form is accepted, booking is validated. Customer is sent a booking result receipt in the form of an email. Booking details are stored in database.
4. Admin enters login details, login details are verified in database, if the account is confirmed authentication is returned and the admin is logged in.
5. Admin accesses bookings index, authentication details are sent with request. Database is queried and all booking data is returned.
6. Admin accesses single booking through booking index. Database is queried and booking data for booking is returned.


## Application Architecture Diagram
![](./docs/diagrams/aad.png)

User accesses front end which then connects to backend Flask Server ec2 instance and queries PostgreSQL database in seperate ec2 instance within a private subnet.
<!-- ???docker??? -->

## Project Management

This project was managed through Notion.
- [T4A2-A](https://www.notion.so/3872ca07418b41469210b23a26106869?v=6bbc9fcef49a419c8dc72182744d628b)
- [T4A2-B](https://www.notion.so/2e265d85058c4f4294840492f8e12cd4?v=8a146125c84a4eadbd150c974caad7af)

Note: All tasks were assigned to myself as I was the only person working on this project. :)
### T4A2 Part A
**11 February 2021**
![](./docs/notion/2021-02-11.png)
**12 February 2021**
![](./docs/notion/2021-02-12.png)
**13 February 2021**
![](./docs/notion/2021-02-13.png)
**15 February 2021**
![](./docs/notion/2021-02-15.png)
**16 February 2021**
![](./docs/notion/2021-02-16.png)
**17 February 2021**
![](./docs/notion/2021-02-17.png)
**18 February 2021**
![](./docs/notion/2021-02-18.png)
**19 February 2021**
![](./docs/notion/2021-02-19.png)

### T4A2 Part B
**25-27 February 2021**  
Due to illness I did not get much done, though I was able to deploy my app using Heroku!  

**01 March 2021**
![](./docs/notion/2021-03-01.png)
**02 March 2021**
![](./docs/notion/2021-03-02.png)
**03 March 2021**
![](./docs/notion/2021-03-03.png)
![](./docs/notion/2021-03-03_status-start.png)
![](./docs/notion/2021-03-03_status-end.png)
