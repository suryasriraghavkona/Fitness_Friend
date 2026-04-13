import streamlit as st
from voice import ask_question, listen_command, speak
from database import insert_data, fetch_data
from analytics import show_dashboard

st.title("🎤 AI Fitness Voice Assistant")

st.write("Control everything using your voice")

if st.button("Start Voice Assistant"):

    speak("Welcome to fitness assistant")
    
    while True:
        speak("Say a command: start tracking, show dashboard, or exit")

        command = listen_command()

        if not command:
            continue

        # 🔥 EXIT
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        # 🔥 START TRACKING
        elif "start" in command or "track" in command:
            name = ask_question("What is your name?")
            age = ask_question(f"{name}, what is your age?", int)

            water = ask_question("How much water did you drink?", float)
            sleep = ask_question("How many hours did you sleep?", float)
            walk = ask_question("How many kilometers did you walk?", float)
            workout = ask_question("Workout minutes?", float)

            insert_data("water", water)
            insert_data("sleep", sleep)
            insert_data("walk", walk)
            insert_data("workout", workout)

            speak("Data saved successfully")
            st.success("✅ Data saved!")

        # 🔥 SHOW DASHBOARD
        elif "dashboard" in command or "show" in command:
            data = fetch_data()
            if data:
                show_dashboard(data)
                speak("Showing dashboard")
            else:
                st.info("No data available")
                speak("No data available")

        else:
            speak("Command not recognized")