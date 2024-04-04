from openai import OpenAI
import time
import chatCompletion as cc

client = OpenAI()

cc.clearFiles(client)

file = client.files.create(
    file=open("base.py", "rb"),
    purpose='assistants'
)
        
assistant = client.beta.assistants.create(
    name = 'UI Builder',
    description = 'You fix errors in the python file.',
    model = "gpt-3.5-turbo",
    tools = [{"type": "code_interpreter"}],
    file_ids = [file.id]
)

thread = client.beta.threads.create()

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)

loopStarts = round(time.time())
while run.status in ['queued', 'in_progress', 'cancelling']:
    time.sleep(1)
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    loopEnds = round(time.time())
    print("It has been {0} seconds since the loop started".format(loopEnds - loopStarts))

if run.status == 'completed': 
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    for message in messages:
        print(message.content.value)
        print(message.file_ids)
else:
    print(run.status)