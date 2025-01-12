class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def get_current_question(self):
        return self.question_list[self.question_number]

    def check_answer(self, user_answer):
        """
        Checks if the user's answer is correct.
        
        Args:
            user_answer (str): The user's answer ("True" or "False").
        
        Returns:
            tuple: (is_correct (bool), correct_answer (str))
        """
        current_question = self.get_current_question()
        correct_answer = current_question.answer
        is_correct = user_answer.lower() == correct_answer.lower()
        if is_correct:
            self.score += 1
        self.question_number += 1
        return is_correct, correct_answer
