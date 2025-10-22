# API in Python

## Goal:

This exercise helps you to understand how to use API and requests

## Step-by-Step Explaination

### Requirements:

You need these modules to work with API
```sh
requests
json
```

### Import modules

```python
import json
import requests
```

### API URL

Find an API-URL to use that
For example: 
- http://api.open-notify.org/astros.json

```python
api_url = "http://api.open-notify.org/astros.json"
```

### request to API

```python
response = requests.get(api_url, timeout=10)
```

### Convert response to json

```python
json_data = response.json()
```

### Use the extracted data

```python
print("Number of people in space: ", json_data["number"])
```