import os 
from google import genai
from dotenv import load_dotenv
from google.genai.errors import ServerError

load_dotenv()

def test_gemini():

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    response = client.models.generate_content(
        model="models/gemini-3.5-flash",
        contents="Say Hello from Gemini"
    )
    return response.text

def review_code(language,code):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    if language.lower() == "python":
        try:
            compile(code, "<string>", "exec")
            syntax_result = "No syntax errors found."
        except SyntaxError as e:
            syntax_result = f"SyntaxError: {e}"
    else:
        syntax_result = "Syntax check not available."

    prompt = f"""
    You are an expert software engineer.

    A syntax check has already been performed by Python itself.

    Syntax Check:
    {syntax_result}

    Never contradict the syntax check above.

    If the syntax check says "No syntax errors found", do NOT mention any syntax or indentation errors.

    Review only:
    - code quality
    - logic
    - readability
    - performance
    - best practices

    Respond exactly in this format.

    Summary:
    (2-3 lines)

    Syntax Check:
    - {syntax_result}

    Errors:
    - Only mention actual logical/runtime errors.
    - If none:
    - No errors found.

    Improvements:
    - Bullet points only.

    Best Practices:
    - Bullet points only.

    Code:
    ```{language}
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
