from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class CustomerFeedbackAnalysisSystem():
    """CustomerFeedbackAnalysisSystem crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], 
            verbose=False
        )

    @agent
    def sentiment_classifier(self) -> Agent:
        return Agent(
            config=self.agents_config['sentiment_classifier'], 
            verbose=False
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=False
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agents=[self.researcher()],
            output_file='reports/research_report.md',
            verbose=False
        )

    @task
    def sentiment_task(self) -> Task:
        return Task(
            config=self.tasks_config['sentiment_task'],
            agents=[self.sentiment_classifier()],
            output_file='reports/sentiment_report.md',
            verbose=False
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            agents=[self.reporting_analyst()],
            output_file='reports/feedback_analysis_report.md',
            verbose=False
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )