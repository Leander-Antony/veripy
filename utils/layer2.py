from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from duckduckgo_search import DDGS
from googlesearch import search

llm = Ollama(model="llama3")

template = """
You are a fact-checking assistant.

Claim:
{claim}

Search Context:
{context}

Using the above information, determine whether the claim is likely true or false.
Give a short explanation and a confidence score out of 100 for being true.
"""

prompt = PromptTemplate(input_variables=["claim", "context"], template=template)
chain = LLMChain(llm=llm, prompt=prompt)

def duckduckgo_search(query, max_results=5):
    results = DDGS().text(query, max_results=max_results)
    return [(r.get("body", ""), r.get("href", "")) for r in results if r.get("body")]

def google_search(query, max_results=5):
    urls = search(query, num_results=max_results)
    return [(None, url) for url in urls]

def get_search_context_and_links(query, max_results=5):
    all_results = []

    try:
        all_results.extend(duckduckgo_search(query, max_results))
    except Exception as e:
        print("DuckDuckGo error:", e)
    
    try:
        all_results.extend(google_search(query, max_results))
    except Exception as e:
        print("Google error:", e)

    context = [body for body, url in all_results if body] 
    links = [url for _, url in all_results if url]

    return "\n\n".join(context), links

def fact_check(claim):
    context, sources = get_search_context_and_links(claim)
    if not context:
        return "No search results found. Unable to verify the claim.", []
    
    result = chain.run({"claim": claim, "context": context})
    return result, sources

if __name__ == "__main__":
    claim_input = "srp trp sindhanai hackathon cancelled"
    verdict, source_links = fact_check(claim_input)

    print("🧠 Verdict:\n", verdict)
    print("\n🔗 Sources:")
    for link in source_links:
        print("-", link)
