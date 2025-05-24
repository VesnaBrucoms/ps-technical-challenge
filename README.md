# PlayStation Technical Challenge

For information on [design](./docs/design/index.md).

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

### Testing

    python -m unittest -v

#### Remote API

    java -jar ./remote-api/playstation-tech-test-api.jar

### Docker

    docker build .