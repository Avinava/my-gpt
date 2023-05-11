from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer
from dotenv import load_dotenv
import os
import time


from rich.console import Console
from rich.prompt import Prompt
# load environment variables
load_dotenv()

revision = os.getenv("MODEL_REVISION") or "v1.3-groovy"
model_name = os.getenv("MODEL_NAME") or "nomic-ai/gpt4all-j"

model = AutoModelForCausalLM.from_pretrained(model_name, revision=revision, device_map='auto') 


# get response from model
def get_response(input_text):
    tokenizer = AutoTokenizer.from_pretrained(model_name, revision=revision)
    input_ids = tokenizer.encode(tokenizer.eos_token + input_text + ' \n', return_tensors='pt')
    response_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    return response_text



if __name__ == "__main__":
    console = Console()
    console.print("\n[bold blue] Welcome to :robot:  my-gpt-bot")
    console.print("[bold blue] You can exit the chatbot at any time by typing 'bye' or 'exit'\n")
    # make the code recursive to get response from model
    while True:
        try:
            user_input = Prompt.ask("[yellow]:robot:  ask my-gpt-bot[/yellow]")
            # Check if user_input is empty or contains only whitespace characters
            if not user_input or user_input.isspace():
                continue
            # Check if user entered 'bye' or 'exit'
            if user_input.lower() in ["bye", "exit"]:
                console.print(Text("Goodbye!", style="bold read"))
                break
            # get response from model
            with console.status("[bold green]Thinking...[/bold green]") as status:
                start_time = time.time()
                res = get_response(user_input)
                end_time = time.time()
            
            console.print(f"[green]{res}")
            console.print(f"[bold blue]Time taken: {round(end_time - start_time)} seconds\n")
        except KeyboardInterrupt:
            console.print("[bold red]KeyboardInterrupt received. Goodbye!")
            break
