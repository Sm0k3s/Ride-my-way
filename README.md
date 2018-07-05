# RIDE MY WAY API
[![Build Status](https://travis-ci.org/Sm0k3s/Ride-my-way.svg?branch=ft-modify-ride-158812548)](https://travis-ci.org/Sm0k3s/Ride-my-way)
[![Coverage Status](https://coveralls.io/repos/github/Sm0k3s/Ride-my-way/badge.svg?branch=master)](https://coveralls.io/github/Sm0k3s/Ride-my-way?branch=master)
## Description

An API that enables CRUD methods for creating rides and accessing users for the ride my way app

## Installation

* Clone this repo 

```bash
$ git clone https://github.com/sm0k3s/ride-my-way.git
```
* Cd into it
* Make a virtual environment and activate it

```bash
$ virtualenv venv
$ venv/bin/activate
```
* Install the dependencies 

```
$ pip install -r requirements.txt
```

* Run the app

 ```bash
 $ python run.py
 ```

* Test the endpoints are working on Postman/Curl

## Running tests
```bash
$ pytest
```
## Endpoints
| Endpoints                                      | Description                                      |
|------------------------------------------------|--------------------------------------------------|
| POST /api/v1/auth/signup                       | Register user                                    |
| POST /api/v1/auth/login                        | Log in user                                      |
| POST /api/v1/auth/logout                       | Log out user                                     |
| GET /api/v1/rides								     |	Fetch all available rides						|
| GET /api/v1/rides/<rideId>						|	Fetch the details of a single ride	|
| POST /api/v1/rides/<rideId>/requests | Make a ride request 			 |
| POST /api/v1/users/rides		|Create a ride offer 	|
| GET /api/v1/users/rides/<rideId>/requests		|	Fetch all ride requests 			|
| PUT /api/v1/users/rides/<rideId>/requests/<requestId> 	| Accept or reject a ride request. 	|
