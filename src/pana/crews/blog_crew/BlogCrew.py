from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew

@CrewBase
class BlogCrew:
    """ Blog Crew for generating blog topics """
    #agents and tasks configs
    agents_config= 'config/agents.yaml'
    tasks_config= 'config/tasks.yaml'    
    #1. Define the agents
    @agent
    def topic_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['topic_generator'],
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
        )
