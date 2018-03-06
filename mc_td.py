import  grid_mdp
import random

grid=grid_mdp.Mdp()
states=grid.getstates()
actions=grid.getactions()
gama=grid.getgama()


#蒙特卡洛模拟方法
def mc(gama,state_sample,action_sample,reward_sample):
    vfunc=dict()   #存储每个状态的价值
    nfunc=dict()    #存储每个sample中各状态出现的次数

    for s in states:
        vfunc[s]=0.0
        nfunc[s]=0.0

    for iter1 in range(len(state_sample)):
        G=0.0
        #对每个样本逆序累加价值和
        for step in range(len(state_sample[iter1])-1,-1,-1):
            G*=gama      #此即为V[S]
            G+=reward_sample[iter1][step]

        for step in range(len(state_sample[iter1])):
            s=state_sample[iter1][step]
            vfunc[s]=vfunc[s]+G
            G-=reward_sample[iter1][step]
            G/=gama
            nfunc[s]+=1.0

    for s in states:
        if nfunc[s]>0.001:#表示s状态至少出现一次的话即参与求平均代价
            vfunc[s]/=nfunc[s]
    print("mc")
    print(vfunc)
    return vfunc

#时差学习方法(temperal difference)
def td(alpha,gama,state_sample,action_sample,reward_sample):
    vfunc=dict()
    for s in states:
        vfunc[s]=0.0

    for iter1 in range(len(state_sample)):
        for step in range(len(state_sample[iter1])):
            s=state_sample[iter1][step]
            r=reward_sample[iter1][step]

            if step+1<len(state_sample[iter1]):
                s1=state_sample[iter1][step+1]
                next_v=vfunc[s1]
            else:
                next_v=0.0

            vfunc[s]+=alpha*(r+gama*next_v-vfunc[s])
    print("td")
    print(vfunc)
    return vfunc

#随机生成的样本形式
# s = [[1,2,3],[4,3]]
# a = [['e','e','s'],['w','s']]
# r = [[0,0,1],[0,1]]

if __name__=="__main__":
    alpha=0.15
    s,a,r=grid.gen_randompi_sample(100)
    mc(gama,s,a,r)
    td(alpha,gama,s,a,r)
