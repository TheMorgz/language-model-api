# Language Model API

A RESTful API for text completion and summarization using Hugging Face's Transformers library, built with FastAPI.

---

## Features

- **Text Completion**: Generate text based on a prompt.
- **Text Summarization**: Summarize long text into a shorter version.
- **Docker Support**: Easily deploy the application using Docker and Docker Compose.
- **Testing**: Includes unit tests for the API and utility functions.

---

## Setup

### Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerized deployment)
- Docker Compose (optional, for multi-container management)

---

### Local Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/language-model-api.git

    cd language-model-api
2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv

    source venv/bin/activate

    pip install -r requirements.txt
3. Run the application:

    ```bash
    uvicorn app.main:app --reload
4. Access the API at:

    ```bash
    http://localhost:8000

---

### Docker Setup

1. Build and run the application using Docker Compose:

    ```bash
    docker-compose up OR docker-compose up -d
2. Access the API at:

    ```bash
    docker-compose up
3. To stop the application:

    ```bash
    docker-compose down

---

### Running Tests (Locally or Docker)

#### Locally

1. Install pytest if not already installed:

    ```bash
    pip install pytest
2. Run the tests:

    ```bash
    pytest tests/

#### Using Docker Compose

1. Run the tests in an isolated Docker container:

    ```bash
    docker-compose run tests

---

### API Endpoints

#### Text Completion

- Endpoint: `POST /complete`

- Input:

    ```json
    {
        "prompt": "Once upon a time",
        "max_length": 50
    }
- Output:

    ```json
    {
        "completed_text": "Once upon a time, there was a..."
    }

#### Text Summarization

- Endpoint: POST /summarize

- Input:

    ```json
    {
        "text": "A long article about something very important...",
        "max_length": 130,
        "min_length": 30
    }

---

### Docker Compose Configuration

The docker-compose.yml file defines two services:

1. app:

    - Runs the FastAPI application.

    - Maps port 8000 on the host to port 8000 in the container.

    - Enables hot-reloading for development.

2. tests:

    - Runs the unit tests using pytest.

    - Uses the same Docker image as the app service.

---

### Testing

#### Test Files

- `tests/test_api.py`: Contains unit tests for the API endpoints and utility functions.

#### Running Tests

- Locally:

    ```bash
    pytest tests/
- Using Docker Compose:

    ```bash
    docker-compose run tests

---

### Future Improvements

- Add authentication (e.g., API keys or OAuth).

- Support for more language model tasks (e.g., translation, sentiment analysis).

- Integration with a database for logging and analytics.

- Add CI/CD pipeline for automated testing and deployment. (Attempted for now)

---
