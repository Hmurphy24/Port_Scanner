import socket
from datetime import datetime


def getting_user_input():

    while True:

        device = input('Type the IP address or name of the device that you want to scan: ')

        try:

            device_id = socket.gethostbyname(device)

            break

        except socket.gaierror:

            print('You entered an invalid IP or computer name.')

            print()

    while True:

        min_port = input('Enter the minimum port number to scan: ')

        if min_port.isdigit():

            min_port = int(min_port)

            break

        else:

            print('You typed in an invalid number!')

    while True:

        max_port = input('Enter the maximum port number to scan: ')

        if max_port.isdigit():

            if int(max_port) < int(min_port):

                print('Enter a number larger than ' + str(min_port) + '. Re-enter your inputs please.')

                print()

                getting_user_input()

            else:

                max_port = int(max_port)

            break

        else:

            print('You typed in an invalid number!')

    return device_id, min_port, max_port


def get_time():

    current_time = datetime.now()

    return current_time


def port_scan(ip, scan_start, scan_stop):

    try:
        for port in range(scan_start, scan_stop + 1):

            connect_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = connect_socket.connect_ex((ip, port))

            connect_socket.settimeout(1)

            if result == 0:

                print('Port {}: Open'.format(port))

            connect_socket.close()

    except socket.error:

        print('The program ran into an error.')

        if socket.herror:

            print('The program encountered an herror.')
            exit()

        elif socket.gaierror:

            print('The program encountered a gaierror.')
            exit()

        elif socket.timeout:

            print('The program encountered a timeout error.')
            exit()

        else:

            exit()


def main():

    ip_address = getting_user_input()

    print()
    print('Scanning ' + ip_address[0] + ' in progress.')
    print()

    start_time = get_time()

    port_scan(ip_address[0], ip_address[1], ip_address[2])

    end_time = get_time()

    time_diff = end_time - start_time

    print('It took you ' + str(time_diff) + ' to complete the scan.')


main()
