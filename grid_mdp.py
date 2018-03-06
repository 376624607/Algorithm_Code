import random
class Mdp:

    def __init__(self):
        self.states=[1,2,3,4,5,6,7,8]
        self.terminal_states=dict()
        self.terminal_states[6]=1
        self.terminal_states[7] = 1
        self.terminal_states[8] = 1

        self.actions=['n','e','s','w']

        self.rewards=dict()
        self.rewards['1_s']=-1
        self.rewards['3_s']=1
        self.rewards['5_s']=-1

        self.t=dict()
        self.t['1_s'] = 6
        self.t['1_e'] = 2
        self.t['2_w'] = 1
        self.t['2_e'] = 3
        self.t['3_s'] = 7
        self.t['3_w'] = 2
        self.t['3_e'] = 4
        self.t['4_w'] = 3
        self.t['4_e'] = 5
        self.t['5_s'] = 8
        self.t['5_w'] = 4

        self.gama=0.5

    def getstates(self):
        return self.states

    def getactions(self):
        return self.actions

    def getterminal(self):
        return self.terminal_states

    def getgama(self):
        return self.gama

    def transform(self,state,action):
        if state in self.terminal_states:
            return True,state,0
        key="%d_%s"%(state,action)
        if key in self.t:
            nextstate=self.t[key]
        else:
            nextstate=state

        is_terminal=False
        if key in self.terminal_states:
            is_terminal=True

        if key not in self.rewards:
            r=0.0
        else:
            r=self.rewards[key]

        return is_terminal,nextstate,r

    def gen_randompi_sample(self,num):
        #num 样本数
        s_sample=[]
        a_sample=[]
        r_sample=[]
        for i in range(num):
            s_temp=[]
            a_temp=[]
            r_temp=[]
            s=self.states[int(random.random()*len(self.states))]
            t=False  #用于控制是否吸收态
            while False==t:
                a=self.actions[int(random.random()*len(self.actions))]
                t,s1,r=self.transform(s,a)
                s_temp.append(s)
                a_temp.append(a)
                r_temp.append(r)
                s=s1
            s_sample.append(s_temp)
            a_sample.append(a_temp)
            r_sample.append(r_temp)

        return s_sample,a_sample,r_sample


