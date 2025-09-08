# EECE590X
EECE251 Question Development

## Importing Custom Libraries and Modules
This project uses many custom modules stored in the `libs` folder, the most notable being `d2l`. In order to use these modules in your Python files, you will need to add `libs` to your default Python path. Here's how to do this in Windows:
- Search the Start menu for "environment variables"
- Click `Environment Variables`
- Click `New` under `User Variables`
- Name the variable `PYTHONPATH` and make its value something like `C:/path/to/your/EECE590X/libs`
- Do the same for `System Variables`
- Confirm that it worked by going into a Python shell and entering `import sys; sys.path`
- Restart your command line / IDE if necessary

Alternatively, you can specify PYTHONPATH in the command line as you run the script:
- `PYTHONPATH="/path/to/your/EECE590X/libs" python3 <script>.py`

## Generating Requirements File
- `pip3 install pipreqs`
- `pipreqs . --force`

## Installing Requirements
- `pip3 install -r requirements.txt`
