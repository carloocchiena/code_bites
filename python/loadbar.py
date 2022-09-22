import time


def load_bar():
    """Print a loadbar on the command line"""
    bar = ['█', '██', '███', '████', '█████', '██████', '      ']
    
    for i in range(len(bar)):
        print(f' Work in progress...{bar[i]}', end='\r')
        time.sleep(.5)

            
if __name__ == '__main__':
    while 1:
        load_bar()
        time.sleep(5)
        exit()
    
