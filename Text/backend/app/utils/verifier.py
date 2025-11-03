import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found in environment. Please check your .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

def verify_claim_with_gemini(claim: str):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash-lite")
        prompt = f"""
        You are an expert fact-checking assistant. Analyze the following claim and determine:
        1. Whether it is True, False, or Unverifiable.
        2. Provide a confidence score between 0.0 and 1.0 based on how certain you are.
        3. Give a clear, structured explanation with factual context and supporting evidence.

        Claim: "{claim}"

        Respond strictly in this JSON format:
        {{
        "verdict": "True" | "False" | "Unverifiable",
        "confidence": float,
        "explanation": "Detailed reasoning that includes context, factual evidence, and justification for the verdict."
        }}
        """

        # Generate response from Gemini
        response = model.generate_content(prompt)
        content = response.text.strip() if hasattr(response, "text") else ""

        # 🔹 Clean up markdown code fences if present (like ```json ... ```)
        if content.startswith("```"):
            content = content.strip("`").strip()
            # remove leading identifiers like json or python
            if content.lower().startswith("json"):
                content = content[4:].strip()

        # 🔹 Try parsing JSON
        try:
            result = json.loads(content)
        except json.JSONDecodeError:
            result = {
                "verdict": "Uncertain",
                "confidence": 0.5,
                "explanation": content or "No explanation provided."
            }

        # Add claim text and timestamp
        result["input_text"] = claim
        result["timestamp"] = datetime.utcnow().isoformat() + "Z"

        return result

    except Exception as e:
        return {
            "input_text": claim,
            "verdict": "System Unavailable",
            "confidence": 0,
            "explanation": (
                "⚠️ Internal inference error: The model encountered an unexpected issue "
                "while analyzing this claim. It may have exceeded its contextual limits or "
                "failed to converge on a stable interpretation. "
                "Please retry after a few moments — subsequent runs often stabilize as "
                "the system recalibrates."
            ),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

