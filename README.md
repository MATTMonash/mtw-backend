# More Than Words Agentic AI FastAPI Server
> _A FastAPI Server with a LangGraph/LangChain Agentic Pipeline._

- The **FastAPI Server** is used to expose API endpoints for the frontend chat interface or create direct integrations with providers (e.g., WhatsApp, Messenger, Discord).
- The **LangGraph/LangChain Agentic Pipeline** is tailored to respond to queries.

---

<details>
<summary><strong>🛠️ Development Environment Setup</strong></summary>

Prior to starting development, its a good idea to setup your virtual environment.
This will be managed using `uv`, first install this package manager so you can use the CLI commands.

### UV installation
Check the official documentation to install `uv`. Really easy, just copy and paste the command into your terminal, and you should have the CLI working.
- https://docs.astral.sh/uv/getting-started/installation/

### Virtual environment setup
In your terminal setup your virtual environment. This will create a `.venv/` folder in the project root.
```bash
uv sync
```
If you're developing on VSCode please also apply this virtual environment's Python interpreter on VSCode.

### Select the virtual environment's interpreter on VS Code
1. Press `Ctrl + Shift + P` (Windows) or `Cmd + Shift + P` (macOS)
2. Begin by typing "Python select interpreter" and select the command from the dropdown list.
3. Choose the virtual environments interpreter "Python 3.x.x (mtw-backend)".
4. Now you're all good to go!

### Environment variables setup
1. Take a look at the `.env.template` file, those are the env variables you'll need.
2. Create a duplicate of the `.env.template` file and rename it to `.env`, set the environment variables.

### Ruff extension for VS Code (optional but really helpful)
For real-time linting feedback, install the Ruff extension:
1. Open Extensions (`Ctrl + Shift + X` or `Cmd + Shift + X`)
2. Search for "Ruff" by Astral Software
3. Click Install

The extension will automatically use the project's ruff configuration and highlight issues as you code.

### Actually running the server!
To run the server you need to open a terminal and first make sure that you have your virtual environment setup.
1. Apply virtual environment. In your terminal write `.venv/scripts/activate` (Windows) 
or `source .venv/scripts/activate` (macOS)
2. Run the server with `uvicorn app.main:app`, or you can do `uvicorn app.main:app --reload` for hot reloading whilst you code.

</details>

<details>
<summary><strong>🔍 Pre-commit Hook Setup</strong></summary>

Prior to committing code, it's essential to ensure code quality and consistency. This project uses `ruff` for linting and formatting, automated through pre-commit hooks.

### Configuring the hooks
The project already inclues a `.pre-commit-config.yaml` file with ruff configured. To activate the hooks in your local repository:
```
pre-commit install
```
### How it works
After installation, every `git commit` will automatically:
- Check your code for errors and style violations
- Auto-fix issues where possible
- Format your code consistently
- Block the commit if critical issues need manual fixing
### Testing the setup (optional)
To verify everything is working correctly, run the hooks manually on all files:
```bash
pre-commit run --all-files
```

</details>

---