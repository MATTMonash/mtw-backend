# More Than Words Agentic AI FastAPI Server
> _A FastAPI Server with a LangGraph/LangChain Agentic Pipeline._

- (In Progress): The **FastAPI Server** is used to expose API endpoints for the frontend chat interface or create direct integrations with providers (e.g., WhatsApp, Messenger, Discord).
- (In Progess): The **LangGraph/LangChain Agentic Pipeline** is tailored to respond to queries.

---
## Development Setup
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
---

