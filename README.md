# TutorAI Backend

## Features

- Flask-based server
- CAMEL AI integration
- Dotenv for managing environment variables

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/informedAI/TutorAI-backend.git
cd tutorAI-backend
```

### 2. Set Up a Python Environment

Use either a virtual environment or Conda.

#### Virtual Environment

```sh
python -m venv venv
source venv/bin/activate
```

#### Conda

```sh
conda create --name tutorAI-backend python=3.12
conda activate tutorAI-backend
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Create and Update Your .env File

Create a file named `.env` in the project root:

```
AIML_API_KEY="your_api_key"
```

Replace `your_api_key` with your actual API key.

### 5. Run the Flask App

```sh
python app.py
```

The application will start in debug mode at `http://127.0.0.1:5000/`.
