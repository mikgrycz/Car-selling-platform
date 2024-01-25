


# Car Bazaar

![GitHub stars](https://img.shields.io/github/stars/mikgrycz/Car-selling-platform?style=social)
![GitHub forks](https://img.shields.io/github/forks/mikgrycz/Car-selling-platform?style=social)
![GitHub issues](https://img.shields.io/github/issues/mikgrycz/Car-selling-platform)
![GitHub license](https://img.shields.io/github/license/mikgrycz/Car-selling-platform)
![Python](https://img.shields.io/badge/python-3.9-blue)
![React](https://img.shields.io/badge/react-17.0.2-blue)
![MySQL](https://img.shields.io/badge/mysql-8.0.25-blue)

Car Bazaar is a car trading system that allows users to buy and sell cars online. Users can browse through various car listings, view detailed information, reviews and ratings, and contact the sellers. Users can also create their own listings, upload photos, set prices, and receive offers. Car Bazaar aims to make car trading easy, fast, and secure.

## Table of Contents

- [Car Bazaar](#car-bazaar)
  - [Table of Contents](#table-of-contents)
  - [Demo](#demo)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Backend](#backend)
    - [Frontend](#frontend)
  - [Usage](#usage)
    - [Running the server](#running-the-server)
    - [Running the client](#running-the-client)
  - [Links](#links)

## Demo

![Main Screen](main_screen.png)

![Car Screen](car_screen.png)

![Review Screen](review_screen.png)

## Features

- Multi car view
- Single car view with info about the listing, reviews and options to buy, share and to leave an opinion
- Logging in
- Leaving reviews
- Car listings sorting
- Server structure
- DB connection
- Main screen displaying car listings
- Adding new cars

## Installation

### Prerequisites

- Python 3.9 or higher
- React.js 17.0.2 or higher
- MySQL 8.0.25 or higher
- Node.js 14.17.1 or higher
- npm 6.14.13 or higher

### Backend

- Clone the repository

```bash
git clone https://github.com/mikgrycz/Car-selling-platform.git
```

- Create and activate a virtual environment

```bash
cd car-bazaar
python -m venv venv
source venv/bin/activate
```

- Install the required dependencies

```bash
pip install -r requirements.txt
```

- Create a .env file with your secret keys

### Frontend

- Install the required dependencies

```bash
cd frontend
npm install
```

## Usage

### Running the server

- Start the server

```bash
uvicorn main:app --reload
```

- By default the server will be running on http://localhost:8000

- You can access the API documentation on http://localhost:8000/docs or http://localhost:8000/redoc

### Running the client

- Start the client

```bash
cd frontend
npm start
```

- By default he client will be running on http://localhost:3000



![GitHub stars](https://img.shields.io/github/stars/mikgrycz/Car-selling-platform?style=social)
![GitHub forks](https://img.shields.io/github/forks/mikgrycz/Car-selling-platform?style=social)
![GitHub issues](https://img.shields.io/github/issues/mikgrycz/Car-selling-platform)
![GitHub license](https://img.shields.io/github/license/mikgrycz/Car-selling-platform)
![Python](https://img.shields.io/badge/python-3.9-blue)
![React](https://img.shields.io/badge/react-17.0.2-blue)