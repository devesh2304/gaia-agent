import os
from dotenv import load_dotenv
from datasets import load_dataset
from agent.runner import run_task
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

load_dotenv()

console = Console()

def run_eval(num_questions: int = 5):
    """Run agent against GAIA benchmark questions and score it."""
    
    console.print(Panel("[bold]GAIA Benchmark Eval[/bold]\nLoading dataset...", style="cyan"))

    # load GAIA validation set
    dataset = load_dataset(
    "gaia-benchmark/GAIA",
    "2023_all",
    split="validation",
    token=os.getenv("HF_TOKEN")
    )

    # filter to level 1 only (easiest) — good for CPU-only machines
    level1 = [q for q in dataset if str(q["Level"]) == "1"]
    questions = level1[:num_questions]

    console.print(f"[dim]Running {num_questions} Level-1 questions...[/dim]\n")

    results = []
    correct = 0

    for i, item in enumerate(questions):
        question = item["Question"]
        expected = str(item["Final answer"]).strip().lower()

        console.print(f"[bold cyan]Q{i+1}:[/bold cyan] {question}")

        with console.status("Agent thinking..."):
            answer = run_task(question)

        predicted = answer.strip().lower()
        is_correct = expected in predicted or predicted in expected

        if is_correct:
            correct += 1
            status = "[bold green]✓ Correct[/bold green]"
        else:
            status = "[bold red]✗ Wrong[/bold red]"

        console.print(f"[dim]Expected:[/dim] {expected}")
        console.print(f"[dim]Got:[/dim] {predicted[:200]}")
        console.print(status)
        console.print()

        results.append({
            "question": question,
            "expected": expected,
            "predicted": predicted,
            "correct": is_correct
        })

    # summary table
    table = Table(title="Eval Results")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("Questions run", str(num_questions))
    table.add_row("Correct", str(correct))
    table.add_row("Score", f"{correct/num_questions:.0%}")

    console.print(table)

if __name__ == "__main__":
    run_eval(num_questions=15)