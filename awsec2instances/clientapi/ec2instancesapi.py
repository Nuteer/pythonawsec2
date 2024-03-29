#!/usr/bin/python
# -*- coding: utf-8 -*-
# ec2instances.py
# It is an example of how to handle AWS EC2 instances.
# It uses Client API (low-level) of Boto3.

import sys
import awshelperapi

def print_menu():
    print('\nMENU')
    print('0 = Quit')
    print('1 = Describe all instances')
    print('2 = Run new instance')
    print('3 = Describe instance')
    print('4 = Start instance')
    print('5 = Stop instance')
    print('6 = Reboot instance')
    print('7 = Terminate instance')
    return


def main():
    instance_id = ''
    option = -1

    while option != 0:
        print_menu()
        try:
            option = int(input('\nEnter an option? '))
            if option == 0:
                print('Bye')
            elif option == 1:
                awshelperapi.describe_instances()
            elif option == 2:
                instance_id = awshelperapi.run_instance()
            elif option == 3:
                awshelperapi.describe_instance(instance_id)
            elif option == 4:
                awshelperapi.start_instance(instance_id)
            elif option == 5:
                awshelperapi.stop_instance(instance_id)
            elif option == 6:
                awshelperapi.reboot_instance(instance_id)
            elif option == 7:
                awshelperapi.terminate_instance(instance_id)
            else:
                print('\nERROR: Enter a valid option!!')
        except ValueError:
            print('\nERROR: Enter a valid option!!')

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
