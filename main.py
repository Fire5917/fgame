import random, os, time, colorama
web_app = input("Are you in the web app (replit) (y/n) ? >>> ").lower()
colorama.init()
def pub():
    global number_of_pub_watch
    global os_is_working
    try:
        if web_app != 'y':
            os.system('start https://link-target.net/534967/fire-game-open-chest')
        print("Link : https://link-target.net/534967/fire-game-open-chest")
    except:
        print("Link : https://link-target.net/534967/fire-game-open-chest")
    number_of_pub_watch += 1
affichage = f"""{colorama.Fore.RED}
    ______                         
   / ____/___ _____ _____ ___  ___ 
  / /_  / __ `/ __ `/ __ `__ \/ _ \\
 / __/ / /_/ / /_/ / / / / / /  __/         
/_/    \__, /\__,_/_/ /_/ /_/\___/ 
      /____/  {colorama.Fore.GREEN}By {colorama.Fore.LIGHTRED_EX}F{colorama.Fore.RED}I{colorama.Fore.LIGHTRED_EX}R{colorama.Fore.RED}E{colorama.Fore.LIGHTRED_EX}5{colorama.Fore.RED}9{colorama.Fore.LIGHTRED_EX}1{colorama.Fore.RED}7  

{colorama.Fore.YELLOW}https://replit.com/@Fire59/fgame 
{colorama.Fore.RED}Derniers ajout : shop (19/11/2022)     
      {colorama.Fore.WHITE}                 
"""
number_of_pub_watch = 0
money = 0
arena = 1
lvl_common = 0
avancement_common = 0
base_life_common = 100
base_attack_common = 100
next_level_base_common = 16
lvl_rare = 0
avancement_rare = 0
base_life_rare = 150
base_attack_rare = 150
next_level_base_rare = 8
lvl_epic = 0
avancement_epic = 0
base_life_epic = 200
base_attack_epic = 200
next_level_base_epic = 4
lvl_legendary = 0
avancement_legendary = 0
base_life_legendary = 250
base_attack_legendary = 250
next_level_base_legendary = 2
lvl_mythic = 0
avancement_mythic = 0
base_life_mythic = 350
base_attack_mythic = 350
next_level_base_mythic = 1
number_of_boosts = 0
nxt_lvl_mythic = next_level_base_mythic * lvl_mythic
nxt_lvl_common = next_level_base_common * lvl_common
nxt_lvl_rare = next_level_base_rare * lvl_rare
nxt_lvl_epic = next_level_base_epic * lvl_epic
nxt_lvl_legendary = next_level_base_legendary * lvl_legendary
stars = 0
victory_number = 0
tie_number = 0
defeat_number = 0
number_of_battle = 0
quete = {
    "avancement" : {
        "arena7" : arena,
        "common_lvl_5" : lvl_common,
        "arena5" : arena,
        "pub5" : number_of_pub_watch,
        "pub10" : number_of_pub_watch,
        "tie" : tie_number
    },
    "avancement_final" : {
        "arena7" : 7,
        "common_lvl_5" : 5,
        "arena5" : 5,
        "pub5" : 5,
        "pub10" : 10,
        "tie" : 1
    },
    "already_done" : {
        "arena7" : False,
        "common_lvl_5" : False,
        "arena5" : False,
        "pub5" : False,
        "pub10" : False,
        "tie" : False
    }
}
def quests():
    global quete
    global lvl_mythic
    global lvl_common
    global lvl_legendary
    global lvl_epic
    global tie_number
    quete["avancement"]["arena7"] = arena
    quete["avancement"]["common_lvl_5"] = lvl_common
    quete["avancement"]["arena5"] = arena
    quete["avancement"]["pub5"] = number_of_pub_watch
    quete["avancement"]["pub10"] = number_of_pub_watch
    quete["avancement"]["tie"] = tie_number
    if quete["avancement"]["arena7"] >= quete["avancement_final"]["arena7"] and quete["already_done"]["arena7"] == False:
        quete["already_done"]["arena7"] = True
        print(f"{colorama.Fore.YELLOW}Qu??te arena7 termin?? ! ")
        print(f"{colorama.Fore.MAGENTA}Vous avez gagner 1 mythic")
        print(f"{colorama.Fore.MAGENTA}Mythic lvl : {colorama.Fore.LIGHTBLUE_EX}{lvl_mythic} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{lvl_mythic + 1}")
        lvl_mythic += 1
    if quete["avancement"]["common_lvl_5"] >= quete["avancement_final"]["common_lvl_5"] and quete["already_done"]["common_lvl_5"] == False:
        quete["already_done"]["common_lvl_5"] = True
        print(f"{colorama.Fore.YELLOW}Qu??te common lvl 5 termin?? ! ")
        print(f"{colorama.Fore.GREEN}Vous avez gagner 1 lvl common")
        print(f'{colorama.Fore.LIGHTGREEN_EX}Common lvl : {colorama.Fore.LIGHTBLUE_EX}{lvl_common} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{lvl_common + 1}')
        lvl_common += 1
    if quete["avancement"]["arena5"] >= quete["avancement_final"]["arena5"] and quete["already_done"]["arena5"] == False:
        quete["already_done"]["arena5"] = True
        print(f"{colorama.Fore.YELLOW}Qu??te arena5 termin?? ! ")
        print(f"{colorama.Fore.YELLOW}Vous avez gagner 1 lvl legendary")
        print(f'{colorama.Fore.YELLOW}Legendary lvl : {colorama.Fore.LIGHTBLUE_EX}{lvl_legendary} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{lvl_legendary + 1}')
        lvl_legendary += 1
    if quete["avancement"]["pub5"] >= quete["avancement_final"]["pub5"] and quete["already_done"]["pub5"] == False:
        quete["already_done"]["pub5"] = True
        print(f"{colorama.Fore.YELLOW}Qu??te visioneur de pub I termin?? ! ")
        print(f"{colorama.Fore.GREEN}Vous avez gagner 2 coffres")
        get_chest(arena)
        get_chest(arena)
    if quete["avancement"]["pub10"] >= quete["avancement_final"]["pub10"] and quete["already_done"]["pub10"] == False:
        quete["already_done"]["pub10"] = True
        print(f"{colorama.Fore.YELLOW}Qu??te visioneur de pub II termin?? ! ")
        print(f"{colorama.Fore.GREEN}Vous avez gagner 5 coffres")
        for i in range(5): get_chest(arena)
    if quete["avancement"]["tie"] >= quete["avancement_final"]["tie"] and quete["already_done"]["tie"] == False:
        quete["already_done"]["tie"] = True
        print(f"{colorama.Fore.YELLOW}Qu??te ??galit?? termin?? ! ")
        print(f"{colorama.Fore.LIGHTMAGENTA_EX}Vous avez gagner 1 lvl epic")
        print(f'{colorama.Fore.LIGHTMAGENTA_EX}Epic lvl : {colorama.Fore.LIGHTBLUE_EX}{lvl_epic} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{lvl_epic + 1}')
        lvl_epic += 1
def get_chest(arena):
    global money
    global lvl_common
    global avancement_common
    global base_life_common
    global base_attack_common
    global next_level_base_common
    global lvl_rare
    global avancement_rare
    global base_life_rare
    global base_attack_rare
    global next_level_base_rare
    global lvl_mythic
    global avancement_mythic
    global base_life_mythic
    global base_attack_mythic
    global next_level_base_mythic
    global lvl_epic
    global avancement_epic
    global base_life_epic
    global base_attack_epic
    global next_level_base_epic
    global lvl_legendary
    global avancement_legendary
    global base_life_legendary
    global base_attack_legendary
    global next_level_base_legendary
    global nxt_lvl_common
    global nxt_lvl_epic
    global nxt_lvl_rare
    global nxt_lvl_legendary
    global nxt_lvl_mythic
    nxt_lvl_common = next_level_base_common * lvl_common
    nxt_lvl_rare = next_level_base_rare * lvl_rare
    nxt_lvl_epic = next_level_base_epic * lvl_epic
    nxt_lvl_legendary = next_level_base_legendary * lvl_legendary
    random_number = random.randint(1,100)
    random_money = random.randint(50,150)
    print(f"{colorama.Fore.YELLOW}Vous avez obtenu {random_money}$ dans ce coffre ! ")
    money += random_money
    if random_number >= 97 and arena >= 7:
        card_rarity = 'mythic'
        print(f"{colorama.Fore.MAGENTA}Vous avez obtenu {arena} {card_rarity}")
        if lvl_mythic == 0:
            print(f"{colorama.Fore.MAGENTA}Mythic lvl : {colorama.Fore.LIGHTBLUE_EX}{lvl_mythic} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{lvl_mythic + 1}")
            lvl_mythic = 1
        else:
            avancement_mythic = avancement_mythic + arena
            if avancement_mythic >= nxt_lvl_mythic:
                while avancement_mythic >= nxt_lvl_mythic:
                    avancement_mythic = avancement_mythic - nxt_lvl_mythic
                    print(f'{colorama.Fore.MAGENTA}Mythic lvl : {colorama.Fore.LIGHTBLUE_EX}{lvl_mythic} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{lvl_mythic + 1}')
                    lvl_mythic += 1
                    nxt_lvl_mythic = next_level_base_mythic * lvl_mythic
            else:
                print(f'{colorama.Fore.MAGENTA}Mythic {colorama.Fore.RED}>>> {colorama.Fore.YELLOW}Avancement pour mont?? de niveau : {colorama.Fore.GREEN}{avancement_mythic}{colorama.Fore.RED}/{colorama.Fore.MAGENTA}{nxt_lvl_mythic}')
    elif random_number > 90:
        card_rarity = 'legendary'
        print(f"{colorama.Fore.YELLOW}Vous avez obtenu {arena} {card_rarity}")
        if lvl_legendary == 0:
            print(f'{colorama.Fore.YELLOW}Legendary lvl : {colorama.Fore.LIGHTBLUE_EX}{lvl_legendary} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{lvl_legendary + 1}')
            lvl_legendary = 1
        else:
            avancement_legendary = avancement_legendary + arena
            if avancement_legendary >= nxt_lvl_legendary:
                while avancement_legendary >= nxt_lvl_legendary:
                    avancement_legendary = avancement_legendary - nxt_lvl_legendary
                    print(f'{colorama.Fore.YELLOW}Legendary lvl : {colorama.Fore.LIGHTBLUE_EX}{lvl_legendary} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{lvl_legendary + 1}')
                    lvl_legendary += 1
                    nxt_lvl_legendary = next_level_base_legendary * lvl_legendary
            else:
                print(f'{colorama.Fore.YELLOW}Legendary {colorama.Fore.RED}>>> {colorama.Fore.YELLOW}Avancement pour mont?? de niveau : {colorama.Fore.GREEN}{avancement_legendary}{colorama.Fore.RED}/{colorama.Fore.MAGENTA}{nxt_lvl_legendary}')
    elif random_number > 75:
        card_rarity = 'epic'
        print(f"{colorama.Fore.LIGHTMAGENTA_EX}Vous avez obtenu {arena} {card_rarity}")
        if lvl_epic == 0:
            print(f'{colorama.Fore.LIGHTMAGENTA_EX}Epic lvl : {colorama.Fore.LIGHTBLUE_EX}{lvl_epic} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{lvl_epic + 1}')
            lvl_epic = 1
        else:
            avancement_epic = avancement_epic + arena
            if avancement_epic >= nxt_lvl_epic:
                while avancement_epic >= nxt_lvl_epic:
                    avancement_epic = avancement_epic - nxt_lvl_epic
                    print(f'{colorama.Fore.LIGHTMAGENTA_EX}Epic lvl : {colorama.Fore.LIGHTBLUE_EX}{lvl_epic} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{lvl_epic + 1}')
                    lvl_epic += 1
                    nxt_lvl_epic = next_level_base_epic * lvl_epic
            else:
                print(f'{colorama.Fore.LIGHTMAGENTA_EX}Epic {colorama.Fore.RED}>>> {colorama.Fore.YELLOW}Avancement pour mont?? de niveau : {colorama.Fore.GREEN}{avancement_epic}{colorama.Fore.RED}/{colorama.Fore.MAGENTA}{nxt_lvl_epic}')
    elif random_number > 50:
        card_rarity = 'rare'
        print(f"{colorama.Fore.LIGHTRED_EX}Vous avez obtenu {arena} {card_rarity}")
        if lvl_rare == 0:
            print(f'{colorama.Fore.LIGHTRED_EX}Rare lvl : {colorama.Fore.LIGHTBLUE_EX}{lvl_rare} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{lvl_rare + 1}')
            lvl_rare = 1
        else:
            avancement_rare = avancement_rare + arena
            if avancement_rare >= nxt_lvl_rare:
                while avancement_rare >= nxt_lvl_rare:
                    avancement_rare = avancement_rare - nxt_lvl_rare
                    print(f'{colorama.Fore.LIGHTRED_EX}Rare lvl : {colorama.Fore.LIGHTBLUE_EX}{lvl_rare} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{lvl_rare + 1}')
                    lvl_rare += 1
                    nxt_lvl_rare = next_level_base_rare * lvl_rare
            else:
                print(f'{colorama.Fore.LIGHTRED_EX}Rare {colorama.Fore.RED}>>> {colorama.Fore.YELLOW}Avancement pour mont?? de niveau : {colorama.Fore.GREEN}{avancement_rare}{colorama.Fore.RED}/{colorama.Fore.MAGENTA}{nxt_lvl_rare}')
    elif random_number > 0:
        card_rarity = 'common'
        print(f"{colorama.Fore.LIGHTGREEN_EX}Vous avez obtenu {arena} {card_rarity}")
        if lvl_common == 0:
            print(f'{colorama.Fore.LIGHTGREEN_EX}Common lvl : {colorama.Fore.LIGHTBLUE_EX}{lvl_common} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{lvl_common + 1}')
            lvl_common = 1
        else:
            avancement_common = avancement_common + arena
            if avancement_common >= nxt_lvl_common:
                while avancement_common >= nxt_lvl_common:
                    avancement_common = avancement_common - nxt_lvl_common
                    print(f'{colorama.Fore.LIGHTGREEN_EX}Common lvl : {colorama.Fore.LIGHTBLUE_EX}{lvl_common} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{lvl_common + 1}')
                    lvl_common += 1
                    nxt_lvl_common = next_level_base_common * lvl_common
            else:
                print(f'{colorama.Fore.LIGHTGREEN_EX}Common {colorama.Fore.RED}>>> {colorama.Fore.YELLOW}Avancement pour mont?? de niveau : {colorama.Fore.GREEN}{avancement_common}{colorama.Fore.RED}/{colorama.Fore.MAGENTA}{nxt_lvl_common}')
    print(f'{colorama.Fore.WHITE}')
def get_arena():
    global arena
    global stars
    backup_arena = arena
    arena = int((stars/100)+1)
    if backup_arena != arena:
        print(f"{colorama.Fore.CYAN}Changement d'arene : {colorama.Fore.LIGHTBLUE_EX}{backup_arena} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{arena}")
        print(f"{colorama.Fore.CYAN}Nombre de cartes par coffre : {colorama.Fore.YELLOW}{arena}{colorama.Fore.WHITE}")
def get_puissance():
    global puissance
    puissance = (base_attack_common + base_life_common)* lvl_common + (base_life_epic + base_attack_epic)* lvl_epic + (base_attack_legendary + base_life_legendary)*lvl_legendary + (base_attack_rare + base_life_rare)*lvl_rare + (base_attack_mythic + base_life_mythic)*lvl_mythic
def get_puissance_adversaire():
    get_puissance()
    global puissance_adversaire
    puissance_adversaire_middle = int((stars * 5)+(puissance/3))
    puissance_adversaire = random.randint(puissance_adversaire_middle-50, puissance_adversaire_middle+50)
    if puissance_adversaire < 0:
        puissance_adversaire = 0
def battle(puissance, puissance_adversaire):
    global number_of_boosts
    global stars
    global victory
    global defeat_number
    global tie_number
    if number_of_boosts >= 1:
        print("Utilisation de 1 boost")
        print("Votre puissance est augment??e de 30%")
        puissance_backup = puissance
        puissance = puissance * 1.3
        print(f"Votre puissance passe de {puissance_backup} ?? {puissance}")
        number_of_boosts -= 1
        print(f"Il vous reste {number_of_boosts} boosts")
    print(f'{colorama.Fore.CYAN}Votre puissance actuel : {colorama.Fore.YELLOW}{puissance}')
    print(f"{colorama.Fore.CYAN}Puissance de votre adversaire : {colorama.Fore.YELLOW}{puissance_adversaire}")
    if puissance > puissance_adversaire:
        print(f'{colorama.Fore.GREEN}Vous avez gagner car {colorama.Fore.LIGHTRED_EX}{puissance} {colorama.Fore.MAGENTA}> {colorama.Fore.RED}{puissance_adversaire}')
        stars_to_add = random.randint(12, 20)
        backup_stars = stars
        stars = stars + stars_to_add
        print(f"{colorama.Fore.CYAN}Vos ??toiles : {colorama.Fore.LIGHTBLUE_EX}{backup_stars} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{stars}   {colorama.Fore.YELLOW}(+{stars_to_add} ??toiles)")
        victory = True
    elif puissance == puissance_adversaire:
        print(f'{colorama.Fore.CYAN}Egalit?? car {colorama.Fore.LIGHTRED_EX}{puissance_adversaire} {colorama.Fore.MAGENTA}= {colorama.Fore.RED}{puissance}')
        print(f"{colorama.Fore.CYAN}Aucun changement d'??toiles")
        victory = False
        tie_number += 1
    else:
        print(f'{colorama.Fore.RED}Vous avez perdu car {colorama.Fore.LIGHTRED_EX}{puissance} {colorama.Fore.MAGENTA}<  {colorama.Fore.RED}{puissance_adversaire}')
        stars_to_remove = random.randint(10,15)
        backup_stars = stars
        stars = stars - stars_to_remove
        if stars < 0:
            stars = 0
        print(f'{colorama.Fore.CYAN}Vos ??toiles : {colorama.Fore.LIGHTBLUE_EX}{backup_stars} {colorama.Fore.RED}--> {colorama.Fore.BLUE}{stars}   {colorama.Fore.YELLOW}(-{stars_to_remove} ??toiles)')
        victory = False
        defeat_number += 1
while True:
    input("Appuyez sur entr??e pour continuer...")
    for i in range(10):
        print("\n\n\n\n\n")
    print(affichage)
    print('''
Actions dispos
[1] >>> Regarder une pub et ouvrir un coffre 
[2] >>> Voir vos stats
[3] >>> Faire un combat (-30$)
[4] >>> Lancer la version en ligne (replit)
[5] >>> Voir les qu??tes
[6] >>> Ouvrir le shop
    ''')
    choice = int(input("Veuillez entrer ce que vous voulez faire >>> "))
    if choice == 1:
        pub()
        x = 10
        for i in range(10):
            print(f"Temps restant : {x} sec")
            x -= 1
            time.sleep(1.0)
        get_chest(arena)
    if choice == 2:
        if arena < 7:
            mythic_already = " < ! > [D??blocable ar??ne 7] < ! >"
        if arena >= 7:
            mythic_already = ''
        get_puissance()
        nxt_lvl_common = next_level_base_common * lvl_common
        nxt_lvl_rare = next_level_base_rare * lvl_rare
        nxt_lvl_epic = next_level_base_epic * lvl_epic
        nxt_lvl_legendary = next_level_base_legendary * lvl_legendary
        if number_of_battle > 0:
            percentage_of_victory = int((victory_number / number_of_battle) * 100)
            percentage_of_tie = int((tie_number/number_of_battle) * 100)
            percentage_of_defeat = int((defeat_number/number_of_battle)*100)
        if number_of_battle == 0:
            percentage_of_victory = "Unknown"
            percentage_of_tie = "Unknown"
            percentage_of_defeat = "Unknown"
        print(f"""
{colorama.Fore.YELLOW}Common lvl       {colorama.Fore.RED}: {colorama.Fore.YELLOW}{lvl_common}     {colorama.Fore.RED}| {colorama.Fore.MAGENTA}Avancement : {colorama.Fore.YELLOW}{avancement_common}{colorama.Fore.RED}/{colorama.Fore.MAGENTA}{nxt_lvl_common}
{colorama.Fore.YELLOW}Rare lvl         {colorama.Fore.RED}: {colorama.Fore.YELLOW}{lvl_rare}     {colorama.Fore.RED}| {colorama.Fore.MAGENTA}Avancement : {colorama.Fore.YELLOW}{avancement_rare}{colorama.Fore.RED}/{colorama.Fore.MAGENTA}{nxt_lvl_rare}
{colorama.Fore.YELLOW}Epic lvl         {colorama.Fore.RED}: {colorama.Fore.YELLOW}{lvl_epic}     {colorama.Fore.RED}| {colorama.Fore.MAGENTA}Avancement : {colorama.Fore.YELLOW}{avancement_epic}{colorama.Fore.RED}/{colorama.Fore.MAGENTA}{nxt_lvl_epic}
{colorama.Fore.LIGHTRED_EX}Legendary lvl    {colorama.Fore.RED}: {colorama.Fore.YELLOW}{lvl_legendary}     {colorama.Fore.RED}| {colorama.Fore.MAGENTA}Avancement : {colorama.Fore.YELLOW}{avancement_legendary}{colorama.Fore.RED}/{colorama.Fore.MAGENTA}{nxt_lvl_legendary}
{colorama.Fore.LIGHTRED_EX}Mythic lvl       {colorama.Fore.RED}: {colorama.Fore.YELLOW}{lvl_mythic}     {colorama.Fore.RED}| {colorama.Fore.MAGENTA}Avancement : {colorama.Fore.YELLOW}{avancement_mythic}{colorama.Fore.RED}/{colorama.Fore.MAGENTA}{nxt_lvl_mythic}  {colorama.Fore.RED}{mythic_already}
{colorama.Fore.RED}Puissance totale : {colorama.Fore.YELLOW}{puissance}
{colorama.Fore.MAGENTA}-----------------------------------------------------------------------------------------        
{colorama.Fore.CYAN}Arene   {colorama.Fore.RED}: {colorama.Fore.YELLOW}{arena}       {colorama.Fore.RED}| {colorama.Fore.CYAN}Nombre de victoire {colorama.Fore.RED}: {colorama.Fore.YELLOW}{victory_number}     {colorama.Fore.RED}| {colorama.Fore.CYAN}Nombre d'??galit??s {colorama.Fore.RED}: {colorama.Fore.YELLOW}{tie_number}
{colorama.Fore.CYAN}Etoiles {colorama.Fore.RED}: {colorama.Fore.YELLOW}{stars}     {colorama.Fore.RED}| {colorama.Fore.CYAN}Nombre de d??faites {colorama.Fore.RED}: {colorama.Fore.YELLOW}{defeat_number}     {colorama.Fore.RED}| {colorama.Fore.CYAN}Nombre de combats {colorama.Fore.RED}: {colorama.Fore.YELLOW}{number_of_battle}
{colorama.Fore.CYAN}Argent  {colorama.Fore.RED}: {colorama.Fore.YELLOW}{money}$
{colorama.Fore.CYAN}Pourcentage de victoire {colorama.Fore.RED}: {colorama.Fore.YELLOW}{percentage_of_victory}%
{colorama.Fore.CYAN}Pourcentage de d??faite  {colorama.Fore.RED}: {colorama.Fore.YELLOW}{percentage_of_defeat}%
{colorama.Fore.CYAN}Pourcentage d'??galit??   {colorama.Fore.RED}: {colorama.Fore.YELLOW}{percentage_of_tie}%    
{colorama.Fore.WHITE}        
        """)
    if choice == 3 and money >= 30:
        money -= 30
        print(f"{colorama.Fore.LIGHTBLUE_EX}Il vous reste {money}$")
        number_of_battle += 1
        get_puissance()
        get_puissance_adversaire()
        battle(puissance, puissance_adversaire)
        get_arena()
        if victory == True:
            time.sleep(2.0)
            print(f"{colorama.Fore.GREEN}Vous avez gagner un coffre car vous avez gagner")
            time.sleep(1.0)
            get_chest(arena)
            victory_number += 1
        if victory == False:
            time.sleep(2.0)
            print(f"{colorama.Fore.RED}Vous n'avez pas gagner de coffre car vous n'avez pas gagner{colorama.Fore.WHITE}")
            time.sleep(1.0)
    elif choice == 3 and money < 30:
        print(f"{colorama.Fore.RED}Il vous manque {30-money}$ pour participer ?? un combat...")
    if choice == 4:
        if web_app == 'y':
            print(f"{colorama.Fore.RED}Vous ??tes d??j?? sur la version en ligne... {colorama.Fore.WHITE}")
        else:
            print(f"{colorama.Fore.GREEN}Lancement en cours...")
            os.system('start https://replit.com/@Fire5917/fgame')
            print(f"Lancement effectu?? ! {colorama.Fore.WHITE}")
    if choice == 5:
        print(f"""{colorama.Fore.YELLOW} 
Qu??tes : 
{colorama.Fore.BLUE}
- Arena7              | Arriver ?? l'ar??ne 7
    R??compense : 1 mythic
    D??j?? fait : {quete['already_done']["arena7"]}
{colorama.Fore.CYAN}
- Common lvl 5        | Avoir un niveau common sup??rieur ou ??gal ?? 5     
    R??compense : +1 lvl common        
    D??j?? fait : {quete['already_done']['common_lvl_5']} 
{colorama.Fore.BLUE}
- Arena5              | Arriver ?? l'ar??ne 5
    R??compense : +1 lvl legendary
    D??j?? fait : {quete['already_done']["arena5"]}     
{colorama.Fore.CYAN}
- Visioneur de pub I  | Regarder 5 pubs  
    R??compense : +2 coffres
    D??j?? fait : {quete['already_done']["pub5"]}
{colorama.Fore.BLUE}
- Visioneur de pub II | Regarder 10 pubs
    R??compense : +5 coffres
    D??j?? fait : {quete['already_done']["pub10"]}
{colorama.Fore.CYAN}
- Egalit??             | Faire une ??galit?? en combat
    R??compense : +1 lvl epic
    D??j?? fait : {quete['already_done']['tie']}
{colorama.Fore.WHITE}           
        """)
    if choice == 6:
        article = {}
        article99 = {"price" : 0, "name": "rien", "desc" : "rien acheter"}
        article1 = {"price" : 125, "name" : "coffre", "desc" : "Obtenir des coffres de son ar??ne actuel"}
        article2 = {"price" : 200, "name": "Boost de puissance", "desc" : "Permet d'avoir +30% de puissance pour son prochain combat"}
        print(f"""{colorama.Fore.YELLOW}
Argent : {money}$
         Shop - Articles Disposnibles:
[01] >>> Coffres                                  | Prix unitaire : 125$    
[02] >>> Boost de puissance (+30% pour 1 combat)  | Prix unitaire : 200$  
        """)
        shopchoice = int(input("Veuillez rentrer le num??ro de l'article que vous d??sirez acheter (99 pour sortir) >>> "))
        if shopchoice == 99:
            article = article99
        if shopchoice == 1:
            article = article1
        if shopchoice == 2:
            article = article2
        numbers_of_items = int(input("Combien de " + article["name"] + " voulez vous acheter ? >>> "))
        price = article["price"] * numbers_of_items
        if price > money:
            print(f"{colorama.Fore.RED}Vous n'avez pas assez d'argent...")
        else:
            print(f"{colorama.Fore.YELLOW}Etes vous sur de vouloir acheter {numbers_of_items} {article['name']} pour {price} ? {colorama.Fore.WHITE}")
            sur = input("(y/n) >>> ").lower()
            if sur == 'y':
                money -= price
                print(f"Il vous reste maintenant {money}$")
                print(f"""{colorama.Fore.WHITE}
R??capitulatif:
Achat de :
    -{article['name']} * {numbers_of_items}
        Descritption de l'article : {article['desc']}

Prix:
    Prix unitaire : {article['price']}
    Prix total : {price}
                """)
                if shopchoice == 1:
                    for i in range(numbers_of_items):
                        get_chest(arena)
                if shopchoice == 2:
                    number_of_boosts += numbers_of_items
        
    if choice == 99:
        print("Mode Triche activ??")
        print("""
        OPTIONS :
        [01] >>> Changer d'arene
        [02] >>> Changer son nombre d'??toiles
        [03] >>> Se give des coffres 
        [04] >>> Se give des ??galit??s
        [05] >>> Se give des victoires
        [06] >>> Se give des d??faites""")
        choice = int(input("Veuillez entrer le num??ro de l'option voulu >>> "))
        if choice == 1:
            arena = int(input("A quelle arene voulez vous ??tre ?"))
        if choice == 2:
            stars = int(input("Combien d'??toiles voulez vous ? "))
        if choice == 3:
            number_of_chests = int(input("Combien de coffres voulez vous ouvrir ? >>> "))
            arene_of_chests = int(input("De quelle arenes doivent ??tre les coffres ? >>> "))
            for i in range(number_of_chests):
                get_chest(arene_of_chests)
        if choice == 4:
            tie_to_add = int(input("Combien d'??galit??s voulez vous vous ajouter ? >>> "))
            tie_number = tie_to_add + tie_number
            number_of_battle += tie_to_add
        if choice == 5:
            victory_to_add = int(input("Combien de victoires voulez vous avoir en plus? >>> "))
            victory_number += victory_to_add
            number_of_battle += victory_to_add
        if choice == 6:
            defeat_to_add = int(input("Combien de d??faites voulez vous rajouter ? >>> "))
            defeat_number += defeat_to_add
            number_of_battle += defeat_to_add
    get_puissance
    try:
        if web_app != 'y':
            os.system(f'title puissance = {puissance}  -  arene = {arena}  - ??toiles = {stars}')
    except:
        if web_app != 'y':
            os.system(f'title arene = {arena}  - ??toiles = {stars}')
    quests()
