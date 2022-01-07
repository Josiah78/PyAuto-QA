def HelloWorld(counter):
    if counter == 2:
        raise Exception('This is an error, counter is equal to 2')
    print('Hello World')

for i in range(0,3):
    try:
        HelloWorld(i)
        except Exception as err:
            print('We have encountered an error:' + str(err))