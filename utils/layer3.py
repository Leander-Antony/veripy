from utils import layer1
from utils import layer2
import ollama

def extract_confidence_score(text):
    import re
    match = re.search(r'Confidence score: (\d+)', text)
    return int(match.group(1)) if match else None

def extract_verdict_only(text):
    import re
    match = re.search(r"🧠 Verdict:\n(.*?)(?:\n|$)", text, re.DOTALL)
    return match.group(1).strip() if match else text

def get_combined_summary_with_ollama(statement, label, short_verdict):
    prompt = f"""Generate a clear, concise fact-checking report in under 100 words using the following information:

- Claim: "{statement}"
- Label predicted by the ML model: {label}
- Fact-checking verdict: "{short_verdict}"

Start with: "According to the ML model and verified context..." and summarize both insights neatly.
"""

    response = ollama.chat(
        model='llama3',  # or 'mistral', 'gemma', etc.
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content'].strip()

def generate_combined_report(statement):
    # Layer 1: Label prediction
    label = layer1.predict_label(statement)

    # Layer 2: Fact-checking
    verdict, sources = layer2.fact_check(statement)
    confidence = extract_confidence_score(verdict)
    short_verdict = extract_verdict_only(verdict)

    # Use Ollama to combine insights into a natural language report
    combined_summary = get_combined_summary_with_ollama(statement, label, short_verdict)

    # Final report
    report = f"""
📌 Combined Fact-Check Report

🧠 Summary:
{combined_summary}


"""

    return {
        "score": confidence,
        "links": sources,
        "report": report.strip()
    }

# if __name__ == "__main__":
#     user_input = input("Enter a claim or statement: ")
#     result = generate_combined_report(user_input)

#     print("\n✅ Final Score:", result["score"])
#     print("\n🔗 Links:")
#     for link in result["links"]:
#         print("-", link)

#     print("\n📝 Full Report:\n")
#     print(result["report"])
