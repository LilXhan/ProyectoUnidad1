import requests

def option_1_generations(): 
    
    request = requests.get(f'https://pokeapi.co/api/v2/generation/?limit=10')
    data = request.json()
    
    #prints all the generations
    for i in range(len(data['results'])): 
        print(data['results'][i]['name']) 
    
    continue_fun = True
    while continue_fun == True:
        try:     
            decision = input('Escribe el numero de la generacion que quieras: ')
            if decision == 'exit':
                continue_fun == False
                break
            else:
                decision = int(decision)
            
            decision -= 1
                
            ##prints the chosen generation
            data_i = data['results'][decision]['url'] 
            new_request = requests.get(f'{data_i}')
            generation_data = new_request.json()
            
            
            for i in range(len(generation_data['pokemon_species'])): # print all the pokemons from gen selected
                
                # print Name, Url Image, Abilities
                name = generation_data['pokemon_species'][i]['name']
                r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
                poke_data = r.json()
                name = poke_data['name']
                image = poke_data['sprites']['other']['official-artwork']['front_default']
                abilities = [i['ability']['name'] for i in poke_data['abilities']]  

                print(f'name: {name}')
                print(f'Image: {image}')
                print(f'ability: {abilities}')
                print('----------------------------------------------')
        
        except:
            print('error')


def option_2_shape():
    request = requests.get(f'https://pokeapi.co/api/v2/pokemon-shape/')
    data = request.json()
        
    for c, i in enumerate(data['results']):
        n = i['name']
        print(f'{c+1}) {n}')

    continue_fun = True
    while continue_fun == True:
        try:
            decision = input('Escribe el numero de habitat que quieres listar: ').lower()
            if decision == 'exit':
                continue_fun == False
                break
            
            url = f'https://pokeapi.co/api/v2/pokemon-shape/{decision}'
            res = requests.get(url)
            data23 = res.json()
            result1 = data23.get('pokemon_species',[])
            
            if result1:
                for i in result1:
                    namePoke = i['name']
                    url4 = f"https://pokeapi.co/api/v2/pokemon/{namePoke}"
                    res4 = requests.get(url4)
                    data4 = res4.json()
                    abilities = [i['ability']['name'] for i in data4['abilities']]
                    image = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{data4['id']}.png"
                    
                    print(f'name: {namePoke}')
                    print(f'ability: {abilities}')
                    print(f'Image: {image}')
                    print('-----------------------------------------')
            
        except:
            print('error')

def option_3_ability(): 
    #print abilities    
    r = 'https://pokeapi.co/api/v2/ability/'
    rq = requests.get(r)
    data = rq.json()
    for c, i in enumerate(data['results']):
        n = i['name']
        print(f'{c+1}) {n}')

    continue_fun = True
    while continue_fun == True:
        try:
            n_Ability= input('Escribe el nombre o el id de la habilidad, puedes usar estas habilidades como referencia: ').lower()
            if n_Ability == 'exit':
                continue_fun == False
                break
        
            url = f'https://pokeapi.co/api/v2/ability/{str(n_Ability)}'
            res = requests.get(url)
            data23 = res.json()
            result1 = data23.get('pokemon',[])
            if result1:
                for i in result1:
                    namePoke = i['pokemon']['name']
                    url4 = f"https://pokeapi.co/api/v2/pokemon/{namePoke}"
                    res4 = requests.get(url4)
                    data4 = res4.json()
                    image = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{data4['id']}.png"
                    abilities = [i['ability']['name'] for i in data4['abilities']]
                
                    print(f'name: {namePoke}')
                    print(f'Image: {image}')
                    print(f'ability: {abilities}')
                    print('-----------------------------------------')
            else:
                print("Esta es una habilidad no oficial en la serie")
        
        except:
            print('error')

def option_4_habitat(): 
    request = requests.get(f'https://pokeapi.co/api/v2/pokemon-habitat')
    data = request.json()
    # print habitatsdef option_4_habitat(): 
    request = requests.get(f'https://pokeapi.co/api/v2/pokemon-habitat')
    data = request.json()
    
    # print habitats
    for count,i in enumerate(data['results']):
        n = i['name']
        print(f'nÂ°: {count+1} Tipo: {n}')
    
    continue_fun = True
    while continue_fun == True:
        try:
            decision = input('Escribe el numero de habitat que quieres listar: ').lower()
            if decision == 'exit':
                continue_fun == False
                break
    
            # get the url from the habitat selected
            data_h = f'https://pokeapi.co/api/v2/pokemon-habitat/{decision}'
            r = requests.get(data_h)
            habitat_data = r.json()
            data322 = habitat_data.get('pokemon_species', [])
            
            if data322:
                for i in data322:
                    poke_name = i['name']
                    url4 = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
                    req4 = requests.get(url4)
                    d = req4.json()
                    image = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{d['id']}.png"
                    abilities = [i['ability']['name'] for i in d['abilities']] 

                    print(f'name: {poke_name}')
                    print(f'Image: {image}')
                    print(f'ability: {abilities}')
                    print('----------------------------------------------')

        except:
            print('error')       
            

def option_5_type(): 

    request = requests.get(f'https://pokeapi.co/api/v2/type')
    data = request.json()
    
    # print the types 
    for count,i in enumerate(data['results']):
        n = i['name']
        print(f'{count+1} Tipo: {n}')
    
    continue_fun = True
    while continue_fun == True:
        
        try: 
            #print('Aviso: No hay pokemones de tipo "unknown" y "shadow"')
            decision = input('Escribe el numero del TIPO de pokemon que quieres ver:').lower()
            if decision == 'exit':
                continue_fun == False
                break
            
            #print pokemon data. name, url, image
            url1 = f'https://pokeapi.co/api/v2/type/{decision}'
            req1 = requests.get(url1)
            d1 = req1.json()
            
            if len(d1['pokemon']) != 0:
                for i in d1['pokemon']:
                    poke_name = i['pokemon']['name']
                    url2 = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
                    req2 = requests.get(url2)
                    d2 = req2.json()
                    
                    # get image 
                    image = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{d2['id']}.png"
                    abilities = [i['ability']['name'] for i in d2['abilities']]
                    
                    print(f'name: {poke_name}')
                    print(f'Image: {image}')
                    print(f'ability: {abilities}')
                    print('----------------------------------------------')
            
            else:
                print(f'no hay pokemones del tipo escogido')
            
        except:
            print('error')
    for count,i in enumerate(data['results']):
        n = i['name']
        print(f'nÂ°: {count+1} Tipo: {n}')
    
    continue_fun = True
    while continue_fun == True:
        try:
            decision = input('Escribe el numero de habitat que quieres listar: ').lower()
            if decision == 'exit':
                continue_fun == False
                break
    
            # get the url from the habitat selected
            data_h = f'https://pokeapi.co/api/v2/pokemon-habitat/{decision}'
            r = requests.get(data_h)
            habitat_data = r.json()
            data322 = habitat_data.get('pokemon_species', [])
            
            if data322:
                for i in data322:
                    poke_name = i['name']
                    url4 = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
                    req4 = requests.get(url4)
                    d = req4.json()
                    image = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{d['id']}.png"
                    abilities = [i['ability']['name'] for i in d['abilities']] 

                    print(f'name: {poke_name}')
                    print(f'Image: {image}')
                    print(f'ability: {abilities}')
                    print('----------------------------------------------')

        except:
            print('error')       
            
def option_5_type(): 

    request = requests.get(f'https://pokeapi.co/api/v2/type')
    data = request.json()
    
    # print the types 
    for count,i in enumerate(data['results']):
        n = i['name']
        print(f'{count+1} Tipo: {n}')
    
    continue_fun = True
    while continue_fun == True:
        
        try: 
            #print('Aviso: No hay pokemones de tipo "unknown" y "shadow"')
            decision = input('Escribe el numero del TIPO de pokemon que quieres ver:').lower()
            if decision == 'exit':
                continue_fun == False
                break
            
            #print pokemon data. name, url, image
            url1 = f'https://pokeapi.co/api/v2/type/{decision}'
            req1 = requests.get(url1)
            d1 = req1.json()
            
            if len(d1['pokemon']) != 0:
                for i in d1['pokemon']:
                    poke_name = i['pokemon']['name']
                    url2 = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
                    req2 = requests.get(url2)
                    d2 = req2.json()
                    
                    # get image 
                    image = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{d2['id']}.png"
                    abilities = [i['ability']['name'] for i in d2['abilities']]
                    
                    print(f'name: {poke_name}')
                    print(f'Image: {image}')
                    print(f'ability: {abilities}')
                    print('----------------------------------------------')
            
            else:
                print(f'no hay pokemones del tipo escogido')
            
        except:
            print('error')

def main():
    
    while True:
        try:
            print('Hola!. Tienes 5 opciones para escoger')
            print('Opcion 1: Listar los pokemones por generacion.')
            print('Opcion 2: Listar pokemones por forma')
            print('Opcion 3: Listar pokemones por habilidad')
            print('Opcion 4: Listar pokemones por habitat')
            print('Opcion 5: Listar pokemones por tipo')
            opcion_escogida = input('Ingresa el numero de que opcion quieres: ')
            
            if opcion_escogida == '1':
                option_1_generations()
            elif opcion_escogida == '2':
                option_2_shape()    
            elif opcion_escogida == '3':
                option_3_ability()
            elif opcion_escogida == '4':
                option_4_habitat()
            elif opcion_escogida == '5':
                option_5_type()
            elif opcion_escogida == 'exit':
                break                 
            
            continue
        except:
            print('Prueba de nuevo')

        
if __name__ == '__main__':
    main()