# An introduction to Git

## The concept

The goal is to create a tutorial:

- Teaching the basic Git skills.
- Teaching how to pull an existing project and contribute a patch.
- How to accept a patch for an own project
- Use as little as possible the terminal and rely on free software that is commonly in use by programmers (vscode).
- Takes two times two hours, for people with basic programming skills.

## Screenshots

The small VS Code window was 976 x 959.

## Exporting the result

The only export that somehow resulted in an ok result is

```sh
pandoc introduction-to-git.md -o introduction-to-git.html
```

- The markdown to pdf vscode extension did not produce any result
- Pandoc to pdf cannot process html tags (img).
- using pandoc to first converting the md file to html and then with the wkhtmltopdf engine it converts to a proper pdf.
