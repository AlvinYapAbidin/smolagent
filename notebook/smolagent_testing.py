from smolagents import TransformersModel, CodeAgent
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

#model = InferenceClientModel(model_id="meta-llama/Llama-2-70b-chat-hf")
# model = LiteLLMModel(model_id="groq/llama-3.1-8b-instant")
model = TransformersModel(model_id="meta-llama/Llama-2-7b-chat-hf")


agent = CodeAgent(tools=[], model=model,add_base_tools=True)

result = agent.run("How many bones in the human body")
print(result)