"""
Filter mail from Google.
"""

from src.utils import gmail_authenticate
import base64
from googleapiclient.discovery import Resource

import base64
from typing import Tuple, List
from googleapiclient.discovery import Resource

def get_newsletters(
    service: Resource,
    query="label:inbox is:unread",
    max_results=100
) -> Tuple[str, List[str]]:
    """
    Fetches emails matching a Gmail search query.
    Returns:
      - concatenated text bodies
      - list of message IDs to allow deletion
    """
    results = service.users().messages().list(
        userId="me",
        q=query,
        maxResults=max_results
    ).execute()

    messages = results.get("messages", [])
    all_bodies = []
    message_ids = []

    for msg in messages:
        message_ids.append(msg["id"])

        msg_data = service.users().messages().get(
            userId="me",
            id=msg["id"],
            format="full"
        ).execute()

        parts = msg_data["payload"].get("parts", [])
        body_text = None

        for part in parts:
            if part.get("mimeType") == "text/plain" and "data" in part.get("body", {}):
                body_text = base64.urlsafe_b64decode(
                    part["body"]["data"]
                ).decode("utf-8", errors="ignore")
                break

        if body_text:
            all_bodies.append(body_text)

    return "\n\n---\n\n".join(all_bodies), message_ids


def filter_mail(mail: str) -> bool:
    """
    Filter mail from Google.
    """
    client = gmail_authenticate()
    import pdb; pdb.set_trace()
    newsletters, ids = get_newsletters(client)
    return True