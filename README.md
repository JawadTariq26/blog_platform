# 📝 AI-Powered Flask Blog CMS

A dynamic web application built with **Python Flask** that allows administrators to manage content effortlessly.The platform features an AI-powered post
generator powered by OpenRouter alongside traditional manual blogging tools.

## 🚀 Features

### For Admins
* **AI Post Generation:** Simply provide a topic, and the integrated OpenRouter API generates a complete blog post.
* **Manual Post Creation:** Full control to write and format posts from scratch.
* **Full CRUD Functionality:** Edit, update, and delete existing posts through a dedicated dashboard.

### For Users
* **View Posts:** Browse and read all published content.
* **Interactive Comments:** Share thoughts and engage with posts through a comment system.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Database:** SQLite3
* **AI Integration:** OpenRouter API (OpenAI Python SDK)
* **Frontend:** HTML5, CSS3, Jinja2 Templates, Bootstrap

## 🏁 Getting Started

### Prerequisites
* Python 3.x
* An API Key from OpenRouter

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd your-repo-name
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key_here
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

5. **Run the application:**
   ```bash
   flask run
   ```
