# EECE590X
251 but I make the questions

## Importing the D2L Library
`d2l` is a custom library made by Dr. Summerville. In order to import it in your Python files, you will need to add its parent folder to your default Python path. Here's how to do this in Windows:
- Search the Start menu for "environment variables"
- Click `Environment Variables`
- Click `New` under `User Variables`
- Name the variable `PYTHONPATH` and make its value something like `C:/path/to/your/EECE590X`
- Do the same for `System Variables`
- Confirm that it worked by going into a Python shell and entering `import sys; sys.path`

Alternatively, you could just paste the `d2l` folder into the same folder as every Python script you run. It would just be hella annoying.
