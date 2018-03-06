from grid_mdp import Mdp

class Policy_Value:
    def __init__(self,grid_mdp):
        ##价值
        self.v=[0.0 for i in range(len(grid_mdp.states)+1)]

        #self.pi[state]=策略在状态state下采取的动作
        self.pi=dict()
        for state in grid_mdp.states:
            if state in grid_mdp.terminal_states:continue
            self.pi[state]=grid_mdp.actions[0]  #初始化时，如果不是吸收态则默认向东移动

    #策略估计
    def policy_evaluate(self,grid_mdp):
        for i in range(1000):
            delta=0.0
            for state in grid_mdp.states:
                if state in grid_mdp.terminal_states:continue
                action=self.pi[state]
                t,s,r=grid_mdp.transform(state,action)
                #计算代价
                new_v=r+grid_mdp.gama*self.v[s]
                delta+=abs(new_v-self.v[state])
                self.v[state]=new_v   #价值更新????
            if delta<1.0e-6:
                break
    #策略更新
    def policy_improve(self,grid_mdp):

        for state in grid_mdp.states:
        #初始化
            a1=grid_mdp.actions[0]
            t,s,r =grid_mdp.transform(state,a1)
            v1=r+grid_mdp.gama*self.v[s]

            for action in grid_mdp.actions:
                t,s,r=grid_mdp.transform(state,action)
                v=r+grid_mdp.gama*self.v[s]
                if v1<v:
                    a1=action
                    v1=v
            self.pi[state]=a1

    def policy_iterate(self,grid_mdp):
        for i in range(1000):
            self.policy_evaluate(grid_mdp)
            self.policy_improve(grid_mdp)

    def value_iteration(self,grid_mdp):
        for i in range(1000):
            delta=0.0
            for state in grid_mdp.states:
                if state in grid_mdp.terminal_states:continue

                a1=grid_mdp.actions[0]  #随便取的
                t,s,r=grid_mdp.transform(state,a1)
                v1=r+grid_mdp.gama*self.v[s]

                for action in grid_mdp.actions:
                    t,s,r=grid_mdp.transform(state,action)
                    if v1<r+grid_mdp.gama*self.v[s]:
                        a1=action   #临时存储疑似最佳策略的行动
                        v1=r+grid_mdp.gama*self.v[s]  #临时存储疑似最佳策略值

                delta+=abs(v1-self.v[state])
                self.pi[state]=a1   #状态state最佳策略的对应的行动
                self.v[state]=v1     #最佳策略对应的奖励

            if delta<1e-6:   #价值之差在一定范围内则表示符合最佳策略要求
                break;

if __name__=='__main__':
    grid_mdp=Mdp()
    polval=Policy_Value(grid_mdp)
    # polval.policy_iterate(grid_mdp)
    polval.value_iteration(grid_mdp)
    print("strategy is:\n")
    for i in range(1,6):
        print(polval.pi[i]+'  ')