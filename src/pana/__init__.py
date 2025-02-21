from crewai.flow.flow import Flow, start , listen
from dotenv import load_dotenv,find_dotenv
from litellm import completion


load_dotenv(find_dotenv())


class PanaFlow(Flow):
    
    @start
    def generate_topic(self):
        print("Generating topic")
        self.state['topic'] = completion(
            model="gemini/gemini-1.5-flash",
            max_tokens=100,
            temperature=0.5,
            messages=[
                {
                    'user': 'user',
                    'content': 'generate a trending topic name for me please'
                }
            ]
        )