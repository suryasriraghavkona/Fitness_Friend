# 🎤 AI Fitness Voice Assistant

A **voice-controlled fitness tracking system** built using Python that allows users to log daily activities through speech and visualize their health data in an interactive dashboard.

---

## 🚀 Features

* 🎤 Voice-based input (Speech Recognition)
* 🧠 Smart parsing of spoken numbers (e.g., *“five point five”, “twenty three”*)
* 🗄️ SQLite database for data storage
* 📊 Interactive dashboard with charts
* 🔄 Fully voice-controlled navigation system
* 🔊 Text-to-speech responses
* ⚠️ Smart health suggestions

---

## 🧠 How It Works

1. User gives voice command (e.g., *“start tracking”*)
2. System asks questions via voice + display
3. User responds using speech
4. Input is processed and stored in database
5. Dashboard visualizes the fitness data

---

## 📁 Project Structure

```
fitness_friend/
│── app.py           # Main controller (app flow)
│── voice.py         # Voice input & speech output
│── parser.py        # Text parsing & data extraction
│── database.py      # SQLite database operations
│── analytics.py     # Data visualization
│── requirements.txt
```

---

## 🛠️ Tech Stack

* **Python**
* **SpeechRecognition** (voice input)
* **pyttsx3** (text-to-speech)
* **Streamlit** (UI)
* **SQLite** (database)
* **Pandas & Matplotlib** (data analysis & charts)

---

## ▶️ Installation & Setup

### 1. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
streamlit run app.py
```

---

## 🎤 Voice Commands

| Command          | Action             |
| ---------------- | ------------------ |
| "start tracking" | Begin data entry   |
| "show dashboard" | View analytics     |
| "exit"           | Stop the assistant |

---

## 🧪 Example Inputs

* “I drank five liters of water”
* “I slept seven hours”
* “I walked five point five kilometers”

---

## 📊 Output

* Activity trends over time
* Pie chart of activity distribution
* Smart health recommendations

---

## 🏆 Key Highlights

* Modular architecture (separation of concerns)
* Voice-first user experience
* Real-time analytics dashboard
* Natural language number parsing
* Scalable and maintainable design

---

## 📌 Future Improvements

* 🔐 User authentication system
* ☁️ Cloud deployment (AWS / Render)
* 🤖 AI-based fitness recommendations
* 📱 Mobile app integration

---

## 🙌 Acknowledgements

* Google Speech Recognition API
* Open-source Python libraries

---

