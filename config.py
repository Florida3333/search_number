from dotenv import load_dotenv
import os

load_dotenv()

NUM_DIGITS = int(os.getenv('NUM_DIGITS'))
MAX_GUESSES = int(os.getenv('MAX_GUESSES'))
