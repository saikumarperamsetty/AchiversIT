import logging

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