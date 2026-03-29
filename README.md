
-----

# 🌦️ Climate-Based Dress Suggestion API

Developed by **[NithishProgrammer](https://github.com/NithishProgrammer)**

A lightweight, FastAPI-powered microservice that suggests appropriate clothing and precautions based on the real-time weather of any city. This API acts as a smart bridge between live meteorological data and daily lifestyle choices.

## 🚀 Features

  * **Real-time Weather Integration:** Fetches live data via OpenWeatherMap.
  * **Smart Clothing Logic:** Categorizes weather conditions (Rain, Clear, Haze, etc.) and provides tailored attire advice.
  * **Safety First:** Includes specific safety tips for reduced visibility or hazardous conditions.
  * **Developer Friendly:** Built with FastAPI, offering automatic Swagger documentation.

-----

## 🛠️ Tech Stack

  * **Python 3.x**
  * **FastAPI:** High-performance web framework.
  * **Requests:** For synchronous API communication.
  * **Uvicorn:** ASGI server for production-ready deployment.

-----

## 📋 Getting Started

### 1\. Prerequisites

  * Python installed on your machine.
  * An API Key from [OpenWeatherMap](https://openweathermap.org/api).

### 2\. Installation

```bash
# Clone the repository
git clone https://github.com/NithishProgrammer/weather-dress-api.git
cd weather-dress-api

# Install dependencies
pip install fastapi requests uvicorn
```

### 3\. Usage

Run the server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

-----

## 📖 API Documentation

### Get Suggestion

**Endpoint:** `GET /city`

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `city` | `string` | Yes | Name of the city (e.g., `Puducherry`, `London`). |

**Example Request:**
`GET /city?city=Chennai`

**Example Response:**

```json
{
  "Suggesting": "Nothing.. Just light sunscreen"
}
```

-----

## 🛡️ Security Note for Contributors

When contributing to this project, **never hardcode your API Key**. Use a `.env` file or environment variables to keep your credentials secure.

```python
# Recommended way to load keys
import os
API_KEY = os.getenv("WEATHER_API_KEY")
```

-----

## 🤝 Contributing

Contributions are what make the open-source community an amazing place to learn and create.

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 📄 License

This project is open-source and available under the **MIT License**.

-----

**Would you like me to help you create a `.gitignore` file so your local environment files don't accidentally get uploaded to your GitHub?**
