import socket
import sys
import time

def get_ip_status(ip,port):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        client.connect((ip,port))
        print('--- {0} port {1} is open----'.format(ip, port))
    except Exception as err:
        # print(err)
        print('{0} port {1} is not open'.format(ip,port))
    finally:
        client.close()

if __name__ == "__main__":
    timer =  2 * 60
    ip = sys.argv[1]
    port = int(sys.argv[2])
    # print (ip, port)
    while True:
        get_ip_status(ip, port)
        time.sleep(timer)