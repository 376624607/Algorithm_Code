class Mdp:

    def __init__(self):
        #状态空间及吸收态标记
        self.states=[1,2,3,4,5,6,7,8]
        self.terminal_states=dict()
        self.terminal_states['6'] = 1
        self.terminal_states['7'] = 1
        self.terminal_states['8'] = 1
        #行动集合
        self.actions=['e','s','w','n']
        #计数奖励
        self.rewards=dict()
        self.rewards['1_s']=-1
        self.rewards['3_s']=1
        self.rewards['5_s']=-1
        #转移状态
        self.t=dict()
        self.t['1_s']=6
        self.t['1_e']=2
        self.t['2_w']=1
        self.t['2_e']=3
        self.t['3_w']=2
        self.t['3_s']=7
        self.t['3_e']=4
        self.t['4_w']=3
        self.t['4_e']=5
        self.t['5_w']=4
        self.t['5_s']=8
        #γ衰减因子
        self.gama=0.8

    def transform(self,state,action):
        if state in self.terminal_states:
            return True,state,0

        key='{}_{}'.format(str(state),action)
        if key in self.t:
            nextstate=self.t[key]
        else:
            nextstate=state  #碰到墙壁时因为self.t中未定义下次转换状态，故一直碰壁

        #判断是否为吸收态
        is_terminal=False
        if nextstate in self.terminal_states:
            is_terminal=True
        #判断key是否属于rewards非零的操作
        if key in self.rewards:
            r=self.rewards[key]
        else:
            r=0.0

        return is_terminal,nextstate,r