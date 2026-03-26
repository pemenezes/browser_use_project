import asyncio
import os
from browser_use import Agent, Browser
from langchain_google_genai import ChatGoogleGenerativeAI

async def main():
    # Passamos a chave diretamente aqui para evitar erros de leitura de arquivo .env
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key="AIzaSyCASjiKrGSOWKykTlfoOOPkREj-1lZ2smo"  # <--- Cole sua chave aqui entre as aspas
    )
    
    # Adicionamos o "crachá" que o browser-use exige
    llm.provider = "google" 

    # Criamos o browser com 'headless': False para você ver ele funcionando!
    browser = Browser(config={'headless': False})

    agent = Agent(
        task="Vá ao site do Google, pesquise por 'preço do Bitcoin hoje' e me diga o valor",
        llm=llm,
        browser=browser,
    )
    
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())