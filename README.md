
# Flask REST API Project

## Project Overview
This project is a simple REST API built using Python and Flask. It provides two endpoints that return JSON responses and supports both GET and POST requests.

## Technologies Used
- Python
- Flask
- Postman
- Git and GitHub

## API Endpoints

### GET /hello
Returns a welcome message.

Example response:
```json
{
  "message": "Welcome to my Flask API!"
}
```

### GET /data
Returns a sample list of students in JSON format.

### POST /data
Accepts JSON data and returns the received information.

Example request:
```json
{
  "name": "Minh",
  "age": 21,
  "major": "Computer Science"
}
```

## Installation and Setup

1. Clone the repository.
2. Install dependencies:
   `python -m pip install -r requirements.txt`
3. Run the application:
   `python app.py`
4. The API runs at `http://127.0.0.1:5000`.

## API Testing
All endpoints were tested using Postman.

- GET /hello - 200 OK
- GET /data - 200 OK
- POST /data - 201 Created

Screenshots of the successful API requests are available in the screenshots folder.

## Agile Development Process
This project followed a simple Agile workflow using GitHub Projects.

Tasks were organized into three columns:
- Todo
- In Progress
- Done

The project was divided into five tasks:
1. Set up Flask project
2. Implement GET /hello endpoint
3. Implement GET and POST /data endpoint
4. Test API endpoints using Postman
5. Write README and finalize GitHub repository

Tasks were moved between columns as development progressed.

## Future Improvements
- Add a database for persistent data storage.
- Implement additional REST API endpoints.
- Add automated API testing.
