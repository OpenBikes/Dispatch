# Dispatch application

## Setup

### Environment variables

Include a `.env` at the root of the application with the following variables -- the values on the right side are examples.

```
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB_NBR=0
```

## Data simulation

```sh
>>> curl -H "Content-Type: application/json" -X POST -d '{"truck_id": 1, "latitude": 43.604, "longitude": 1.443}' http://localhost:5000/indicate_position
```
