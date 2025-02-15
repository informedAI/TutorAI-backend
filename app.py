from flask import Flask, request, jsonify
from dotenv import load_dotenv
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs import AIMLConfig
from camel.agents import ChatAgent
from camel.societies.workforce import Workforce
from camel.tasks import Task

# Load environment variables from .env file
load_dotenv()


app = Flask(__name__)

model = ModelFactory.create(
    model_platform=ModelPlatformType.AIML,
    model_type=ModelType.DEEPSEEK_CHAT,
    model_config_dict=AIMLConfig().as_dict(),
)

# Initialize the agents
planner_agent = ChatAgent(
    "You are a curriculum planner specialising in effective study plans", model=model
)
time_manager_agent = ChatAgent("You are a time management advisor", model=model)
professor_agent = ChatAgent("You are a professor", model=model)

# Create a workforce instance
workforce = Workforce(
    "A Simple Workforce focused on education",
    coordinator_agent_kwargs={"model": model},
    task_agent_kwargs={"model": model},
    new_worker_agent_kwargs={"model": model},
)

workforce.add_single_agent_worker(
    "A curriculum planner specialising in effective study plans",
    worker=planner_agent,
).add_single_agent_worker(
    "A time management advisor",
    worker=time_manager_agent,
).add_single_agent_worker(
    "A professor agent",
    worker=professor_agent,
)

task = Task(
    content="Make a study plan for calculus 1",
    id="0",
)
task = workforce.process_task(task)
print(task)


@app.route("/")
def home():
    # response = agent.step("Hello, can you help me?")
    # return response.msgs[0].content
    # task = Task(
    #     content="Make a study plan for calculus 1",
    #     id="0",
    # )
    # task = workforce.process_task(task)
    # print(task)
    return "???"


if __name__ == "__main__":
    app.run(debug=True)
