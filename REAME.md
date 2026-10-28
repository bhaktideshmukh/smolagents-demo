# smolagents Demo

A simple AI agent built with Hugging Face's [smolagents](https://huggingface.co/docs/smolagents)
library. It uses a `CodeAgent` that can search the web (DuckDuckGo) and use a
custom tool (word counter), powered by Google Gemini.

## How it works

The agent follows a ReAct loop: it **thinks**, writes Python code to call a tool,
**observes** the result, and repeats until it can give a final answer. Each step
is printed in the terminal.

## Project structure

```
smolagents-demo/
├── agent.py            # Entry point: builds and runs the agent
├── tools.py            # Custom tools
├── requirements.txt    # Dependencies
├── .env.example        # Template for environment variables
└── README.md
```

## Setup

1. Clone the repo
   ```bash
   git clone https://github.com/<your-username>/smolagents-demo.git
   cd smolagents-demo
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv

   # Windows (PowerShell)
   venv\Scripts\Activate.ps1

   # macOS / Linux
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   python -m pip install -r requirements.txt
   ```

4. Add your API key
   - Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com)
   - Copy the template and fill it in:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and set `GEMINI_API_KEY`

## Run

```bash
python agent.py
```

Then enter a task, for example:

```
Search for what the smolagents library is, summarize it in one sentence,
then tell me how many words your summary has.
```

## Using a different model

The model is set in `agent.py`. smolagents lets you swap it without changing
the rest of the code:

- **Gemini / OpenAI / Anthropic** via `LiteLLMModel`
- **Hugging Face Inference Providers** via `InferenceClientModel` (needs credits)
- **Local models** via Ollama and `LiteLLMModel`

## Notes

- `CodeAgent` executes LLM-generated Python code. Use a sandbox for anything
  beyond experiments.
- Never commit your `.env` file. It is listed in `.gitignore`.

## Built with

- [smolagents](https://github.com/huggingface/smolagents)
- [LiteLLM](https://github.com/BerriAI/litellm)
- [ddgs](https://pypi.org/project/ddgs/)