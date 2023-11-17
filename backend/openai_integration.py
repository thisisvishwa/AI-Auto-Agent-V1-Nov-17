```python
import openai

# Initialize OpenAI GPT model
openai_model = openai.GPT3Model()

def process_query(query):
    """
    Function to process complex queries using OpenAI.
    """
    try:
        response = openai_model.complete(query)
        return response
    except Exception as e:
        print(f"Error in processing query: {e}")
        return None

def openai_response(query):
    """
    Function to handle responses from OpenAI.
    """
    response = process_query(query)
    if response:
        return response.choices[0].text.strip()
    else:
        return "Unable to process query at the moment."

if __name__ == "__main__":
    query = "Translate the following English text to French: 'Hello, how are you?'"
    print(openai_response(query))
```