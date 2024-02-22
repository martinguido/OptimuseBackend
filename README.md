# OptimuseBackend

Optimuse Assignment

## Usage

This project can be run in two ways: using Docker or running locally with Python and uvicorn.

### Running with Python and uvicorn locally

1. Ensure you have Python 3.8 with pip installed. You can download it from [Python's official website](https://www.python.org/downloads/).

2. Open the folder where the project was cloned or downloaded. Open a terminal and install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

3. In the terminal at the same location, run the following code:

```bash
python -m uvicorn main:app --reload
```

### Running with Docker

1. Ensure you have Docker installed. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop/).

2. Open the folder where the project was cloned or downloaded. Run the following code to build the backend image:

```bash
docker build -t optimuse-backend .
```

3. Run the image locally with:

```bash
docker run -d -p 8000:8000 optimuse-backend
```

## Documentation

The API documentation is automatically generated when running and can be accessed at:

- [Swagger UI](http://localhost:8000/docs).

## Endpoints

App must be running

- [/health](http://localhost:8000/health): it returns an object with the current state of the backend server.

- [/asset/{asset_id}](http://localhost:8000/asset/1):it returns an object with the energy demand for the requested asset in the link. If you click the link, you can see the generated metrics for the asset with id = 1, but you can change it. The asset_id must be an integer between 1-3. If you decide not to use a digit or the digit is not found as an asset id, it will raise an exception and a different HTTP code to notify the user.
