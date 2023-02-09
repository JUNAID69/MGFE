
# Restaurant/Cafe/Bar Order Management App

![WhatsApp Image 2022-09-22 at 3 41 41 PM (2)](https://user-images.githubusercontent.com/124381004/217826137-253bf3ed-f1dc-4d0f-b861-1be670cc82e6.png)


A Web-App for Interactive and Innovative way of Ordering Food/Drinks in a Restaurant.


![image](https://user-images.githubusercontent.com/72696677/147385238-ad4cd89f-69d6-4547-b1b7-5df01b5276ec.png)


- [Abstract](#abstract)
- [Introduction](#Introduction)
- [Objective](#objective)
- [Features](#features)
- [Tools and Technology Used](#tools)
- [Design and Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [List of Tables](#tables)
- [Bug Reporting](#bug)
- [Feature Request](#feature-request)
- [License](#license)


<a id = "abstract"></a>

## Abstract

+ Nowadays we have to roam around a lot to get a type of environment to fit in. We binge 
search on the internet for some places which can be flexible with the variety and quality 
of food we like to have.
+ This project titled “Meat and Greet Food Exchange” will be a software-based system that 
will make it more flexible for the working class to make it more to grab some 
entertainment with easily available lavish cuisines.
+ Making it more convenient for the customers with beautiful surroundings and an exciting 
system makes meat and greet a happy-to-go place.


<a id = "objective"></a>

## Objective

+ Trying to create a best End-to-End Solution for a Food/Drinks Ordering App which will be of a great use after Covid19 Pandemic where customers fill unsafe while using a HardCopy Menu.
+ Users no longer have to call a Waiter for Ordering or for doing a Payment.
+ Making the Ordering Drinks Task very Interactive and Innovative by Introducing Dynamic Pricing of Drinks(Prices of drinks change while ordering depending on our Algorithm).

<a id = "Introduction"></a>

## Introduction 

+ The Meat and Greet Food Exchange is a dine-in ordering web application for mobile 
devices which helps people to order food or drinks in a club/restaurant. This software 
will be designed to increase restaurant customer interaction and not make them wait for
the waiter to take their order. 
+ This software will be implementing a stock market theme for ordering food as well as drinks. As in a stock market, more demand means higher 
prices similarly, the software should increase the price of the drink based on its demand.
+ TBSE will “trade” * in food and drinks whilst making sure you have a great exchange 
(of conversation, of course!). Starting with all prices starting at retail prices, the prices of 
your favorite food rise in direct proportion to its consumption over a period of time. 
+ Every increasing peg/pint/shot/glass ordered by a patron increases its value margin, to be 
brought down once again if time is on your side (if orders for the same drink decrease 
over a period of time). Before you gasp in worry, our circuit breaker system will ensure 
that you get the best bang for your buck always (whether your favourite stock is high or 
low).


<a id = "features"></a>
## Project Background

- Bar Stock Exchange is Web-Based Mobile Application which can be used in Restaurant-Bars, replacing Hardcopy Menu for Food and Drinks Ordering.

- Users can Scan the QR Code available and user the App.

- Whats Unique about this application is that a Stock Market Theme is implemented while ordering any drink using the application. 

- Prices of Drinks increases and Decreases Dynamically(async) while Ordering drinks, backed by algorithms created for changing the prices.

- Implemented Google Sign Up and Sign In with the help of **GMAIL API** to increase customer experience while using the application.

- Implemented functionalities like - Food Items Filtering based on Newest, Most Ordered, Admin Panel, Social-Auth, Smooth Scrolling, Dynamic Pricing, Dynamic Ordered Item Page, End-to-End Payments Solution.

- Three Django Apps were used which are <b> main, registration and payments </b>.

  - Main App includes these Pages and their different views/functionalities – Home, Explore, Menu, Bar menu, Order Page

  - Registration App contains the Landing(index) Page which is used for scanning the QR code which will redirect user to registration page of app.

  - Payments App provides payment of bill facility to a user. Integrated RazorPay Payments Sytems in which user can pay through all Online Payments modes possible.


<a id = "getting-started"></a>
## Getting Started

### Prerequisites

Latest Stable version of Python should be installed, you can download from [here](https://www.python.org/downloads/)


### Instructions of setting up the project on your local machine

1. Open Terminal and Clone the Repo
```
git clone https://github.com/JUNAID69/MGFE/.git
```
2. Go inside the Project Directory using <b> cd </b> and install the dependencies using the command:

```
pip install -r requirements.txt
```

3. Run Command in the terminal for running the App

```
Python manage.py runserver
```

Your Application Server would be live and you can access the App using url - "http..." 

<a id= "tools"></a>
## Tools and Technology Used

- Front-End Interface - HTML, CSS, JavaScript
- Programming Language - Python(Django)
- Database - sqlite
- Other Technologies - jQuery, Ajax

<a id = "screenshots"></a>
## Few Screenshots

<div align="center">

</div>
 
<a id = "tables"></a>

## List of Tables

+ Users - Stores all the User Data. There are two types of User : Admin Staff of Restaurant and a Customer.
+ FoodMenu - Stores all the data related to Food Products offered by a Restaurant.
+ BarMenu -  Stores all the data related to Bar/Drinks offered by a Restaurant.
+ FoodOrder - Stores all the Food Order of a User.
+ BarOrder - Stores all the Bar Order of a User.
+ Payments - Stores details regarding Bill of a User.
+ Social Accounts - Stores all the data regarding the Social Accounts used while Sign Up.

<a id= "bug"></a>

## 🐛 Bug Reporting

Feel free to [open an issue](https://github.com/JUNAID69/MGFE/BSE/issues) on GitHub if you find any bug.

<a id="feature-request"></a>

## ⭐ Feature Request

- Feel free to [Open an issue](https://github.com/JUNAID69/MGFE/BSE/issues) on GitHub to request any additional features you might need for your use case.

<a id= "feature-request"></a>


<a id="license"></a>

## 📜 License

This software is open source, licensed under the [MIT License](https://github.com/JUNAID69/MGFE/BSE/blob/master/LICENSE).

<!-- # https://django-allauth.readthedocs.io/en/latest/installation.html -->
