def doc_to_text(doc):
    question = doc["question"]
    
    if "body" in doc:
        body = doc["body"]
        return f"Given the following problem, reason and give a final answer to the problem.\nProblem: {body} {question}\nYour response should end with \"The final answer is [answer]\" where [answer] is the response to the problem.\n"
    return f"Given the following problem, reason and give a final answer to the problem.\nProblem: {question}\nYour response should end with \"The final answer is [answer]\" where [answer] is the response to the problem.\n"
