# GenQuiz – AI Quiz Generator

GenQuiz is a Generative AI-based quiz generator web application that automatically creates multiple-choice quizzes based on a user-provided topic. The application uses AI models to generate questions dynamically and allows users to attempt the quiz interactively.

## Features

* Generate quiz questions using AI
* Select topic, difficulty level, and number of questions
* Multiple-choice questions interface
* Next question navigation
* Automatic score calculation
* Simple and clean user interface

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* OpenRouter API (AI model)

## How It Works

1. User enters a quiz topic.
2. User selects difficulty and number of questions.
3. The system sends the request to an AI model.
4. The AI generates quiz questions.
5. Questions are displayed one by one.
6. User selects answers and submits.
7. Final score is displayed.

## Project Structure

GenQuiz
│
├── app.py
├── templates
│   └── index.html
└── README.md

## How to Run

1. Install requirements:
   pip install flask requests

2. Run the application:
   python app.py

3. Open browser:
   http://127.0.0.1:5000

## Future Improvements

* Timer for each question
* Progress bar
* User login system
* Quiz history
* Leaderboard

## Author

GenQuiz Project – BTech Generative AI Mini Project
