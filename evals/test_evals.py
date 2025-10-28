import sys
from evaluate import evaluate_generated_answer  # A


def run_RAG(user_question):  # B
    return "IDKLOL"

eval_questions = [
    "What is Underwhelming Spatula?",  # A
    "Who wrote 'Dubious Parenting Tips'?",  # A
    "How long is Almost-Perfect Investment Guide?",  # A
]

eval_answers = [
    "Underwhelming Spatula is a kitchen tool that redefines expectations by fusing whimsy with functionality.",  # A
    "Lisa Melton wrote Dubious Parenting Tips.",  # A
    "The Almost-Perfect Investment Guide is 210 pages long.",  # A
]

def test_run_RAG():
    generated_answers = []
    for question in eval_questions:
        answer = run_RAG(question)
        generated_answers.append(answer)  # D
    for i in range(len(eval_questions)):  # E
        # Используем sys.stderr для гарантированного вывода
        sys.stderr.write(f"\n{'='*60}\n")
        sys.stderr.write(f"Question {i+1}: {eval_questions[i]}\n")
        sys.stderr.write(f"Expected answer: {eval_answers[i]}\n")
        sys.stderr.write(f"Given answer: {generated_answers[i]}\n")
        sys.stderr.flush()
        
        result = evaluate_generated_answer(
            eval_answers[i], generated_answers[i]
        )
        
        sys.stderr.write(f"\n--- Evaluation Result ---\n")
        sys.stderr.write(f"Result type: {type(result)}\n")
        sys.stderr.write(f"Result value: {result}\n")
        sys.stderr.write(f"Result contains 'PASS': {'PASS' in str(result)}\n")
        sys.stderr.write(f"{'='*60}\n\n")
        sys.stderr.flush()
        
        # Также используем обычный print с flush
        print(f"\n{'='*60}", flush=True)
        print(f"Question {i+1}: {eval_questions[i]}", flush=True)
        print(f"Expected answer: {eval_answers[i]}", flush=True)
        print(f"Given answer: {generated_answers[i]}", flush=True)
        print(f"\n--- Evaluation Result ---", flush=True)
        print(f"Result type: {type(result)}", flush=True)
        print(f"Result value: {result}", flush=True)
        print(f"Result contains 'PASS': {'PASS' in str(result)}", flush=True)
        print(f"{'='*60}\n", flush=True)
        
        # Раскомментируйте, когда будете готовы проверять результат:
        assert "PASS" in str(result), f"Expected PASS in result, got: {result}"