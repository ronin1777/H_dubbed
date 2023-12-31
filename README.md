# H_dubbed
This is an API Movie review using Django Rest Framework ,with user achievment and badge system.
# Table of Contents
* [Introduction](https://github.com/ronin1777/H_dubbed/blob/main/README.md#introduction)
* [Features](https://github.com/ronin1777/H_dubbed/blob/main/README.md#features)
* [technology](https://github.com/ronin1777/H_dubbed/blob/main/README.md#technology)
* [How to use](https://github.com/ronin1777/H_dubbed/blob/main/README.md#setup-and-run)
# Introduction
This is a movie review project, users have levels and points, and users' levels are increased based on their activities (such as passing quizzes).Also, users have badges and after performing the specified activities, they can get those badges and The process followed for each user to get the badges is specified.
# Features
* Social network Registration via django-allauth
* Registeration and Confirm email adress using link via generate unique token
* Authentication via JWT
* Media storage using Amazon S3
* Test Driven Development(TDD) and Run tests with unittest
* Implement Badge System
* User Level and Point and Achievment system
* Quiz App
* RATING and Review for Post, Comment, Reply via Generic-relation and content-type
# technology
* Celery
* Postgres
* JWT
* Django Rest Framework
* Redis
# Setup and Run
1. Clone the repo:
```python
pip install -r requirements.txt
```
3. Configure a virtual
```python
python3 -m venv .venv
```
4. install -r requirements
```python
pip install -r requirements.txt
```
5. set up database
```python
python3 manage.py makemigrations
python3 manage.py migrate
```
Author:
> Hosein Sayah
> Email: hoseincomiser27@gmail.com
> ========Thank You !!!=========.
