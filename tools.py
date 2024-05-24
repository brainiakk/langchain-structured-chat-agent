import os
import time
from langchain_openai import ChatOpenAI
from langchain.tools import BaseTool
from langchain.pydantic_v1 import BaseModel, Field
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from typing import Optional
import json
from langchain.tools import SteamshipImageGenerationTool
from langchain.schema import HumanMessage, SystemMessage
import numpy as np
from PIL import Image
import base64
from typing import Optional, Type
from langchain.llms import Ollama
from langchain_google_vertexai import ChatVertexAI
from PIL import ImageGrab
from langchain_openai import ChatOpenAI
import cv2
from voice import VoiceService

vs = VoiceService()
# vs.piper('hello')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google-credentials.json"

llm = ChatVertexAI(model_name="gemini-1.5-pro-preview-0514", temperature=0)

def analyze_image(image: str, query: str):
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": query,
            },
            {
                "type": "image_url",
                "image_url": {"url": image}
            }
        ]
    )
    
    response = llm.invoke([message])
    
    return response.content
    
    

class VisionInput(BaseModel):
    query: str = Field(..., description="use this as the query: 'give a detailed description of this image, as detailed as possible.'")
    wait_message: str = Field(..., description="address the user politely and ask the user to hold on while you access the webcam")

class VisionTool(BaseTool):
    name="Vision Tool"
    description="Useful tool to take a snapshot. Use this tool to access the user's webcam. USE this tool when asked to 'take a look' at something and no context was provided. Format input as: {{ \"query\": \"...\", \"wait_message\": \"...\" }}."
    args_schema: Type[BaseModel] = VisionInput
    # return_direct=True
    
    
    def _run(self, query: str, wait_message: str, run_manager: Optional[CallbackManagerForToolRun]):
        print(wait_message)
        # vs.piper(str(wait_message))
        image_path = self.capture()
        
        analyze = analyze_image(image_path, query)
        return analyze
    
    async def _arun(self, query: str, wait_message: str, run_manager: Optional[AsyncCallbackManagerForToolRun]):
        return await self._run(query, wait_message, run_manager)
    
    def capture(self):
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            raise IOError("Camera failed to open")
        
        print("Camera opened successfully")
        time.sleep(1)
        
        ret, frame = cap.read()
        
        if not ret:
            raise IOError("Failed to grab frame")
        else:
            img_path = os.path.join("images", "snapshot.jpg")
            cv2.imwrite(img_path, frame)
            print(f"Image saved successfully to: {img_path}")
            
        cap.release()
        print("Camera closed successfully")
        return img_path

class ScreenshotInput(BaseModel):
    query: str = Field(..., description="use this as the query: 'give a detailed description of this image, as detailed as possible.'")
    wait_message: str = Field(..., description="address the user politely and ask the user to hold on while you take a screenshot of the active window.")
    
    
class ScreenshotTool(BaseTool):
    name="Screenshot Tool"
    description="Useful tool to take a screenshot. ONLY use this tool when asked to look at the SCREEN.  Use this tool to screenshot the user's screen. Use this tool if asked to look at the user's screen. Format input as: {{ \"query\": \"...\", \"wait_message\": \"...\" }}."
    args_schema: Type[BaseModel] = ScreenshotInput
    # return_direct=True
    
    
    def _run(self, query: str, wait_message: str, run_manager: Optional[CallbackManagerForToolRun]):
        print(wait_message)
        # vs.piper(str(wait_message))
        image_path = self.capture()
        
        analyze = analyze_image(image_path, query)
        return analyze
        
    async def _arun(self, query: str, wait_message: str, run_manager: Optional[CallbackManagerForToolRun]):
        return await self._run(query, wait_message, run_manager)
    
    def capture(self):
        screenshot = ImageGrab.grab()
        img_path = os.path.join("images", "screenshot.png")
        screenshot.save(img_path)
        
        return img_path