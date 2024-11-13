from openai import OpenAI
from dotenv import load_dotenv

def get_products(image):
    load_dotenv()

    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "write a haiku about ai"}
        ]
    )

    return ["products"]