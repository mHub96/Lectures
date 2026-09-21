# Test helper to verify QR code and MQTT library syntax
import sys

print("Testing python environment for generating HTML...")
import deck1_data
import deck2_data
print(f"Deck 1 slides: {len(deck1_data.DECK1_SLIDES)}")
print(f"Deck 2 slides: {len(deck2_data.DECK2_SLIDES)}")

