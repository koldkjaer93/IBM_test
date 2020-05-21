# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:31:51 2020

@author: jonas
"""


import hashlib

commands = ['products', 'help', 'goodbye', 'weather', 'store']
describtion = ['Listing all our available products', 'Listing the accaptable commands', 'No further help is needed', 'Showing the weather at your current location', 'Displaying the store nearest you']
products = ['hammer', 'screwdriver']
hammers = ['https://plusshop.dk/draper-expert-stal-klofthammer?gclid=Cj0KCQjwzZj2BRDVARIsABs3l9I2TRmFwpgRVAG3qf5qrhAKyZVOgRY9ArZGuY1DTC-eWEhVOcCIKpUaAtx1EALw_wcB','https://www.thomann.de/dk/stairville_kupferhammer_250_gramm.htm?glp=1&gclid=Cj0KCQjwzZj2BRDVARIsABs3l9L_4p03gVJMLOdU4lPAlRsltbJJcewaomKVx1kmTSQpiYD6v05UUAcaAg4jEALw_wcB']
screwdriver = []
dictionary = {products[0]:hammers, products[1]:screwdriver}

ToDo = []
temperatur = 15
city = 'København'
pythonhashseed=(1337)




intro = input (f"Hello and welcome, what can i help you with? You can use the following commands: {commands} \n")
intro = intro.lower()

while True:
    
    if intro == 'products':
        product = input(f'I can help you with the following products: {list(dictionary.keys())}, let me know which you are looking for, and i will list the ones available \n')
        product = product.lower()
        
        if product in products:
            if len(dictionary[product]) == 0:
                print('No more products in stock \n')
            else:
                print(dictionary[product],'\n')
            intro = input('Anything else i can help you with, type \"help\", see the available products again type \"products\" \n')
        
        elif product == 'goodbye':
            break
        else:
            intro = input('Cant find the following product, type \"help\" to see what i can help you with and if you wanna see the available products again type \"products\" \n')
    
    
    elif intro == 'help':
        intro = input(f'You can use the following commands: \n {commands[0]}: {describtion[0]} \n {commands[1]}: {describtion[1]} \n {commands[2]}: {describtion[2]} \n {commands[3]}: {describtion[3]} \n {commands[4]}: {describtion[4]} \n' )
    
    
    elif intro == 'weather':
        intro = input(f'The current temperature is {temperatur} degrees celcius. Type \"help\" to see what else i can help with. \n\n')
    
    elif intro == 'configure':
        hashpass = hashlib.sha256()
        password = hashpass.update(bytes(input('Type in the correct password to proceed \n'),'utf8'))
        password = hashpass.hexdigest()
        if password == 'dc9e6e6dad5334b7069bf93f95642b87abcc1122a152cccac4340d9332c84e1a':
            options = input('You now have the following options:\n Add new product with the command \"add\" \n Delete product with the command \"delete\" \n Add link to specific product using \"links\" \n\n')
            if options == 'add':
                added = input('Type the name of the product(s) you want to add if you want to add more than one item separate with a \",\" : \n\n')
                dictionary[added] = []
                intro = input(f'You have now added the products, type a valid command to proceed: {commands}\n\n')
            elif options == 'delete':
                delete =  input('Type the name of the product you want to delete: \n')
                if delete in products: products.remove(delete)
                intro = input(f'You have now deleted the products, type a valid command to proceed: {commands}\n\n')
            elif options == 'links':
                productlink =  input(f'Type which product of {list(dictionary.keys())} which you want to add the link: \n')
                newlink = input('Now type the link you want to add \n')
                dictionary[productlink].append(newlink)
                intro = input(f'You have now added a link to the product, type a valid command to proceed: {commands}\n\n')
        else:
            intro = input(f'Password was incorrect, type \"configure\" to try again or \"help\" to see other options \n')
            
                   
    elif intro == 'store':
        intro = input(f'The store nearest you is in {city} at the adress: Kongens Nytorv 24, 1050 {city}. Type \"help\" to see what else i can help with \n\n')
        
    elif '?' in intro:
        ToDo.append(intro)
        intro = input(f'Did not understand the question but it has been added to my todo list, type \"help\" to see what else i can do for you \n\n')

        
    elif intro == 'goodbye':
        print('Happy to help, hope you got what you came for \n\n')
        break
        
    else: 
        intro = input('Did not understand your command, try to write \"help\" to see what commands you can use \n\n')
        
