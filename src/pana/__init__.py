from crewai.flow.flow import Flow,start,listen
from dotenv import load_dotenv,find_dotenv
# from litellm import completion
from pana.crews.blog_crew.BlogCrew import BlogCrew
_: bool = load_dotenv(find_dotenv())


class PanaFlow(Flow):
    

    @start()
    def generate_topic(self) -> str:
        response = BlogCrew().crew().kickoff(
            inputs={
                "input": "Top 25 New Technology Trends in 2025"
            }
        )
        self.state['topic'] = response.raw
        return self.state['topic']
    
    # @listen(generate_topic)
    # def generate_outline(self) -> str:
    #     response = completion(
    #         model="gemini/gemini-1.5-flash",
    #         messages=[
    #             {"role": "user", "content": "Generate a structure outline for a blog post on the topic: "+ self.state['topic']}
    #         ],
    #         temperature=0.3,
    #         )
    #     self.state['outline'] = response.choices[0].message.content
    #     return self.state['outline']
def kickoff():
    flow = PanaFlow()
    flow.kickoff()
    print("Flow Ended")   
def main():
    kickoff()
    