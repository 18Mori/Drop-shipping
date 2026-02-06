# React-Django Users App

This project is a web application that uses React for the frontend and Django for the backend, with a PostgreSQL database to manage user data. The application allows for the management of signed-up users, including viewing their details and submissions, as well as deleting users.

## Project Structure

```
react-django-users-app
├── frontend          # React frontend application
│   ├── package.json  # NPM configuration and dependencies
│   ├── public
│   │   └── index.html # Main HTML file for the React app
│   ├── src
│   │   ├── index.js   # Entry point of the React application
│   │   ├── App.js     # Main App component with routing
│   │   ├── components  # Contains reusable components
│   │   │   ├── UsersTable.js # Component to display users in a table
│   │   │   └── UserDetailsModal.js # Component to show user details
│   │   ├── pages
│   │   │   └── UsersPage.js # Main page for managing users
│   │   ├── services
│   │   │   └── api.js  # API calls to the Django backend
│   │   └── styles
│   │       └── main.css # CSS styles for the application
│   └── .env.example    # Example environment variables for frontend
├── backend             # Django backend application
│   ├── manage.py       # Command-line utility for managing the Django project
│   ├── requirements.txt # Python dependencies for the backend
│   ├── backend
│   │   ├── __init__.py # Marks the backend directory as a Python package
│   │   ├── settings.py # Configuration for the Django project
│   │   ├── urls.py     # URL routing for the Django application
│   │   └── wsgi.py     # Entry point for WSGI-compatible web servers
│   ├── users           # User management app
│   │   ├── __init__.py # Marks the users directory as a Python package
│   │   ├── admin.py    # Registers User model with Django admin
│   │   ├── apps.py     # Configuration for the users app
│   │   ├── models.py   # Defines the User model
│   │   ├── serializers.py # Serializers for User model
│   │   ├── urls.py     # URL routing for user-related endpoints
│   │   └── views.py    # Views for handling user requests
│   └── submissions     # Submissions management app
│       ├── __init__.py # Marks the submissions directory as a Python package
│       ├── models.py   # Defines the Submission model
│       ├── serializers.py # Serializers for Submission model
│       └── views.py    # Views for handling submission requests
├── docker-compose.yml  # Defines services for the application
├── .env.example        # Example environment variables for backend
└── README.md           # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd react-django-users-app
   ```

2. **Set up the backend:**
   - Navigate to the `backend` directory.
   - Create a virtual environment and activate it.
   - Install the required packages:
     ```
     pip install -r requirements.txt
     ```
   - Set up the PostgreSQL database and update the `settings.py` file with your database credentials.
   - Run migrations:
     ```
     python manage.py migrate
     ```
   - Start the Django server:
     ```
     python manage.py runserver
     ```

3. **Set up the frontend:**
   - Navigate to the `frontend` directory.
   - Install the dependencies:
     ```
     npm install
     ```
   - Start the React application:
     ```
     npm start
     ```

## Usage

- Access the application at `http://localhost:3000`.
- You can view the list of signed-up users, delete users, and view their details and submissions.

## License

This project is licensed under the MIT License.