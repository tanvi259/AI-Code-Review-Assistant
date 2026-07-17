import os 
from google import genai
from dotenv import load_dotenv
from google.genai.errors import ServerError

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def test_gemini():

    response = client.models.generate_content(
        model="models/gemini-3.5-flash",
        contents="Say Hello from Gemini"
    )
    return response.text

def review_code(language,code):
    prompt = f"""
    You are an expert software engineer.

    Review the following {language} code.

    Respond in this exact format.

    Summary:
    (2-3 lines)

    Errors:
    - Bullet points only.
    - If there are no errors, write:
    - No errors found.

    Improvements:
    - Bullet points only.

    Best Practices:
    - Bullet points only.

    Keep the response concise and beginner friendly.

    Code:
    {code}
    """

    try:
        response = client.models.generate_content(
            model="models/gemini-3.5-flash",
            contents=prompt 
        )

        return response.text
    
    except ServerError:
        return "Gemini service is temporarily unavailable. Please try again later."

    except Exception:
        return "Unable to generate AI review."
