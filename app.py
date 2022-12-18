import os
import openai
from dotenv import load_dotenv
import argparse
from os.path import exists

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
models = ["text-ada-001", "text-babbage-001", "text-curie-001", "text-davinci-003"]
costPerThousand = [.004, .005, .0020, .0200]

parser = argparse.ArgumentParser()
parser.add_argument("request", help='The request text enclosed in double quotes.  Try: "Summarize this" or "Summarize this for Gen Z"')
parser.add_argument("-original", required=True, help="original text to act on. This can be a file name or text in quotes.")
parser.add_argument("-model", type=int, default=3, help="the model levels 1 to 4. Defaults to 3. Higher levels are more capable buit more expensive.")
parser.add_argument("-number", type=int, default=1, help="The number of outputs 1 to a max of 5. Be careful here as this adds to cost.")
parser.add_argument("-temperature", type=float, default=0.7, help="Higher values mean the model will take more rishs.  0 is minimum and max is 0.9.")
parser.add_argument("-maxOutputTokens", type=int, default=64, help="Maximum number of tokens in the output.  64 is around max length of a tweet and is the default.")
parser.add_argument("-debug", type=bool, help="Show raw response.")

args = parser.parse_args()

if args.model > 4 or args.model < 1:
  raise argparse.ArgumentError("model must be an integer between 1 and 4")

if args.number < 1 or args.number > 5:
  raise argparse.ArgumentError("number must be an integer between 1 and 5")

if args.temperature < 0 or args.temperature > 0.9:
  raise argparse.ArgumentError("number must be a floating point number between 0.0 and 0.9")

if args.maxOutputTokens < 0:
  raise argparse.ArgumentError("maxOutputTokens must be an integer greater than zero")

original = ""
isFile = False
if exists(args.original):
  with open(args.original) as f:
    original = f.read()
    isFile = True
else:
  original = args.original
  
print("--------------------------------------------------------------")
print(f"Model: {models[args.model - 1]}")
print(f"Number of outputs: {args.number}")
print(f"Temperature: {args.temperature}")
print(f"Max output tokens: {args.maxOutputTokens}")
print(f"Request: {args.request}")
if isFile:
  print(f"File: {args.original}")
else:
  print(f"original text: {args.original}")
print("")

prompt = f"{args.request}\n\n{original}"

response = openai.Completion.create(
  model=models[args.model - 1],
  prompt=prompt,
  n = args.number,
  temperature=args.temperature,
  max_tokens=args.maxOutputTokens,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

if args.debug:
  print(response)

tokens = response.usage.total_tokens;
cost = (tokens/1000) * costPerThousand[args.model - 1]

print(f"Cost ${cost}")

i = 0
for choice in response.choices:
  print(f"Output {i + 1}: {response.choices[i].text}")
  i += 1
