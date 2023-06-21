# Dealflow Freelancers API

Welcome to the Dealflow Freelancers API! This API allows you to fetch and search for freelancers on Dealflow based on various criteria.

## Problem Statement

The goal of this project is to provide a set of RESTful APIs that enable clients to retrieve all available freelancers on Dealflow and perform searches by first name, last name, email, phone number, and followers on a social media platform. The API should also support pagination to handle large result sets efficiently. The freelancers' data should be stored in a database.

## Solution

The Dealflow Freelancers API is built using Django and Django REST Framework. It provides the following endpoints:

- `/api/v1/freelancers/`: Retrieves all freelancers or performs searches based on query parameters for first name, last name, email, phone number, and followers.
- `/api/v1/freelancers/{id}/`: Retrieves a specific freelancer by ID.
- `/api/v1/brands/`: Retrieves all brands.
- `/api/v1/brands/{id}/`: Retrieves a specific brand by ID.

The API supports pagination using query parameters such as `page` and limit and offset to control the number of results per page.

## Installation

1. Clone the repository: `git clone https://github.com/Monil-Karia/DealFlow-Challenge-Backend.git` 
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the Django project:
    - Add the path to your Django project in `settings.py`.
    - Set the `DJANGO_SETTINGS_MODULE` environment variable to `Main_Challengev2.settings`.
    - Run database migrations: `python manage.py migrate`
4. Populate the database with sample data:
    - Run the `data.py` script to create and save freelancer objects.
    - Run the `brand_data.py` script to create and save brand objects.

## Usage

1. Start the Django development server: `python manage.py runserver`
2. Access the API endpoints at `http://localhost:8000/api/v1/`.
3. Perform GET requests to retrieve freelancers and brands. Use query parameters for searching and pagination.

### API Endpoints

- `/api/v1/freelancers/`
    - `GET`: Retrieves all freelancers or performs searches by query parameters.
    - Query Parameters:
        - `first_name`: Filters freelancers by first name.
        - `last_name`: Filters freelancers by last name.
        - `email`: Filters freelancers by email.
        - `phone_number`: Filters freelancers by phone number.
        - `followers`: Filters freelancers by followers.
        - `page`: Controls the page number for pagination.
- `/api/v1/freelancers/{id}/`
    - `GET`: Retrieves a specific freelancer by ID.
- `/api/v1/brands/`
    - `GET`: Retrieves all brands.
- `/api/v1/brands/{id}/`
    - `GET`: Retrieves a specific brand by ID.

## Contributing

Contributions to the Dealflow Freelancers API are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).****
