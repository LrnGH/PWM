from fastapi import  HTTPException
import aiohttp
import os
from  dotenv import load_dotenv

load_dotenv(".env")

token=os.environ["ACCESS_TOKEN"]
version=os.environ["VERSION"]
phone=os.environ["PHONE_NUMBER_ID"]


async def send_message(data):
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    async with aiohttp.ClientSession() as session:
        url = f"https://graph.facebook.com/{version}/{phone}/messages"
        try:
            async with session.post(url, data=data, headers=headers) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    raise HTTPException(status_code=response.status, detail="Message not sent")
        except aiohttp.ClientConnectorError as e:
            raise HTTPException(status_code=500, detail=f"Connection error: {str(e)}")

def get_text_message_input(recipient, text):
    return {
        "messaging_product": "whatsapp",
        "preview_url": False,
        "recipient_type": "individual",
        "to": recipient,
        "type": "text",
        "text": {
            "body": text
        }
    }