# demo.py

import llms

def main():
    # Using the OpenAI LLM.
    openai_client = llms.get_llm("openai", api_key="YOUR_OPENAI_API_KEY")
    print(openai_client.query("Hello, how are you?"))
    
    # Using the Gemini LLM.
    gemini_client = llms.get_llm("gemini", api_key="YOUR_GEMINI_API_KEY")
    print(gemini_client.query("Tell me a joke."))

if __name__ == "__main__":
    main()
