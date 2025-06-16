from crew import PharmaCrew
import os
from dotenv import load_dotenv

load_dotenv()


def run_pharma_assistant(question: str):
    """
    Runs the MedicamentAI Assistant with the given question.

    Args:
        question (str): The medicament question to be answered.

    Returns:
        str: The response from the AI pharma agent.
    """
    if not question.strip():
        return "⚠️ Please enter a valid question."

    # Initialize the PharmaCrew
    crew_instance = PharmaCrew()

    # Run the AI Pharma Assistant
    result = crew_instance.crew().kickoff(inputs={"question": question})

    return result