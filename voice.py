import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

# 🔊 Safe speak function (fixes run loop error)
def speak(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except:
        pass


# 🔥 Advanced number parser (handles words + decimals)
def word_to_number(text):
    text = text.lower().replace("-", " ")

    # remove units (optional cleanup)
    for unit in ["liters", "liter", "km", "kilometers", "hours", "minutes"]:
        text = text.replace(unit, "")

    words = text.split()

    units = {
        "zero":0, "one":1, "two":2, "three":3, "four":4,
        "five":5, "six":6, "seven":7, "eight":8, "nine":9,
        "ten":10, "eleven":11, "twelve":12, "thirteen":13,
        "fourteen":14, "fifteen":15, "sixteen":16,
        "seventeen":17, "eighteen":18, "nineteen":19
    }

    tens = {
        "twenty":20, "thirty":30, "forty":40,
        "fifty":50, "sixty":60, "seventy":70,
        "eighty":80, "ninety":90
    }

    scales = {
        "hundred":100,
        "thousand":1000
    }

    current = 0
    total = 0
    decimal_part = []
    is_decimal = False

    for word in words:
        if word == "point":
            is_decimal = True
            continue

        if is_decimal:
            if word in units:
                decimal_part.append(str(units[word]))
            elif word.isdigit():
                decimal_part.append(word)
            continue

        if word in units:
            current += units[word]
        elif word in tens:
            current += tens[word]
        elif word in scales:
            current *= scales[word]
        elif word.isdigit():
            current += int(word)

    total += current

    if decimal_part:
        return float(f"{total}." + "".join(decimal_part))

    return float(total)


# 🎤 Main voice Q&A function
def ask_question(question, data_type=str):
    while True:
        try:
            print("\n" + question)
            speak(question)

            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("🎤 Listening...")
                audio = r.listen(source, timeout=5)

            answer = r.recognize_google(audio)
            print("You said:", answer)

            # 🔥 NUMBER HANDLING
            if data_type in [int, float]:
                num = word_to_number(answer)

                if num is not None:
                    return int(num) if data_type == int else float(num)

                # fallback if direct number spoken
                try:
                    return int(answer) if data_type == int else float(answer)
                except:
                    raise ValueError

            return answer

        except sr.UnknownValueError:
            print("❌ Could not understand")
            speak("Please repeat")

        except ValueError:
            print("❌ Please say a valid number like five or five point five")
            speak("Please say a valid number")

        except Exception as e:
            print("Error:", e)
            speak("Something went wrong")

def listen_command():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("🎤 Listening for command...")
            audio = r.listen(source, timeout=5)

        command = r.recognize_google(audio).lower()
        print("Command:", command)
        return command

    except:
        return None