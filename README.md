# PlayStation Technical Challenge

For information on design see the [design section of the docs](./docs/design/index.md). Of particular
importance is the [Key Assumptions](./docs/design/key-assumptions.md) page which has a potential impact
on the correctness of the solution.

For thoughts on technology choices see the [Tech Choices](./docs/tech-choices.md) page.

NOTE: The Docker image and setup is incomplete due to lack of time. As such this API needs to be run right
on the desktop. Instructions follow after the endpoints section.

## Endpoints

* Get all users: `/users`
  * Filter by level: `/users?level=bronze` 
* Get single user: `/users/{user_id}`
* API docs: `/docs`

## Getting Started

### Setup and Run

#### Quickstart

The API that I was sent has not been included in this repository. If you'd like me to include it I'm happy to
commit.

```
python -m venv venv
pip install -r requirements.txt
java -jar ./remote-api/playstation-tech-test-api.jar
flask --app ps_challenge.app run
```

To see the unittests, check this repo's [latest build](https://github.com/VesnaBrucoms/ps-technical-challenge/actions/workflows/test_on_commit.yaml) or run `python -m unittest -v`.

#### Remaining Commands

Create and enter a virtual environment:

    python -m venv venv

or create through VSCode.

Install dev requirements to virtual environment:

    pip install -r requirements.txt

Install package to virtual environment:

    pip install .

Run with the development server:

    flask --app ps_challenge.app run

Access on `http://127.0.0.1:5000/`.

To instead run without debug mode:

    flask --app ps_challenge.app run --host=0.0.0.0

The Dockerfile uses this for the container to run with.

### Testing

    python -m unittest -v

#### Remote API

    java -jar ./remote-api/playstation-tech-test-api.jar

### Docker

Build this project's image tagged as `ps-technical-challenge`:

    docker build -t ps-technical-challenge .

To list images:

    docker image list