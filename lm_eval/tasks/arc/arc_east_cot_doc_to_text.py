def doc_to_text(doc):
    question = doc["question"]
    choices = doc["choices"]

    # mc = " ".join([f"({label}) {text}" for label, text in zip(choices['label'], choices['text'])])
    # return f"Given the following problem, reason and give a final answer to the problem.\nProblem: {question} {mc}\nYour response should end with \"The final answer is [answer]\" where [answer] is the response to the problem.\n"

    mc = "\n".join(
        [f"{label}. {text}" for label, text in zip(choices["label"], choices["text"])]
    )
    return f'Given the following problem, reason and give a final answer to the problem.\nProblem: {question}\n{mc}\nYour response should end with "The final answer is [answer]" where [answer] is the response to the problem.\n'
