# AGENTS

## Workspace overview
- Small Python practice repository.
- Main files are simple scripts in the root: `billsplit.py`, `ceasarcipher.py`, `EmployeeprofileGenerator.py`, `hello.py`, `reportcardprinter.py`.
- No build system, tests, or package structure.

## Agent behavior
- Do not give unsolicited suggestions or fixes before the user asks.
- Wait for the user to write their code and explicitly request corrections.
- When asked to correct or improve code, respond with concise, targeted feedback.
- Preserve the user’s learning process by avoiding step-by-step guidance unless requested.

## When helping
- Focus on the current file the user is editing.
- Keep explanations minimal and code-focused.
- Do not assume the user wants a full rewrite unless they ask for one.
