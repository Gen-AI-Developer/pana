from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
import os
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
api_key = os.getenv('GEMINI_API_KEY')
# Create a knowledge source
# content = """
# - AI for Medical 
# - AI for Crimal justice
# - AI for Data Ananlysis
# - AI for Geo Engineering
# - AI for Robotics
# - AI for Cyber Security
# - AI for Image Processing
# - AI for Natural Language Processing
# - AI for Speech Recognition
# - AI for Autonomous Vehicles
# - AI for Game Development
# - AI for Music Composition
# - AI for Art
# - AI for Fashion
# - AI for Sports
# - AI for Agriculture
# - AI for E-Commerce
# - AI for Health Care
# - AI for Education
# - AI for Finance
# - AI for Social Media
# - AI for Marketing
# - AI for Human Resources
# - AI for Customer Service
# - AI for Supply Chain Management
# - AI for Logistics
# - AI for Manufacturing
# - AI for Construction
# - AI for Energy
# - AI for Environment
# - AI for Space Exploration
# """
# string_source = StringKnowledgeSource(
#     content=content,
# )

text_knowledge = TextFileKnowledgeSource(
    file_paths='knowledge.txt'
)
pdf_knowledge = PDFKnowledgeSource(
    file_paths='knowledge.pdf'
)

@CrewBase
class BlogCrew:
    # text_file_knowledge_source = TextFileKnowledgeSource(file_path=['knowledge.txt'])
    """ Blog Crew for generating blog topics """
    #agents and tasks configs
    agents_config= 'config/agents.yaml'
    tasks_config= 'config/tasks.yaml'    
    #1. Define the agents
    @agent
    def topic_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['topic_generator'],
            llm='gemini/gemini-1.5-flash',
            
        ) 
    #2. Define the tasks
    @task
    def generate_topic(self) -> Task:
        return Task(
            config=self.tasks_config['generate_topic'],
        )
    #3. Define the crew
    @crew
    def crew(self) -> Crew:
        """ Creates the Blog Crew """
        #2. Define the tasks
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[pdf_knowledge], # Enable knowledge by adding the sources here. You can also add more sources to the sources list.
            embedder={
                "provider":"google",
                "config":{
                    "model":"models/text-embedding-004",
                    "api_key":api_key
                }
            }
            # knowledge=self.text_file_knowledge_source
        )
