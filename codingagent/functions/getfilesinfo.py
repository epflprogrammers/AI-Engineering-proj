import os
from google.genai import types


def getfilesinfo(workingdir, dir = "."):
    absworkingdir = os.path.abspath(workingdir)

    
    absdir = os.path.abspath(os.path.join(workingdir,dir))

    if not absdir.startswith(absworkingdir):
        return(f"Error:{dir} is not a directory")
    
    finalresponse = ""
    contents = os.listdir(absdir)

    for content in contents:
        contentpath = os.path.join(absdir,content)
        isdir = os.path.isdir(contentpath)
        size = os.path.getsize(contentpath)
        finalresponse += f"-{content}: filesize={size} bytes, isdir = {isdir}\n"

    return(finalresponse) 

    

schemagetfilesinfo = types.FunctionDeclaration(
    name="getfilesinfo",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "dir": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

