# Flask: Python's web framework

## Goal:

This folder helps you to find how Flask works!

## Step-by-Step Explaination

### Requirements

```sh
flask
```

### Install Flask

```sh
pip install flask
```

### Import Flask

```python
from flask import Flask
```

### Initialize Flask App

```python
app = Flask(__name__)
```

### Use the route()

Use the `route()` decorator to tell Flask what URL should trigger our function.
```python
@app.route('/') # or /home or /about
```

### Define a function

```python
def hello():
    return "Hello, World"
```
This function return "Hello, World" in `/` route

### Run the app

```python
if __name__ == "__main__":
    app.run()
```
press f5

### Run with Terminal

```sh
flask --app filename run

### You should see this output on Terminal

```sh
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

- Then go to the following url in your browser
- http://127.0.0.1:5000


### Example of output:

<img src="./static/images/Screenshot from 2025-10-22 17-13-44.png">