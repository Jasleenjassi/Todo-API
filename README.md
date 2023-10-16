 # TODO API

This is a simple TODO API built with FastAPI. It allows you to create, get, update, and delete TODO items.

## Prerequisites

To run this API, you will need:

* Python 3.6 or later
* FastAPI
* Uvicorn

## Installation

1. Install Python 3.6 or later.
2. Install FastAPI:

```
pip install fastapi
```

3. Install Uvicorn:

```
pip install uvicorn
```

## Usage

To run the API, simply run the following command:

```
uvicorn main:app --host 127.0.0.1 --port 8000
```

This will start the API on port 8000.

## Endpoints

The API provides the following endpoints:

* `/todos/`: Create a TODO item.
* `/todos/`: Get all TODO items.
* `/todos/{todo_id}`: Get a single TODO item.
* `/todos/{todo_id}`: Update a TODO item.
* `/todos/{todo_id}`: Delete a TODO item.

## Code Explanation

The code for the API is located in the `main.py` file. Let's go through the code step by step to understand how it works.

### Import Libraries

The first step is to import the necessary libraries.

```
from fastapi import FastAPI
```

### Create a FastAPI App

Next, we create a FastAPI app.

```
app = FastAPI()
```

### Define TODO Items Database

We then define a dictionary to store TODO items.

```
# TODO items database
todos = {}
```
