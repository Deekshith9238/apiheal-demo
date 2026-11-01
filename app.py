"""Representative migration fixture; no provider call runs at import time."""

from openai import OpenAI as _apiheal_OpenAI


def answer(model, messages):
    """Extract the first chat response's text."""
    with _apiheal_OpenAI() as _apiheal_client:
        response = _apiheal_client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message.content
