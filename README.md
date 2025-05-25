# PlayStation Technical Challenge

For information on design see the [design section of the docs](./docs/design/index.md). Of particular
importance is the [Key Assumptions](./docs/design/key-assumptions.md) page which has a potential impact
on the correctness of the solution.

## Getting Started

### Setup and Run

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