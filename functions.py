def content_msg(msg):
    msg = msg.split()
    msg[0] = ''
    print(msg)
    msg = ' '.join(msg)
    return msg.strip()
