import os, subprocess

def create(client,textInputField,parentUI):
        prompt = textInputField.toPlainText()
        textInputField.clear()
        conversation = open('conversation.txt').readlines()
        baseWindow = open('base.py','r').read()
        promptExt = conversation[0]+' prompt:'+prompt+' window:'+baseWindow
        print(promptExt)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": conversation[0]},
                {"role": "user", "content": promptExt},
            ])
        generated_code = response.choices[0].message.content
        clean_code = cleanResponse(generated_code)
        updateFile('base.py',clean_code)  #Does up to here, then no other window shows
        from base import window
        generatedWindow = window()
        parentUI.generatedWindows.append(generatedWindow)
        generatedWindow.show()

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
