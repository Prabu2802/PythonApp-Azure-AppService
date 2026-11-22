# PythonApp-Azure-AppService

A simple Flask application for deployment to Azure App Service using the **Code** deployment option. The home page displays Netsys Infotech and welcomes visitors to Prabu's Training.

## Run locally

```bash
python -m pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`.

## Deploy to Azure App Service

Create a **Linux Web App** with a Python runtime, then deploy this repository using the **Code** deployment option. App Service installs dependencies from `requirements.txt` and detects the Flask application as `app` in `app.py`. If a startup command is needed, use:

```bash
gunicorn --bind=0.0.0.0 --timeout 600 app:app
```