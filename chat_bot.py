from rich.console import Console
from rich.prompt import Confirm, Prompt
from rich.markdown import Markdown

import google.generativeai as genai

EXIT_OPTIONS = ["quit", "exit", "stop", "end", "terminate", "close", "terminate"]

console = Console()

def append_file(files: list) -> list:
    file_path = Prompt.ask(prompt="Enter file path", console=console)
    try:
        files.append(genai.upload_file(path=file_path, display_name=file_path))
    except Exception as e:
        console.print(f"Error uploading file: {e}")
    
    while True:
        add_more = Confirm.ask(prompt="Add another?", console=console)
    
        if add_more:
            return append_file(files)
        else:
            return files

def add_files() -> list | None:
    files = []
    while True:
        add_files = Confirm.ask(prompt="Do you want to add any files?", console=console)
        if add_files:
            files = append_file(files)
            break 
        else:
            return None
        
    return files

def chat_bot(model: genai.GenerativeModel):
    chat = model.start_chat()
    console.print("\nWelcome to Gemini! Ask me anything, or type 'quit/exit/stop' etc to end the program.")

    while True:
        prompt = Prompt.ask(prompt="Ask me", console=console)

        if prompt.lower() in EXIT_OPTIONS:
            break

        files = add_files()

        try:
            if files is not None:
                message = [prompt] + files
                response = chat.send_message(message)
            else:
                response = chat.send_message(prompt)
        except Exception as e:
            print(f"Error sending message: {e}")
            continue

        console.print(Markdown(response.text))

