from flask import Flask, request, jsonify
from dotenv import load_dotenv
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs import AIMLConfig
from camel.agents import ChatAgent

# Load environment variables from .env file
load_dotenv()


app = Flask(__name__)

model = ModelFactory.create(
    model_platform=ModelPlatformType.AIML,
    model_type=ModelType.DEEPSEEK_CHAT,
    model_config_dict=AIMLConfig().as_dict(),
)

# Define an assitant message
system_msg = "You are a helpful assistant."

# Initialize the agent
agent = ChatAgent(system_msg, model=model)


@app.route("/")
def home():
    response = agent.step("Hello, can you help me?")
    print(response.msgs)
    return response.msgs[0].content


if __name__ == "__main__":
    app.run(debug=True)
