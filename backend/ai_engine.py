# ai_engine.py
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables (safe to call multiple times)
load_dotenv()

def get_openai_client():
    """Return an OpenAI client instance safely."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")
    return OpenAI(api_key=api_key)

def analyze_requirement_text(text: str):
    """
    Sends the requirement text to OpenAI for analysis and returns structured insights.
    """
    client = get_openai_client()

    prompt = f"""
    You are an experienced software business analyst.
    Analyze the following business requirement text and identify:
    1. Missing details or ambiguities
    2. Possible validations or constraints
    3. Limitations or assumptions
    4. Non-functional requirements (e.g., performance, scalability, security)

    Requirement:
    {text}

    Respond in valid JSON format with the following keys:
    missing_details, validations, limitations, nfr
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a precise and structured requirement analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )

        content = response.choices[0].message.content.strip()

        try:
            return eval(content)
        except Exception:
            return {"raw_output": content}

    except Exception as e:
        return {"error": str(e)}
