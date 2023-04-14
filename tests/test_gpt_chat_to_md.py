# test_gpt_chat_to_md.py
from datetime import datetime

import pytest

from chattermark.gpt_chat_model import GPTChatSession, Message
from chattermark.gpt_chat_to_md import gpt_chat_session_to_md


@pytest.fixture
def sample_chat_session():
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
    return GPTChatSession(session_id="some_unique_id", messages=messages)


def test_gpt_chat_session_to_md(sample_chat_session):
    expected_output = "user: Hello, GPT!\n" "> Hello! How can I help you?\n"
    md_output = gpt_chat_session_to_md(sample_chat_session)
    assert md_output == expected_output


def test_empty_chat_session():
    chat_session = GPTChatSession(session_id="empty_session", messages=[])
    expected_output = ""
    md_output = gpt_chat_session_to_md(chat_session)
    assert md_output == expected_output


def test_chat_session_with_unknown_sender_type():
    messages = [
        Message(
            sender="unknown",
            content="I'm not a user or an assistant!",
            timestamp=datetime.fromisoformat("2023-04-13T15:32:10.123Z"),
        ),
    ]
    chat_session = GPTChatSession(session_id="unknown_sender", messages=messages)
    expected_output = "unknown: I'm not a user or an assistant!\n"
    md_output = gpt_chat_session_to_md(chat_session)
    assert md_output == expected_output
