def send_messages(sent_messages, messages):
    for message in messages:
        sent_messages.append(message)
        print(sent_messages)
    print("The existing message list is: ")
def show_messages(messages):
    for message in messages:
        print(message)
messages = ["hi", "bye", "why", "my", "lie"]
sent_messages = []
send_messages(sent_messages, messages[:])
show_messages(messages)
