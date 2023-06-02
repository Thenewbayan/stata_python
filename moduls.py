import text
import players


player_stata:list[dict[str:str]]=[]
path_in='input_data.txt'
path_out='data.txt'


def start_main_menu()->int:
    print(text.main_menu)
    while True: 
        select=input(text.select_menu)
        if select.isdigit() and 0<int(select)<7:
            return int(select)


def kpi(number:int)->float:
    with open(path_in, 'r') as file:
        data=file.readlines()
        for players in data:
            players=players.strip().split(',')
            new={'index':players[0], 'name':players[1], 'number':players[2], 'time':float(players[3]), 
                 'distance':float(players[4]), 'touch':float(players[5]), 'pass':float(players[6]), 
                 'succs_pass':float(players[7]), 'forward_pass':float(players[8]), 'shoots':float(players[9]), 
                 'shoots_on_target':float(players[10]), 'goal':float(players[11]), 'assist':float(players[12]), 
                 'max_speed':float(players[13]), 'block_shot':float(players[14]), 'head_duels_win':float(players[15]),
                'head_duels':float(players[16])}
            player_stata.append(new)
    stata=(player_stata[int(number)-1])
    stata_def=(stata.get('touch'))/(stata.get('time')+stata.get('head_duels_win')/stata.get('head_duels'))/2
    stata_attack=((stata.get('succs_pass')/stata.get('pass')+
                    stata.get('shoots_on_target')/stata.get('shoots')+
                    stata.get('goal')/stata.get('shoots_on_target')+
                    stata.get('assist')/stata.get('forward_pass')))/4
    stata_phisic=((stata.get('distance')/stata.get('time'))+stata.get('max_speed'))/2
    result=(stata_def+stata_attack+stata_phisic)
    return result


def select_player () -> int:
    numb=input(text.select_player)
    while True:
        if numb.isdigit():
            return numb
        
def create_player(Attack, Defence, Phisical):
    
