#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from customer_feedback_analysis_system.crew import CustomerFeedbackAnalysisSystem

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        "reviews" : [
            "The food was delicious, and the staff were incredibly friendly!",
            "Long wait times and the food was cold when it arrived.",
            "Ambiance was nice, but the menu could have more variety."
        ]
    }
    
    try:
        CustomerFeedbackAnalysisSystem().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        CustomerFeedbackAnalysisSystem().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CustomerFeedbackAnalysisSystem().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        CustomerFeedbackAnalysisSystem().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
