# Django CRM App

This is a Django-based CRM (Customer Relationship Management) application with basic CRUD (Create, Read, Update, Delete) functionalities.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Views](#views)
- [Django Authentication](#django-authentication)
- [Django Migration Commands](#django-migration-commands)
- [Contributing](#contributing)

## Installation

To set up the project, follow these steps:

1. Clone the repository:

    ```
    git clone https://github.com/onkarlapate27/crm_website/tree/development
    ```

2. Navigate into the project root directory:

3. Install dependencies using `requirements.txt`:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run migrations to create the database schema:

    ```
    python manage.py migrate
    ```

2. Start the development server:

    ```
    python manage.py runserver
    ```

3. Access the application at `http://localhost:8000` in your web browser.

## Models

The following models are used in the application:

- **Customer**: Represents information about customers.
- **User**: Using django internal model for authentication related data.

## Views

The application contains following views:

- **customer_view**: contains APIs for performing CRUD operations for customers.
- **home_view**: redirects to home page.
- **user_view**: APIs related to authentication and user registration.

## Django Authentication

Django's built-in authentication system is utilized for user authentication. Users can log in, log out, and change their passwords.

## Django Migration Commands

To manage database schema changes, use Django's migration commands. Some common commands include:

- `python manage.py makemigrations`: Creates new migrations based on changes to the models.
- `python manage.py migrate`: Applies migrations to the database.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/my-feature`).
6. Create a new Pull Request.

