import os
from google.genai import types

def writefile(workingdir, filepath, content):
    absworkingdir = os.path.abspath(workingdir)
    absfilepath = os.path.abspath(os.path.join(workingdir,filepath))
    if not absfilepath.startswith(absworkingdir):
        return(f"error: {filepath} is not working dir")
    
    parentdir = os.path.dirname(absfilepath)
    if not os.path.isdir(parentdir):
        try:
            os.makedirs(parentdir, exist_ok = True)
        except Exception as e:
            return(f"couldnt create dir")
    
    try:
        with open(absfilepath,"w") as f:
            f.write(content)
        return("wrote it")

    except Exception as e:
        return(f"couldn't write content")
        



schemawritefile = types.FunctionDeclaration(
    name="writefile",
    description="Overwrites an existing file or writes to a new file if it doesn't exist (and creates required parent dirs safely)",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents to write to a file as a string.",
            )
        },
    ),
)

