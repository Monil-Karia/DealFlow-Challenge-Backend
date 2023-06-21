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

1. **Fetch All Available Freelancers**
   - Endpoint: `GET /api/v1/freelancers/`
   - Description: Retrieves a list of all available freelancers on Dealflow.
   - Parameters: None
   - Response: List of freelancer objects with details such as `freelancer_id`, `first_name`, `last_name`, `email`, `phone_number`, `brand`, `followers`, `added_data`, and `social_media`.

2. **Search Freelancers**
   - Endpoint: `GET /api/v1/freelancers/?first_name=<first_name>&last_name=<last_name>&email=<email>&phone_number=<phone_number>&followers=<followers>`
   - Description: Searches for freelancers based on the provided parameters. You can search by `first_name`, `last_name`, `email`, `phone_number`, and/or `followers`.
   - Parameters:
     - `first_name` (optional): Filters freelancers by first name.
     - `last_name` (optional): Filters freelancers by last name.
     - `email` (optional): Filters freelancers by email.
     - `phone_number` (optional): Filters freelancers by phone number.
     - `followers` (optional): Filters freelancers by number of followers on a social media platform.
   - Response: List of freelancer objects that match the search criteria.

3. **Pagination**
   - Endpoint: `GET /api/v1/freelancers/?page=<page_number>&page_size=<page_size>`
   - Description: Retrieves a paginated list of freelancers. Supports pagination to navigate through the results.
   - Parameters:
     - `page` (optional): Specifies the page number to retrieve (default: 1).
     - `page_size` (optional): Specifies the number of freelancers per page (default: 10).
   - Response: Paginated list of freelancer objects.

Please note that these endpoints assume the base URL is `http://localhost:8000/` (adjust accordingly based on your deployment configuration). Also, ensure that you have properly configured your Django project and installed the required packages before using the API.

## Contributing

Contributions to the Dealflow Freelancers API are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).****
