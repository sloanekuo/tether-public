import google.generativeai as genai
import os

# Hardcode key just for this quick test (Delete after!)
genai.configure(api_key="AIzaSyBSWVDhDQwb5tkwXi-N-r5L7hV8wHwn9g8")

print("Checking available models...")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"✅ AVAILABLE: {m.name}")