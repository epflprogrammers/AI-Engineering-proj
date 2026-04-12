import os
from config import maxchars
from google.genai import types

def getfilecontent(workingdir, filepath):
    absworkdir = os.path.abspath(workingdir)
    absfilepath = os.path.abspath(os.path.join(workingdir,filepath))

    if not absfilepath.startswith(absworkdir):
        return(f"Error:{filepath} not in workingdir")
    if not os.path.isfile(absfilepath):
        return(f"Error: {filepath} is not a file")
    
    try:
        with open(absfilepath, "r") as f:
            filecontstr = f.read()
        if len(filecontstr) > maxchars:
            filecontstr = filecontstr[:maxchars]
            print(f"file {filepath} truncated")

        return(filecontstr)
    
    except Exception as e:
        return(f"exception reading file:{e}")


schemagetfilecontent = types.FunctionDeclaration(
    name="getfilecontent",
    description="Gets the content of the given file as a string, constrained to a working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="The path to the file, from the working directory.",
            ),
        },
    ),
)
