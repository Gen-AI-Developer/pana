import os
from dotenv import load_dotenv
from crewai import LLM , Agent, Crew, Process, Task, knowledge

# Load API key from environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
# Initialize the LLM
llm = LLM(model="gemini/gemini-2.0-flash-exp", api_key=api_key)
# knowledge
k_source = knowledge.TextFileKnowledgeSource(
    file_paths='cro.txt'
)
class MyChatBot:
    def __init__(self):
        self.chat_agent = Agent(
            role="Conversational AI Assistant",
            goal="Have meaningful and contextual conversations with customers",
            backstory=""" You are an AI-powered chatbot designed to assist customers with their
                questions across various topics. Known for being approachable, you engage
                 in conversations with empathy, clarity, and a touch of humor""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
            knowledge_sources=k_source,
            embedder={
                "provider":"google",
                "config":{
                    "model":"models/text-embedding-004",
                    "api_key":api_key
                }
            }
        )
    def create_conversation_task(self,user_input):
        return Task(
            description=f"Respond to the user's query: '{user_input}'",
            agent=self.chat_agent,
            expected_output="A response to the user's query",
        )
    def chat(self,user_input):
        crew = Crew(
            agents=[self.chat_agent],
            tasks=[self.create_conversation_task(user_input)],
            process=Process.hierarchical,
            manager_llm=llm,
            verbose=True,
        )
        result = crew.kickoff()
        return result
def main():
    chatbot = MyChatBot()
    print("\n ChatBot: Hello! I'm your AI assistant. How can I help you today?")

    while True:
        try:
            user_input = input("\nYou: ").strip()
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\nChatBot: Goodbye! Have a great day!")
                break

            if not user_input:
                print("\nChatBot: I didn't catch that. Could you please say something?")
                continue

            response = chatbot.chat(user_input)
            print(f"\nChatBot: {response}")

        except KeyboardInterrupt:
            print("\n\nChatBot: Goodbye! Have a great day!")
            break
        except Exception as e:
            print(
                f"\nChatBot: I encountered an error: {str(e)}. Let's continue our conversation!"
            )
if __name__ == "__main__":
    main()