import os
from dotenv import load_dotenv
from openai import OpenAI
import reflex as rx

# Load env
load_dotenv()

# OpenAI client
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Grok client (optional)
grok_client = None
if os.getenv("XAI_API_KEY"):
    grok_client = OpenAI(
        api_key=os.getenv("XAI_API_KEY"),
        base_url="https://api.x.ai/v1"
    )


class State(rx.State):
    # -------- STATE VARIABLES --------
    code: str = ""
    selected_ai: str = "openai"  # IMPORTANT: matches UI
    result: str = ""
    optimized_code: str = ""

    # -------- ANALYZE FUNCTION --------
    def analyze_code(self):
        try:
            if not self.code.strip():
                self.result = "⚠️ Please enter code"
                return

            prompt = f"""
You are a professional code reviewer.

Analyze this code:
{self.code}

Give:
1. Errors
2. Improvements
3. Optimized code
"""

            output = ""

            # -------- GROK --------
            if self.selected_ai == "grok" and grok_client:
                try:
                    response = grok_client.chat.completions.create(
                        model="grok-1.5",
                        messages=[
                            {"role": "user", "content": prompt}
                        ]
                    )
                    output = response.choices[0].message.content
                except Exception as e:
                    output = f"⚠️ Grok failed → switching to OpenAI\n{str(e)}"

            # -------- OPENAI (fallback) --------
            if not output or "failed" in output.lower():
                response = openai_client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                output = response.choices[0].message.content

            self.result = output
            self.optimized_code = output

        except Exception as e:
            self.result = f"❌ Error: {str(e)}"