# Dynamic Trivia Quiz App

## Overview
The **Dynamic Trivia Quiz App** is a customizable quiz application built using Python and Streamlit. This app allows users to select the number of questions, difficulty levels, and dynamically fetch trivia questions from the Open Trivia Database API. It tests users' knowledge while providing immediate feedback and scoring.

## Quiz App URL
https://trivia-quiz-app.streamlit.app/

## Features
- Dynamic question fetching from the [Open Trivia Database API](https://opentdb.com/).
- User-selectable number of questions (5-20).
- Three difficulty levels: Easy, Medium, Hard.
- Instant feedback for each question.
- Real-time score tracking.
- Interactive and user-friendly interface using Streamlit.

## Prerequisites
Ensure you have the following installed:
- Python 3.7 or later
- Streamlit
- Requests

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dynamic-trivia-quiz-app.git
   cd dynamic-trivia-quiz-app
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv quiz-venv
   source quiz-venv/bin/activate    # On Windows: quiz-venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```
2. Customize your quiz preferences in the sidebar:
   - Select the number of questions.
   - Choose a difficulty level.
   - Click the **Start Quiz** button.
3. Answer the questions and view your score in real-time.

## Files and Directories
- **main.py**: The entry point of the application.
- **fetch_questions.py**: Handles fetching questions from the Open Trivia Database API.
- **question_model.py**: Defines the `Question` class to represent quiz questions.
- **quiz_brain.py**: Contains the `QuizBrain` class to manage quiz logic.
- **requirements.txt**: Lists all required dependencies for the project.

## Deployment
To deploy the app:
1. Push the repository to GitHub (already completed).
2. Follow the steps to deploy your app on [Streamlit Community Cloud](https://streamlit.io/cloud).

## Example Screenshots
### Home Screen
![Home Screen](link_to_home_screenshot)

### Quiz Question
![Quiz Question](link_to_quiz_screenshot)

### Results
![Results](link_to_results_screenshot)

## Future Enhancements
- Add category selection for questions.
- Expand the question types beyond True/False.
- Include a timer for each question.
- Save user scores and display a leaderboard.

## Acknowledgments
- Open Trivia Database API for providing the trivia questions.
- [Streamlit](https://streamlit.io/) for making interactive app development easy.
