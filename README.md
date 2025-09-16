# More Than Words Agentic AI FastAPI Server
> _A FastAPI Server with a LangGraph/LangChain Agentic Pipeline._

- The **FastAPI Server** is used to expose API endpoints for the frontend chat interface or create direct integrations with providers (e.g., WhatsApp, Messenger, Discord).
- The **LangGraph/LangChain Agentic Pipeline** is tailored to respond to queries.

---

## Setup

<!-- DEVELOPMENT ENVIRONMENT SETUP -->
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

<!-- PRE COMMIT HOOK SETUP -->
<details>
<summary><strong>🔍 Pre-commit Hook Setup</strong> (please set this up before making commits)</summary>

Prior to committing code, it's essential to ensure code quality, security, and consistency. This project uses multiple pre-commit hooks to maintain high standards.

### Configuring the hooks
The project includes a `.pre-commit-config.yaml` file with comprehensive quality checks. To activate the hooks in your local repository:
```bash
pre-commit install
```

### What the hooks check
After installation, every `git commit` will automatically run:

**Code Quality & Formatting:**
- **Ruff** - Python linting and auto-formatting for consistent code style

**Security:**
- **Bandit** - Scans Python code for common security vulnerabilities and issues
- **Detect Private Key** - Prevents accidental commits of SSH keys, API tokens, and other secrets

**Commit Standards:**
- **Conventional Commits** - Enforces commit message format (e.g., `feat:`, `fix:`, `docs:`)

### How it works
The hooks will:
- Auto-fix issues where possible (formatting, trailing whitespace)
- Block commits if security vulnerabilities or private keys are detected
- Ensure commit messages follow conventional format
- Provide clear feedback on what needs to be fixed manually

### Testing the setup (optional)
To verify everything is working correctly, run the hooks manually on all files:
```bash
pre-commit run --all-files
```

</details>

<!-- COMMIT STANDARD -->
<details>
<summary><strong>📝 Commit Standard</strong> (pre-commit will fail if not adhered to)</summary>

For this project, we follow the conventional commits standard. See this cheatsheet below to get an idea of how commits should be made.

### Quick Examples
- `feat: new feature`
- `fix(scope): bug in scope`
- `feat!: breaking change` / `feat(scope)!: rework API`
- `chore(deps): update dependencies`

### Commit Types
- `build`: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- `ci`: Changes to CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
- **`chore`: Changes which doesn't change source code or tests e.g. changes to the build process, auxiliary tools, libraries**
- `docs`: Documentation only changes
- **`feat`: A new feature**
- **`fix`: A bug fix**
- `perf`: A code change that improves performance
- `refactor`:  A code change that neither fixes a bug nor adds a feature
- `revert`: Revert something
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `test`: Adding missing tests or correcting existing tests

### Reminders
- Put newline before extended commit body
- More details at **[conventionalcommits.org](https://www.conventionalcommits.org/)**

</details>

---