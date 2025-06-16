from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
import os
from dotenv import load_dotenv

load_dotenv()
import sys

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ OPENAI_API_KEY não encontrada!")
    sys.exit(1)
else:
    print("✅ OPENAI_API_KEY carregada com sucesso")

# Knowledge sources
pdf_prednisolona = PDFKnowledgeSource(
    file_paths=['Prednisolonaeurofarma.pdf']
)
pdf_imosec = PDFKnowledgeSource(
    file_paths=['Imosec-JanssenCilag.pdf']
)
pdf_ablok = PDFKnowledgeSource(
    file_paths=['Bula-Ablok-Plus-Paciente-Consulta-Remedios.pdf']
)


llm = LLM(
    model="openai/gpt-3.5-turbo",
    temperature=0,
    max_tokens=1500,
)

@CrewBase
class PharmaCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def pharma_expert(self) -> Agent:
        return Agent(
            config=self.agents_config["pharma_expert"],
            goal="Assist with pharmaceutical queries",
            verbose=True,
            tools=[],
            llm=llm,
        )

    @task
    def answer_question(self) -> Task:
        return Task(
            config=self.tasks_config["answer_question"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MQuestKnowledge crew"""

        return Crew(
            agents=[self.pharma_expert()],
            tasks=[
                self.answer_question(),
            ],
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[pdf_ablok, pdf_imosec, pdf_prednisolona],
        )