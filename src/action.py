def check_for_success(command):
    while True:
        received = input()
        if received == 'succeeded ' + command:
            return True
        elif received.startswith('failed ' + command):
            return False
        elif received.startswith('error ' + command):
            return False
            
def action(command, wait=True):
    print('start ' + command , flush=True)
    if wait==True:
        return check_for_success(command)
    else:
        return True
