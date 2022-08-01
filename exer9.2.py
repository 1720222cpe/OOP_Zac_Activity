try:
    friends = {
        'Jen' : '42',
        'Dan' : '8',
        'Althea' : '2',
}
    print(friends.items())

    del friends['Althea']
    del friends['Dan']
    print(friends)

except:
    print('Sorry, Error')