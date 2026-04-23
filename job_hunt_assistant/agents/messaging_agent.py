"""Messaging agent for application notifications."""


class MessagingAgent:
    """Send notifications or messages during the job hunt process."""

    def send_message(self, recipient: str, subject: str, body: str) -> bool:
        """Placeholder implementation for sending a message."""
        print(f"Sending message to {recipient}: {subject}\n{body}")
        return True
