#!/home/maksim/etc/Python3.9/Python-3.9.0/python
import logging


logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')

def main():
    logging.info('Start..')
    name = 'Maksim'
    print(f'{name}')


if __name__=='__main__':
    main()
