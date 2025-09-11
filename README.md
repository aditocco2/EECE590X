# EECE590X
EECE251 Question Development

## Uploading Question Pools to Brightspace

Once the CSV question pools (and supplemental images) have been generated, you can turn them into Brightspace quizzes with the following steps:

### Upload Images to the File System
**If your questions have images attached, it is important to upload the images _before_ uploading questions, because otherwise the questions won't link the images properly.**
- Go to `Course Tools` -> `Course Admin` -> `Manage Files`
- Navigate to the image directory specified by the CSV / Python script (usually `/imagepools/deadbeef` or `/imagepools/alivebeef`)
- `Upload`, select/drag the image, and finish with `Save`

### Upload Questions to the Question Library
- Go to `Quizzes` -> `Question Library`
- Make a `New` -> `Section` (basically a folder)
- Name the section/folder something relevant, for example, `q14_6` for HW/Quiz 14 Question 6
- Navigate to the section/folder you just made
- `Import` -> `Upload File`
- Select/drag the CSV and finish with `Import All`

### Import Questions to a Quiz
- In the `Quizzes` tab, click on a quiz to edit it (or make a new quiz)
- `Create New` -> `Question Pool` -> `Browse Question Library`
- Select the section/folder with all the questions and `Import`
- Give the question pool a relevant name
- Select `1` for `Number of Questions to Select` (unless you want more)
- `Save` the question and `Preview` the quiz to make sure it looks right

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

### Generating Requirements File
- `pip3 install pipreqs`
- `pipreqs . --force`

### Installing Requirements
- `pip3 install -r requirements.txt`
