#!/usr/bin/python

def dataStruct():
    shoplist = ['apple', 'mango', 'carrot', 'banana'];
    print('I have', len(shoplist),'items to purchase.');
    for item in shoplist:
        print(item,end=',');
    print();
    print('-'*10,'operations','-'*10);
    shoplist.append('rice');
    print(shoplist);
    shoplist.sort();
    print(shoplist);
    zoo = ('wolf', 'elephant', 'penguin');
    print('Number of animals in the zoo is', len(zoo));
    new_zoo = ('monkey', 'dolphin', zoo);
    print(new_zoo);
    print(new_zoo[1]);
    print(new_zoo[2]);
    print(new_zoo[2][0]);