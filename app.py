import os
import openai
from dotenv import load_dotenv
import argparse
from os.path import exists

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
models = ["text-ada-001", "text-babbage-001", "text-curie-001", "text-davinci-003"]

parser = argparse.ArgumentParser()
parser.add_argument("request", help='The request text enclosed in double quotes.  Try: "Summarize this" or "Summarize this for Gen Z"')
parser.add_argument("-original", required=True, help="original text to act on. This can be a file name or text in quotes.")
parser.add_argument("-model", type=int, default=3, help="the model levels 1 to 4. Defaults to 3. Higher levels are more capable buit more expensive.")

args = parser.parse_args()

if args.model > 4 or args.model < 1:
  raise argparse.ArgumentError("model must be an integer between 1 and 4")

original = ""
isFile = False
if exists(args.original):
  with open(args.original) as f:
    original = f.read()
    isFile = True
else:
  original = args.original
  
print("--------------------------------------------------------------")
print(f"Request:{args.request}")
if isFile:
  print(f"File:{args.original}")
else:
  print(f"original text:{args.original}")
print("\n\n")

prompt = f"{args.request}\n\n{original}"

response = openai.Completion.create(
  model=models[args.model - 1],
  prompt=prompt,
  temperature=0.7,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response)