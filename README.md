# genus-moeda

The goal of this project is to convert different currencies.
To do that, I implemented a solution using Currancylayer as a source of information. 

I have some observations to do yet. First of all, you have to sign up on https://currencylayer.com/ and generate a token and change the value on the constants.py file. Another point of attention is the password of your database has to be changed on docker-compose.yml and mysql_context.py.

If you like this code and you want to run it, you need to follow these steps:

1 - Clone the repository

2 - Download Docker

3 - Download docker-compose

4 - Open your terminal and run docker-compose up -d --build command

After these steps, docker will download all necessary tools and will launch the API on port 5001.

If you really enjoyed you can contact me on LinkedIn - https://www.linkedin.com/in/gabriel-araujo-dantas-aa4318117/ 

When I will start a new project I like to think the simplest possible, so I choose for this project these frameworks and tools.

I will start with the programming language, I choose Python because Python is a simple language, easy to work with JSON, has many database connectors, has many REST frameworks and I could implement it fast.

I worked with the Flask framework because Flask is a light and fast REST framework and is easy to configure.

I choose a Relational Database (MySQL) because is simpler than NoSQL databases to explain my model. MySQL was a SGDB I had installed on my PC.
