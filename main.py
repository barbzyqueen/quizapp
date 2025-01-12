import streamlit as st
from question_model import Question
from quiz_brain import QuizBrain
from fetch_questions import fetch_questions

# App title
st.title("Dynamic Trivia Quiz App")
st.write("Customize your quiz and test your knowledge!")

# Quiz settings
st.sidebar.header("Quiz Settings")
amount = st.sidebar.slider("Number of Questions", 5, 20, 10)
difficulty = st.sidebar.selectbox("Select Difficulty", ["easy", "medium", "hard"])
start_quiz = st.sidebar.button("Start Quiz")

# Initialize quiz
if start_quiz:
    st.write("Fetching questions... Please wait.")
    try:
        # Fetch questions
        questions_data = fetch_questions(amount=amount, difficulty=difficulty)
        if not questions_data:
            st.error("No questions found. Please try different settings.")
        else:
            # Create question bank
            question_bank = [
                Question(q["question"], q["correct_answer"]) for q in questions_data
            ]

            # Start the quiz
            quiz = QuizBrain(question_bank)
            st.session_state["quiz"] = quiz  # Save quiz object in session state
            st.session_state["quiz_active"] = True
            st.rerun()  # Ensure app refreshes to load the quiz
    except Exception as e:
        st.error(f"Failed to fetch questions: {e}")

# Quiz interface
if st.session_state.get("quiz_active"):
    quiz = st.session_state["quiz"]
    if quiz.still_has_questions():
        current_question = quiz.question_list[quiz.question_number]
        st.subheader(f"Q.{quiz.question_number + 1}: {current_question.text}")
        user_answer = st.radio("Your Answer:", ["True", "False"], key=quiz.question_number)
        if st.button("Submit"):
            # Check the user's answer
            is_correct, correct_answer = quiz.check_answer(user_answer)

            # Save feedback messages in session state
            st.session_state["feedback"] = {
                "is_correct": is_correct,
                "correct_answer": correct_answer,
                "score": quiz.score,
                "total_questions": len(quiz.question_list),
            }

            # Update the quiz progress
            st.session_state["quiz"] = quiz
            st.rerun()  # Refresh to display feedback
    else:
        st.balloons()
        st.success(f"Quiz Complete! Your final score is {quiz.score}/{len(quiz.question_list)}.")
        st.session_state["quiz_active"] = False

# Display feedback if available
if "feedback" in st.session_state:
    feedback = st.session_state["feedback"]
    if feedback["is_correct"]:
        st.success("You got it right!")
    else:
        st.error("That's wrong.")
    st.info(f"The correct answer was: {feedback['correct_answer']}")
    st.info(f"Your score: {feedback['score']}/{feedback['total_questions']}")
