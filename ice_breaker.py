import os
from os import scandir

from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

def ice_breaker_with(name: str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    summary_template = """
        Given the information {information} about a person from I want you to create:
        1. a short summary
        2. Two interesting facts about him
        3. Two dangerous things about him
    """

    summary_promt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_promt_template | llm

    res = chain.invoke(input={"information": linkedin_data})

    print(res)

if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Enter")
    ice_breaker_with(name="Eden Marco Udemy")
