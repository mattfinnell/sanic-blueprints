# Sanic Blueprint POST bug

## Info
Sanic Blueprints (with a set `url_prefix` parameter) wont tolerate `POST` requests

`sanic.exceptions.InvalidUsage: Method POST not allowed for URL /api/failing`

- This seems to only affect blueprints that have the `url_prefix` parameter set
- [super weird] POST request will work if it is the only route in the blueprint

## Running
```sh
git clone https://github.com/mattfinnell/sanic-blueprints.git

cd sanic-blueprints

pipenv install

pipenv run python main.py
```

## Checking Endpoints

I was using [postman](https://www.getpostman.com/) for checking the following endpoints, here is a shorthand of what I was testing

```sh
  # Passing Endpoints
  GET localhost:8000/api/passing
  GET localhost:8000/api/failing
  POST localhost:8000/api/passing --headers {"some": "data"}

  # Failing Endpoint
  POST localhost:8000/api/failing --headers {"some": "data"}
```

The Failing POST request returns a `sanic.exceptions.InvalidUsage: Method POST not allowed for URL /api/failing` error.
