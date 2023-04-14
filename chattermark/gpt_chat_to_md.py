# gpt_chat_to_md.py
from .gpt_chat_model import GPTChatSession


def gpt_chat_session_to_md(chat_session: GPTChatSession) -> str:
    md_output = []

    for message in chat_session.messages:
        if message.sender == "assistant":
            md_output.append(f"> {message.content}\n")
        else:
            md_output.append(f"{message.sender}: {message.content}\n")

    return "".join(md_output)


if __name__ == "__main__":
    # Example usage
    from gpt_chat_model import Message
    from datetime import datetime

    messages = [
        Message(
            sender="user",
            content="Hello, GPT!",
            timestamp=datetime.fromisoformat("2023-04-13T15:32:10.123Z"),
        ),
        Message(
            sender="assistant",
            content="Hello! How can I help you?",
            timestamp=datetime.fromisoformat("2023-04-13T15:32:12.456Z"),
        ),
    ]

    gpt_chat_session = GPTChatSession(session_id="some_unique_id", messages=messages)
    markdown_output = gpt_chat_session_to_md(gpt_chat_session)
    print(markdown_output)
