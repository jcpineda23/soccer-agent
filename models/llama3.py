import subprocess

def call_llama(prompt: str) -> str:
    """
    Calls LLaMA 3 locally via Ollama and returns the raw output.
    """
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()