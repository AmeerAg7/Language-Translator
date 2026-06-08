# Language-Translator

Blog Link - https://machinelearningprojects.net/language-translator/


## Project Description

A Flask web application that translates text using the RapidAPI Google Translate service.

---

## Requirements

- Python 3.13+
- Docker
- RapidAPI key

---

## Local Run

### Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```
---

## Docker Build
### Build the Docker image:

```bash
docker build -t translator-app .
```
---

## Docker Run

### Run the container:
```bash
docker run --name translator-container -p 5001:5000 --env-file .env translator-app
```
### Open:
  http://localhost:5001

---

## Environment Variable

| Variable | Description |
|----------|-------------|
| API_KEY | RapidAPI key used for translation requests |


