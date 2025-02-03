import os
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from .env
load_dotenv(".env.local")

# Initialize Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def generate_gemini_response(prompt: str) -> str:
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = await model.generate_content_async(prompt)
        
        # Handle the response structure properly
        print("response*********",response)
        print("reponse.candidates **************",response.candidates)
        if response and response.candidates:
            # Get text from first candidate's content parts
            parts = response.candidates[0].content.parts
            return "".join(part.text for part in parts if hasattr(part, 'text'))
            
        return "No response generated"
    
    except IndexError:
        print("Error: No candidates in response")
        return "Response format error"
    
    except AttributeError as ae:
        print(f"Attribute error: {str(ae)}")
        return "Unexpected response format"
    
    except Exception as e:
        print(f"Gemini API error: {str(e)}")
        return "Sorry, I couldn't process that request"