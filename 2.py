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
            
            
            continue
        except:
            print('Prueba de nuevo')
        
if __name__ == '__main__':
    main()