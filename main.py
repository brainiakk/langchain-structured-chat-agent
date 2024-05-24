from langchain_google_vertexai import ChatVertexAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import create_structured_chat_agent, AgentExecutor
from langchain import hub
import os

from tools import VisionTool, ScreenshotTool
from voice import VoiceService
from langchain.schema import HumanMessage, SystemMessage

vs = VoiceService()

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google-credentials.json"

llm = ChatVertexAI(model_name="gemini-1.5-pro-preview-0514", temperature=0)

# memory = ConversationBufferMemory(
#     memory_key="chat_history",
#     return_messages=True
# )
tools = [VisionTool(), ScreenshotTool()]

prompt = hub.pull("hwchase17/structured-chat-agent")
agent = create_structured_chat_agent(llm, tools, prompt)

agent_exec = AgentExecutor(agent=agent, handle_parsing_errors="Check your output and make sure it conforms, use the Action/Action Input syntax, if it doesn't call a tool, output only the action_input.",  tools=tools, return_intermediate_steps=True, verbose=True)

while True:
    query = input("Enter your query >>> ")
    response = agent_exec.invoke({"input": query})
    print(response["output"])
    # vs.piper(str(response["output"]))