from generate import generate_response


TEST_CASES = [
    {
        "question": "How long does delivery take?",
        "expected": "3-5 business days"
    },
    {
        "question": "What is your refund policy?",
        "expected": "7 days"
    },
    {
        "question": "Which payment methods do you accept?",
        "expected": "bank transfers and card payments"
    }
]


def evaluate():

    for test in TEST_CASES:

        question = test["question"]
        expected = test["expected"]

        answer = generate_response(question)

        passed = expected.lower() in answer.lower()

        print({
            "question": question,
            "expected": expected,
            "answer": answer,
            "passed": passed
        })


if __name__ == "__main__":
    evaluate()