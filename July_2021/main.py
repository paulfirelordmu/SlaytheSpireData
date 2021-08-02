import os,json,statistics 

level = []
cards = []
score = []
removes = []
relics = []
purchuses = []
victory = 0
max_hp = []
newo = []
monsters = []
elites = []
camps = []
upgrades = []
rests = []
events = []
merchents = []
potions = []
killed_by = []
A1_damage = []
A2_damage = []
A3_damage = []
A4_damage = []
Boss_damage = []

for subdir, dirs, files in os.walk("."):
    for filename in files:
        filepath = subdir + os.sep + filename
        if ".run" in filepath:
            with open(filepath) as file:
                json_data = json.load(file)
                damage = json_data['damage_taken']
                a1_damage = 0
                a2_damage = 0
                a3_damage = 0
                a4_damage = 0
                boss_damage = 0
                for item in damage:
                    if item['floor'] <= 16.0:
                        a1_damage = a1_damage+item['damage']
                    if item['floor'] >= 18.0 and item['floor'] <=33.0 and json_data['floor_reached'] >=18.0:
                        a2_damage = a2_damage+item['damage']
                    if item['floor'] >= 34.0 and item['floor'] <=51.0 and json_data['floor_reached'] >=34.0:
                        a3_damage = a3_damage+item['damage']
                    if item['floor'] >= 52.0 and item['floor'] <=56.0 and json_data['floor_reached'] >=52.0:
                        a4_damage = a4_damage+item['damage']
                    if (item['floor'] == 16.0 or item['floor'] == 33.0 or item['floor'] == 50.0 or item['floor'] == 51.0 or item['floor'] == 56) and json_data['floor_reached'] >=52.0:
                        boss_damage = boss_damage+item['damage']
                level.append(json_data['floor_reached'])
                removes.append(len(json_data['items_purged']))
                score.append(json_data["score"])
                cards.append(len(json_data['master_deck']))
                relics.append(len(json_data['relics']))
                purchuses.append(len(json_data['items_purchased']))
                if json_data['victory'] == True:
                    victory = victory + 1                
                max_hp.append(max(json_data['max_hp_per_floor']))
                newo.append(json_data['neow_bonus'])
                monsters.append(json_data['path_per_floor'].count('M'))
                elites.append(json_data['path_per_floor'].count('E'))
                camps.append(json_data['path_per_floor'].count('R'))
                upgrades.append(json_data['campfire_upgraded'])
                rests.append(json_data['campfire_rested'])
                events.append(json_data['path_per_floor'].count('?'))
                merchents.append(json_data['path_per_floor'].count('$'))
                potions.append(len(json_data['potions_floor_spawned']))
                try:
                    killed_by.append(json_data['killed_by'])
                except:
                    killed_by.append("None")
                A1_damage.append(a1_damage)
                A2_damage.append(a2_damage)
                A3_damage.append(a3_damage)
                A4_damage.append(a4_damage)
                Boss_damage.append(boss_damage)



print("Victory count: {}".format(victory))
print("Overall runs: {}".format(len(level)))
print("Winrate: {}".format(victory/len(level)))


print("Average Floor Reached: {}".format(statistics.mean(level)))
print("Average Cards removed: {}".format(statistics.mean(removes)))    
print("Average Score: {}".format(statistics.mean(score)))
print("Average Card count: {}".format(statistics.mean(cards)))
print("Average Relic count: {}".format(statistics.mean(relics)))
print("Average Item Purchused: {}".format(statistics.mean(purchuses)))
print("Average Max HP: {}".format(statistics.mean(max_hp)))
# print("Average Neow: {}".format(json_data['neow_bonus']))
print("Average Monster fight encounters: {}".format(statistics.mean(monsters)))
print("Average Elite fight encounters: {}".format(statistics.mean(elites)))
print("Average Camp encounters: {}".format(statistics.mean(camps)))
print("Average Camp Upgrade count: {}".format(statistics.mean(upgrades)))
print("Average Camp Rest count: {}".format(statistics.mean(rests)))
print("Average Event encounters: {}".format(statistics.mean(events)))
print("Average Merchant encounters: {}".format(statistics.mean(merchents)))
print("Average Potions counts: {}".format(statistics.mean(potions)))
# print("Average Killed by: {}".format((json_data['killed_by'])))
print("Average Overall A1 Damage Taken: {}".format(statistics.mean(A1_damage)))
print("Average Overall A2 Damage Taken: {}".format(statistics.mean(A2_damage)))
print("Average Overall A3 Damage Taken: {}".format(statistics.mean(A3_damage)))
print("Average Overall A4 Damage Taken: {}".format(statistics.mean(A4_damage)))
print("Average Overall Boss Damage Taken: {}".format(statistics.mean(Boss_damage)))