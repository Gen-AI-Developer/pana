from crewai.flow.flow import Flow,start,listen
from dotenv import load_dotenv,find_dotenv
from litellm import completion
_: bool = load_dotenv(find_dotenv())

class PanaFlow(Flow):

    @start()
    def generate_topic(self) -> str:
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {"role": "user", "content": "share most trending in AI world  just give me a single topic title."}
            ],
            temperature=0.7,
            max_tokens=100,
            )
        self.state['topic'] = response.choices[0].message.content
        print(f"Selected Topic for Blog Post is :-> {self.state['topic']}")
        return self.state['topic']
    
    @listen(generate_topic)
    def generate_outline(self) -> str:
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {"role": "user", "content": "Generate a structure outline for a blog post on the topic: "+ self.state['topic']}
            ],
            temperature=0.3,
            )
        self.state['outline'] = response.choices[0].message.content
        return self.state['outline']
    
def main():
    flow = PanaFlow()
    print(flow.kickoff())
    print("Flow Ended")