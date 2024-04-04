import os, subprocess, time

def create(client,textInputField,parentUI):
        
        #Retrieved prompt from previous field and then clear it
        prompt = textInputField.toPlainText()
        textInputField.clear()

        systemRole = open('systemRole.txt').read()

        #Upload the base.py file
        baseUI = client.files.create(
            file=open("base.py", "rb"),
            purpose='assistants'
        )

        #Create the assistant with the correct role and model
        UIbuilderAssistant = client.beta.assistants.create(
            name = 'UI Builder',
            description = systemRole,
            model = "gpt-3.5-turbo",
            tools = [{"type": "code_interpreter"}],
            file_ids = [baseUI.id]
        )

        #Create the thread which messages are going to be saved on
        thread = client.beta.threads.create()

        #Add the first user prompt to the thread
        userMessage = client.beta.threads.messages.create(
            thread_id = thread.id,
            role = "user",
            content = prompt,
        )

        #Creates a run using the thread and assistant already created
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=UIbuilderAssistant.id
        )

        #Run is async, so make it sync 
        loopStarts = round(time.time())
        while run.status in ['queued', 'in_progress', 'cancelling']:
            time.sleep(1)
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            loopEnds = round(time.time())
            print("It has been {0} seconds since the loop started".format(loopEnds - loopStarts))
        

        #Retrieve the messages from the thread when the assistant is done.
        if run.status == 'completed': 
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )
            for message in messages:
                print(message.content)
                print(message.file_ids)
        else:
            print(run.status)
                            
        
        # generated_code = response.choices[0].message.content
        # clean_code = cleanResponse(generated_code)
        # updateFile('base.py',clean_code)

        # from base import window
        # generatedWindow = window()
        # parentUI.generatedWindows.append(generatedWindow)
        # #generatedWindow.show()

def cleanResponse(response):
        cleaned_response = response.strip()
        if cleaned_response.startswith('```python'):
            cleaned_response = cleaned_response[len('```python'):].strip()
        if cleaned_response.endswith('```'):
            cleaned_response = cleaned_response[:-len('```')].strip()

        return cleaned_response

def updateFile(path,code):
        with open(path,'w') as file:
            file.write("\n" + code)

def runUIFile():
        script_path = 'UI.py'
        venv_python_path = os.path.join('.venv', 'Scripts', 'python.exe')  
        try:
            subprocess.run([venv_python_path,script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running {script_path}: {e}")

def clearFiles(client):
    for file in client.files.list():
        client.files.delete(file.id)


