import ast
import json
import csv
import os
import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "How are you feeling today?"},
    ]
)


def response(chatLog):
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            chatLog
        ]
    )
    assistant_response = chat_completion['choices'][0]['message']['content']
    print("Bot:", assistant_response.strip("\n").strip())
    return {"role": "assistant", "content": assistant_response.strip()}


chat_log = []
if not os.path.exists("./MindfulChatlog.csv"):
    data = [{"role": "system", "content": "How are you feeling today?"}]

    with open('MindfulChatlog.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # writer.writerow(header)
        writer.writerow(data)

with open('MindfulChatlog.csv') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        temp1 = str(str(line)[2:-2])
        temp2 = ast.literal_eval(temp1)
        chat_log.append(temp2)
print(chat_log)




chat_log.append({"role": "system", "content": "How are you feeling today?"})
print(completion)
while True:
    user_input = input()
    if user_input == "quit":
        # SAVE CHATLOG
        data = chat_log
        for i in range(0, len(data)):
            data[i]=[data[i]]
        with open('MindfulChatlog.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        break
    else:
        chat_log.append({"role": "user", "content": user_input})
        chat_log.append(response(chat_log))
