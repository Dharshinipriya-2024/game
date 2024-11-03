import streamlit as st
import random

# Set up the title of the app
st.title("Number Guessing Game")

# Define the range for the random number
number_range = st.slider("Select the range for the number:", 1, 100, 50)

# Initialize session state
if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, number_range)
    st.session_state.attempts = 0

# Display the number of attempts
st.write(f"You have made {st.session_state.attempts} attempts.")

# Get user input
guess = st.number_input("Enter your guess:", min_value=1, max_value=number_range, step=1)

# Button to submit guess
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.number_to_guess:
        st.write("Too low! Try again.")
    elif guess > st.session_state.number_to_guess:
        st.write("Too high! Try again.")
    else:
        st.write(f"Congratulations! You guessed the number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts.")
        # Reset game
        if st.button("Play Again"):
            st.session_state.number_to_guess = random.randint(1, number_range)
            st.session_state.attempts = 0

# Button to reset the game
if st.button("Reset Game"):
    st.session_state.number_to_guess = random.randint(1, number_range)
    st.session_state.attempts = 0
    st.write("Game has been reset. Start guessing!")
