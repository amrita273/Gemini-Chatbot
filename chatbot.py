import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def main():
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: Please set the GEMINI_API_KEY environment variable.")
        return
    

    client=genai.Client()


    chat=client.chats.create(model="gemini-3.5-flash")
    print("🤖 Gemini Terminal Chatbot")
    print("Type your question below. Type 'quit' or 'exit' to stop.")
    print("-" * 50)

    while True:
        try:
            user_input = input("\nYou: ")

            if user_input.strip().lower() in ['quit', 'exit']:
                print("Goodbye!")
                break

            if not user_input.strip():
                continue

            response = chat.send_message(user_input)
            print(f"\nGemini: {response.text}")


        except KeyboardInterrupt:
            
            print("\nGoodbye!")
            break
        except Exception as e:
           
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()

