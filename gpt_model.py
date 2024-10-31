import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with API key
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_study_plan(content, days, hours):
    # System prompt to instruct the model about its task
    system_prompt = """
    You are an AI Agent that helps users generate specific study plans according to the given topic. You respond based on understanding the content. If the user provides specific content like a PDF or document with topics or descriptions, use that content to generate a customized study plan. Otherwise, create a general plan based on the given input.
    """ 

    # Focused user input prompt based on content provided
    input_prompt = (
        f"The user is preparing for the subject '{content}'. "
        f"They have {days} days available for preparation and can dedicate {hours} hours each day. "
        "Based on this information, generate a detailed study plan that includes specific study activities, resource suggestions, and tips for effective learning."
    )
    
    try:
        # Generate response from OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o",  # Replace with your specific model name
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": input_prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        # Return error message if generation fails
        return f"An error occurred while generating the study plan: {str(e)}"
