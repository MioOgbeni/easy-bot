import os
import time
from twitchio.ext import commands

# Load credentials from environment variables
BOT_NICK = os.getenv("BOT_NICK")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL")

# Thresholds and time windows
MESSAGE_THRESHOLD = 3  # Number of repeats to trigger echo
TIME_WINDOW = 5  # Time window in seconds
COOLDOWN_PERIOD = 180  # Cooldown time in seconds (3 minutes)
TARGET_MESSAGE = "!easy"  # The only message to track

class EchoBot(commands.Bot):
    def __init__(self):
        super().__init__(token=BOT_TOKEN, prefix="!", nick=BOT_NICK, initial_channels=[CHANNEL])
        self.message_cache = []
        self.last_echo_time = 0  # Track when the last echo happened

    async def event_ready(self):
        print(f"{self.nick} is online in {CHANNEL}!")

    async def event_message(self, message):
        if message.echo:  # Avoid responding to itself
            return

        await message.channel.send("FUNGUJU!")

        # now = time.time()

        # # Check if the bot is on cooldown
        # if now - self.last_echo_time < COOLDOWN_PERIOD:
        #     return  # Ignore all messages during cooldown

        # # Only process messages that match the target
        # if message.content.lower() == TARGET_MESSAGE:
        #     # Add the timestamp to the cache
        #     self.message_cache.append(now)

        #     # Remove old timestamps outside the TIME_WINDOW
        #     self.message_cache = [
        #         timestamp for timestamp in self.message_cache
        #         if now - timestamp <= TIME_WINDOW
        #     ]

        #     # Check if the message count exceeds the threshold
        #     if len(self.message_cache) >= MESSAGE_THRESHOLD:
        #         await message.channel.send("FUNGUJU!")
        #         self.last_echo_time = now  # Set the cooldown timer
        #         self.message_cache.clear()  # Reset the cache after echoing

# Run the bot
if __name__ == "__main__":
    bot = EchoBot()
    bot.run()
