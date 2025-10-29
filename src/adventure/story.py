from adventure.utils import read_events_from_file
from rich import print
import random

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[red]You stand still, unsure what to do. The forest swallows you.[/red]"

def left_path(event):
    return "[pink]You walk left. [/pink]" + event

def right_path(event):
    return "[pink]You walk right. [/pink]" + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("[green]You wake up in a dark forest. You can go left or right.[/green]")
    while True:
        print("[green]Which direction do you choose?[/green] [green]([/green][purple]left[/purple][green]/[/green][purple]right[/purple][green]/[/green][yellow]exit[/yellow][green]):[/green] ")
        choice = input()
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        print("[green]"+step(choice, events)+"[/green]")
    print("[yellow]The forest bids you goodbye[/yellow]")
