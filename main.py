import asyncio
import os
from dotenv import load_dotenv

from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI, HarmCategory, HarmBlockThreshold
from pydantic import ConfigDict

class GeminiPermissivo(ChatGoogleGenerativeAI):
    provider: str = "google"
    model_config = ConfigDict(extra="allow")
    
    @property
    def model_name(self):
        return self.model

load_dotenv()

async def main():
    # 1. Usando a versão 2.0-flash (mais estável para formato JSON nesta biblioteca)
    # 2. Mantendo a temperatura em 0.0
    # 3. REATIVANDO os filtros de segurança para que as notícias não sejam bloqueadas
    llm = GeminiPermissivo(
        model="gemini-2.0-flash", 
        api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.0,
        safety_settings={
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        }
    )

    agent = Agent(
        task="open google and search for the latest news about brasil'",
        llm=llm,
    )
    
    print("Iniciando o agente com Gemini 2.0 Flash...")
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())