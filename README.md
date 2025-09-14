# AI Chat Reply Automation

Short description
- Automates selecting chat text, copying it, checking if the last message is from a specific sender, generating a reply with Google Gemini, and pasting the reply back into the chat.

Repository files
- [program.py](program.py) — main automation script; contains the [`is_last_message_from`](program.py) function and the [`model`](program.py) configuration.
- [move.py](move.py) — helper script to print mouse coordinates.
- [tempCodeRunnerFile.py](tempCodeRunnerFile.py) — temporary snippet left in workspace.
- [.env](.env) — environment variables (store your API key here).
- [.gitignore](.gitignore) — ignores the .env file.

Requirements
- Python 3.8+
- Packages:
  - pyautogui
  - pyperclip
  - python-dotenv
  - google-generative-ai (or the package that provides `google.generativeai`)
  - time (standard lib)
- Install via:
  ```sh
  pip install pyautogui pyperclip python-dotenv google-generative-ai

  Setup

Place your Gemini (Google generative AI) API key into the .env file as an environment variable named GEMINI. The current program.py loads GEMINI:

Ensure .env contains a line like<vscode_annotation details='%5B%7B%22title%22%3A%22hardcoded-credentials%22%2C%22description%22%3A%22Embedding%20credentials%20in%20source%20code%20risks%20unauthorized%20access%22%7D%5D'>: </vscode_annotation> ``` GEMINI=your_api_key_here
Note: the existing .env currently contains GEMINI_API; update the variable name or update program.py to read that name.
Verify coordinates

Use move.py to print cursor coordinates and update the click/drag coordinates in program.py if needed.


Usage

Run the automation:
- python program.py

After a short delay the script will:
1. Click the configured icon position and select the chat area.
2. Copy the selected chat to clipboard and parse it.
3. Use is_last_message_from to check whether the last message sender matches the configured name (default: "Hardik").
4. If matched, call the configured Gemini model ([model](program.py)) to generate a reply, paste it into the chat input, and send it.
5. Important notes & safety

This script uses GUI automation (pyautogui). Ensure the target window is visible and coordinates match your screen resolution.
Automating input can interfere with your control of the system; use with caution.
Keep your API key secret. The repository .gitignore already includes .env.
Key functions and where to find them

Message-checking logic: is_last_message_from (in program.py)
Model config: model (in program.py)
Coordinate helper: move.py
Troubleshooting

If the script copies nothing, verify selection coordinates and clipboard permissions.
If API calls fail, confirm GEMINI env var is set and the package is correctly installed.
If model responses are unexpected, inspect the system instruction in model.
License & security

Do not commit your .env; it is already in .gitignore.
Treat API keys as secrets.
Contact

For adjustments to coordinates or parsing logic, modify program.py and use move.py for coordinate discovery.
