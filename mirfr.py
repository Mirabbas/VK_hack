# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:53:06 2019

@author: pitonhik
"""
import requests as re
import random
import gener
import azure
import time
true = True
false = False
def get_friends(ids):
    token = 'c1c11f20ec7f6c6969a7e013240454c3e6f4c38961cd00c11e90b6c968d0a39f777c034b10cc0e1add791'
    try:
        api = eval((re.get('https://api.vk.com/method/friends.get?user_id=' + str(ids) + '&order=hints&fields=domain,citi&count=5000&name_case=nom&access_token='+str(token)+'&v=5.92').text))
        if api['response']:
             True
        friend = []
        for i in range(len(api['response']['items'])):
            friend.append(api['response']['items'][i]['id'])
        return friend
    except:
        return 0
def user_info(ids):
     
      token = 'c1c11f20ec7f6c6969a7e013240454c3e6f4c38961cd00c11e90b6c968d0a39f777c034b10cc0e1add791'
      api = eval(re.get('https://api.vk.com/method/users.get?user_id='+ str(ids) +'&name_case=nom&fields=verified,sex,bdate,city,country,home_town,contacts,site,education,universities,schools,status,career,personal,relation&access_token='+ str(token) + '&v=5.92').text)
      #print(api)
      person_info = {}
      try:
        person_info['name'] = api['response'][0]['first_name']
      except:
          person_info['name'] = 0
      try:
        person_info['fam'] = api['response'][0]['last_name']
      except:
        person_info['fam'] =0 
      try:
       person_info['sex'] = api['response'][0]['sex']
      except:
          person_info['sex']=0
      try:
       arg = api['response'][0]['bdate'].split('.')
      except:
       arg = []
      if len(arg) ==3:
       person_info['age'] = 2019 - int(arg[2])
      else:
       person_info['age'] = 0
      try:
       person_info['citi'] = api['response'][0]['city']
      except:
       person_info['citi'] = 0
      try:
       person_info['country'] = api['response'][0]['country']
      except:
        person_info['country']=0
      try:
       person_info['university'] = api['response'][0]['university']
      except:
        person_info['university'] = 0
      try:
       person_info['career'] = api['response'][0]['career']
      except:
       person_info['career'] = 0
      try:
       person_info['personal'] = api['response'][0]['personal']
      except:
        person_info['personal'] = 0
      try:
       person_info['relation'] = api['response'][0]['relation']
      except:
       person_info['relation'] = 0
    
      return person_info
    
      #return 0  #выполнее функции завершилось с ошибкой 
def mas_m_fr():
    m = [175309344, 145809681, 206649940, 250007741, 328199506, 357141362, 33662427, 26537712, 199864051, 319175536, 313709124, 311224404, 335241105, 145936863, 268360335, 190657563, 180585214, 189612188, 316214266, 360917419, 99385128, 96029187, 144583294, 3031603, 420995125, 68764827, 271424657, 137065113, 145635012, 92635851, 548341760, 122526230, 202163818, 379209184, 152834078, 223278999, 223454521, 160343915, 136214609, 242278915, 232670426, 214606673, 178565746, 155630933, 190115099, 180764550, 192963941, 202038187, 158708618, 117140649, 104344603, 138123065, 473216147, 222258502, 532464962, 121752392, 390799222, 352197350, 493476096, 187375289, 240178704, 377597538, 382607235, 231291046, 307881072, 241655837, 448966472, 353816147, 59542558, 272920120, 23195751, 378233895, 184035604, 152251997, 159954335, 349085514, 276572222, 303555938, 345395970, 226052259, 96332740, 287123304, 5379200, 40348481, 29218869, 270207395, 346680504, 155279549, 124214006, 12773328, 76198994, 73297393, 210316284, 143080108, 137185395, 102387406, 135351968, 86880701, 51234677, 83901303, 553491, 134084141, 25085112, 150499323, 203700256, 532395080, 56489859, 121545456, 36472615, 50737522, 24209739, 221401857, 151283935, 55565453, 199094932, 109773439, 276853426, 141940739, 426521150, 54100626, 98841974, 25547874, 19488811, 142786759, 76062503, 43750767, 137738900, 153154335, 42623971, 11301292, 18871693, 81968055, 74976058, 52223700, 97259694, 45154260, 251241403, 119706122, 44799073, 50884710, 83463622, 59473203, 90946416, 392452534, 39374684, 96159031, 281553758, 23762493, 29537985, 62955530, 33797744, 28583833, 79700317, 96729361, 2622997, 55482091, 21794274, 20743645, 110401827, 68588626, 138621470, 182381680, 135745075, 47058890, 54342571, 32076925, 51990165, 103551706, 66796613, 83773349, 118164522, 165454106, 54547367, 123902986, 128625439, 31991904, 134885930, 221421371, 21441425, 114716588, 63546198, 82172660, 139699319, 246561334, 25955714, 20495423, 356901968, 54691791, 55952297, 148404482, 170544665, 29093721, 42093136, 245470, 161068223, 22118554, 30817021, 150456704, 198080603, 30612805, 123855128, 132888438, 35799362, 145762347, 156799886, 93831654, 13808, 180562171, 74950195, 71121465, 137780361, 136512725, 115181551, 66895582, 460492101, 26519287, 154012470, 275601567, 70936303, 36479409, 206305837, 121933846, 5050525, 88404949, 294277536, 69533082, 95238607, 55856272, 181218081, 46289294, 35472542, 359818502, 95120258, 228900589, 316972460, 167458120, 247553450, 183236685, 134782009, 33924650, 98606778, 41061904, 125317402, 2783884, 125030435, 303368061, 224227312, 97528302, 25509489, 11496743, 151034963, 83730610, 69648377, 293454159, 150989074, 54852680, 151500561, 139933419, 205935959, 67913661, 126758382, 182511727, 261365795, 12226041, 291559798, 5021850, 32723336, 222866407, 178588580, 56775362, 29659992, 315293552, 182104535, 2295315, 186062804, 69488073, 209669111, 429689288, 185628912, 52802682, 155739874, 3886175, 387077147, 16471743, 36880485, 20485849, 146006487, 29299390, 44144085, 362483421, 167428620, 78327902, 298462914, 54235876, 366220662, 101596284, 12919340, 174431466, 132360259, 112814360]
    return m
class client:
    def kred(self,suma):
        value = []
        value.append(self.name)
        value.append(self.fam)
        value.append(self.gender)
        value.append(self.age)
        value.append(self.university)
        value.append(0)
        value.append(0)
        value.append(0)
        value.append(0)
        
        try:
            a  = self.country['id']
        except:
            a = 0
        value.append(a)
        
        while len(value) < 18:
            value.append(0)
        kred = azure.get_reit(value)
        self.k = kred
        #return kred
    def __init__(self,id_vk):
      
      api = user_info(id_vk)
      time.sleep(0.34)
      #print(api)
      if api !=0:
       self.id_vk = id_vk
       self.name = api['name']
       self.fam = api['fam']
       self.gender = api['sex']
       self.age = api['age']
       self.citi = api['citi']
       self.country = api['country']
       self.university = api['university']
       self.career = api['career']
       self.personal = api['personal']
       self.relation= api['relation']
       self.friends = get_friends(id_vk)
       #self.best_fr = self.friends[:10]
       self.trade = gener.purchase_history_generator(gener.name_generator(1))
       self.ClassInit = True
       self.k = 0
      else:
       self.id_vk = id_vk
       self.name = 0
       self.surname = 0
       self.gender = 0
       self.age = 0
       self.citi = 0
       self.country = 0
       self.university = 0
       self.career = 0
       self.personal = 0
       self.relation= 0
       self.ClassInit = False
       self.k = 0
