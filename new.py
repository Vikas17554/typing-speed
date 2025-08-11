# typing_test_web.py
import streamlit as st
import random
from time import time

sentences = [
    "hello my name is vikas",
    "the sky is blue as ocean",
    "kismat ka khel hai bhai 10 lakh lpa nhi milag",
    "kuch toh log kahenge logo ka kaam hai kehna"
]

def count_errors(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    error += abs(len(partest) - len(usertest))
    return error

def speed(start, end, user_input):
    duration = end - start
    duration = max(duration, 0.01)
    return round(len(user_input) / duration)

st.title("🧠 Typing Speed Test")
if "start_time" not in st.session_state:
    st.session_state.start_time = 0
if "original" not in st.session_state:
    st.session_state.original = ""

if st.button("Start Test"):
    st.session_state.original = random.choice(sentences)
    st.session_state.start_time = time()

if st.session_state.original:
    st.markdown("### Type this:")
    st.code(st.session_state.original)

    typed = st.text_area("Start typing here...", height=150)
    if st.button("Submit"):
        end_time = time()
        user_speed = speed(st.session_state.start_time, end_time, typed)
        user_errors = count_errors(st.session_state.original, typed)
        duration = round(end_time - st.session_state.start_time, 2)

        st.success(f"Speed: {user_speed} characters/sec")
        st.info(f"Time Taken: {duration} seconds")
        st.warning(f"Errors: {user_errors}")

        # Reset
        st.session_state.original = ""
