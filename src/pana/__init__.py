from crewai.flow.flow import Flow, start, listen
from dotenv import load_dotenv, find_dotenv
from litellm import completion

load_dotenv(find_dotenv())

class PanaFlow(Flow):
    
    @start()
    def generate_topic(self):
        print("Generating topic")
        try:
            response = completion(
                model="gemini/gemini-1.5-flash",
                max_tokens=100,
                temperature=0.5,
                messages=[
                    {
                        'role': 'user',  # changed from 'user' to 'role': 'user'
                        'content': 'generate a most sharing/learning topic name in Agentic AI'
                    }
                ]
            )
            topic = response.choices[0].message['content']
            self.state['topic'] = topic  # Store topic in state
            return topic
        except Exception as e:
            print(f"Error generating topic: {str(e)}")
            return None

def main():
    pana_flow = PanaFlow()
    pana_flow.kickoff()

if __name__ == '__main__':
    main()