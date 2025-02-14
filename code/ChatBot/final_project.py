from typing import List, Dict
from utils import query_llm

class Memory:
    """Stores conversation history"""
    def __init__(self):
        # Store last 3 messages (each message is a dictionary with 'role' and 'content')
        self.messages: List[Dict] = []
    
    def add_message(self, role: str, content: str) -> None:
        """Add a new message to memory while keeping only the last 3 messages."""
        self.messages.append({"role": role, "content": content})
        self.messages = self.messages[-3:]
    
    def get_recent_messages(self) -> str:
        """Return recent messages as a formatted string."""
        return "\n".join(f"{msg['role'].capitalize()}: {msg['content']}" for msg in self.messages).strip()

class Chatbot:
    """Base chatbot class with core functionality"""
    def __init__(self, name: str):
        self.name: str = name
        self.memory: Memory = Memory()
    
    def _create_prompt(self, user_input: str) -> str:
        """Create a prompt for the LLM including recent conversation history."""
        recent_messages = self.memory.get_recent_messages()
        return f"{recent_messages}\nUser: {user_input}\n{self.name}:"
    
    def generate_response(self, user_input: str) -> str:
        """Generate a response using the LLM."""
        self.memory.add_message("user", user_input)
        prompt = self._create_prompt(user_input)
        response = query_llm(prompt)
        self.memory.add_message("bot", response)
        return response

class FriendlyBot(Chatbot):
    """A casual and friendly chatbot"""
    def _create_prompt(self, user_input: str) -> str:
        recent_messages = self.memory.get_recent_messages()
        return (f"{recent_messages}\nUser: {user_input}\n{self.name}: "
                "That’s a great question. Let me help you!")

class TeacherBot(Chatbot):
    """An educational chatbot with a specific subject"""
    def __init__(self, name: str, subject: str):
        super().__init__(name)
        self.subject = subject
    
    def _create_prompt(self, user_input: str) -> str:
        recent_messages = self.memory.get_recent_messages()
        return (f"{recent_messages}\nUser: {user_input}\n{self.name}: "
                f"As a teacher of {self.subject}, let me explain it in detail to you.")

class AssistantBot(Chatbot):
    """An assistant bot with a helpful, service-oriented personality"""
    def _create_prompt(self, user_input: str) -> str:
        recent_messages = self.memory.get_recent_messages()
        return (f"{recent_messages}\nUser: {user_input}\n{self.name}: "
                "I'm here to assist you with anything you need. How can I help today?")

def show_help():
    """Display help information."""
    print("\nAvailable commands:")
    print("/help - Show this help message")
    print("/quit - Exit the chatbot")
    print("/change - Change your chatbot\n")

def main():
    """Main interaction loop"""
    bot = None
    
    def select_bot():
        nonlocal bot
        """Function to select chatbot"""
        while True:
            print("Choose your chatbot:")
            print("1. Friendly Bot")
            print("2. Teacher Bot")
            print("3. Assistant Bot")
            print("Type /help for assistance.")
            
            choice = input("Enter 1, 2, or 3: ").strip()
            
            if choice == "/help":
                show_help()
                continue
            elif choice == "1":
                bot = FriendlyBot("Joy")
                break
            elif choice == "2":
                subject = input("What subject should I teach? ")
                bot = TeacherBot("Prof. Smith", subject)
                break
            elif choice == "3":
                bot = AssistantBot("Alex")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or /help.")
    
    select_bot()  # Initial bot selection
    
    print(f"\n{bot.name}: Hello! How can I help you today?")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "/quit":
            break
        elif user_input.lower() == "/help":
            show_help()
            continue
        elif user_input.lower() == "/change":
            print(f"\n{bot.name}: Switching to a new chatbot...")
            select_bot()  # Reset the bot selection when "/change" is typed
            print(f"\n{bot.name}: Hello! How can I help you today?")
            continue
        
        response = bot.generate_response(user_input)
        print(f"{bot.name}: {response}")

if __name__ == "__main__":
    main()
