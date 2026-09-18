import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

bot_token = os.getenv("SLACK_BOT_TOKEN")
app_token = os.getenv("SLACK_APP_TOKEN")

if not bot_token or not bot_token.startswith("xoxb-"):
    raise SystemExit("Missing or invalid SLACK_BOT_TOKEN in .env. Add your Bot User OAuth Token.")

if not app_token or not app_token.startswith("xapp-"):
    raise SystemExit("Missing or invalid SLACK_APP_TOKEN in .env. Add your App-Level token.")

app = App(token=bot_token)

@app.event("app_mention")
def handle_app_mention(event, say):
    text = event.get("text", "")
    say(f"Hi! You mentioned me: {text}")

if __name__ == "__main__":
    handler = SocketModeHandler(app, app_token)
    print("Bot is running...")
    handler.start()