import openai
import os
import lmstudio as lms
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def send_to_openai(message):
    openai.api_key = os.environ.get("OPENAI_API_KEY")  
    completion = openai.chat.completions.create(
        model="gpt-4o",  # B
        messages=[{"role": "user", "content": message}],  
    )
    return completion.choices[0].message.content.strip()  

def send_to_lms(message):
    model = lms.llm("qwen/qwen3-4b-2507")
    result = model.respond(message)
    return result

def evaluate_generated_answer(expected_answer, generated_answer):  
    prompt = (
        f"Please evaluate the generated answer. If the generated answer provides the same information "
        f"as the expected answer, then return PASS. Otherwise, return FAIL. "
        f"Expected answer: {expected_answer} Generated answer: {generated_answer}"
    )
    model_type="lms"

    if model_type == "openai":
        response = send_to_openai(prompt)  # C
    elif model_type == "lms" or model_type == "qwen":
        response = send_to_lms(prompt)  # C
    else:
        raise ValueError(f"Unknown model_type: {model_type}. Use 'openai' or 'lms'/'qwen'")
    return response  # D
