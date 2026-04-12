import os
import subprocess
from google.genai import types

def runpythonfile(workingdir,filepath,args=[]):
    absworkingdir = os.path.abspath(workingdir)
    absfilepath  = os.path.abspath(os.path.join(workingdir,filepath))

    if not absfilepath.startswith(absworkingdir):
        return("error not in working dir.")
    
    if not os.path.isfile(absfilepath):
        return("error: not a file")
    
    if not filepath.endswith(".py"):
        return("not a pythonfile.")
    
    try:
        finalargs= ["python3",filepath]
        finalargs.extend(args)
        output = subprocess.run(finalargs,
                                cwd = absworkingdir,
                                timeout=30,
                                capture_output = True)
        finalstring = f"""
        STDOUT: {output.stdout}
        STDERR: {output.stderr}
        """
        if output.stdout == "" and output.stderr == "":
            finalstring = "No output produced.\n"

        if output.returncode !=0:
            finalstring += f"process exited with {output.returncode}"

        return(finalstring)
    
    except Exception as e:
        return(f"Error executing file {e}")


schemarunpythonfile = types.FunctionDeclaration(
    name="runpythonfile",
    description="Runs a python file with the python3 interpreter. Accepts additional CLI args as an optional array.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="The file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional array of strings to be used as the CLI args for the Python file.",
                items = types.Schema(type = types.Type.STRING,),
            ),
        },
    ),
)
