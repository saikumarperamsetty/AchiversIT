import logging

#Ex:1
logging.basicConfig(level=logging.DEBUG, filename='loginfo.txt',format='%(asctime)s %(message)s')
print('DEBUG.')
logging.debug('Its DEBUG message.')
print('INFO..')
logging.info('Its INFO message..')
print('WARNING...')
logging.warning('Its WARNING message...')
print('ERROR....')
logging.error('its a ERROR message....')
print('CRITICAL.....')
logging.critical('its CRITICAL message.....')

Ex:2
logging.basicConfig(filename="abc.txt",
                    format='%(asctime)s %(levelname)s-%(message)s'
                    )
for i in range(0,15):
    if(i%2==0):
        logging.warning('log warning message')
    elif(i%3==0):
        logging.critical('log critical message')
    else:
        logging.error('log error message')