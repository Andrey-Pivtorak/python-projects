import time

# dictionary
d = {
    'time': time.time(),
    'name': 'Jack',
    'text': 'Hello there!'
}


db = [
    {
        'time': time.time(),
        'name': 'Jack',
        'text': 'Hello Mary!'
    },
    {
        'time': time.time(),
        'name': 'Mary',
        'text': 'Hi, Jack! How are you?'
    }
]


# send message
def send_message(name, text):
    # to do: make message and add to db
    message = {
        'time': time.time(),
        'name': name,
        'text': text,
    }
    db.append(message)
    
    
 def get_messages(after):
    """messages from db after given timestamp"""
    result=[]
    for message in db:
        if message['time'] > after:
            result.append(message)
    return result

print(db)

t1 = db[-1]['time']
print(get_messages(t1))

send_message('123', '123')
send_message('123', '456')
print(get_messages(t1))

t2 = db[-1]['time']
print(get_messages(t2))

send_message('123', '789')
print(get_messages(t2))
    
