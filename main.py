from itertools import chain
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch

# from tavily import TavilyClient

# tavily = TavilyClient()


load_dotenv(override=True)

# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches over internet
#     Args:
#         query: The query to search for
#     Returns:
#         The search result
#     """
#     print(f"Searching for {query}...")
#     return tavily.search(query=query)

llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)



def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="Search for 3 job postings for an ai engineer using langchain in malaysia on linkedin and list their details")]})
    print(result)

    # information = """
    # Elon Reeve Musk (/ˈiːlɒn/ ⓘ; born June 28, 1971) is an industrialist, futurist, and former United States public official. He is the chief executive officer and largest shareholder of Tesla and SpaceX. Musk has been the wealthiest person in the world since 2025, and became the only trillionaire in history (in terms of US dollars) in 2026; as of November 2026, Forbes estimates his net worth to be $849.7 billion.
    # Musk was born into the wealthy Musk family in Pretoria, South Africa. He emigrated to Canada in 1989; he has Canadian citizenship as his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California, United States, to pursue business ventures. In 1995, he co-founded Zip2, a web software company. Following its sale in 1999, he co-founded X.com, an e-commerce payment system that merged with Confinity in March 2000 to form PayPal. Musk also became an American citizen in 2002.
    # """

    # summary_template = """
    # Given the following information about Elon Musk:
    # {information}
    # 1. A short summary
    # 2. two interesting facts about Elon Musk
    # """

    # summary_prompt_template = PromptTemplate(
    #     input_variables=["information"],
    #     template=summary_template,
    # )

    # llm = ChatOpenAI(temperature=0, model="gpt-5")

    # chain = summary_prompt_template | llm
    # response = chain.invoke(input={"information":information})   

    # print(f"llm: {response.content}")




if __name__ == "__main__":
    main()
