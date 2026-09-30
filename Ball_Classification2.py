#rough=1
#smooth=0
#tennis ball=1
#cricket ball=2
def main():
    print("ball classification case study")
    #encoding
    Fetures=[[35,"1"],[47,"1"],[90,"0"],[48,"1"],[92,"0"],[35,"1"],[35,"1"],[35,"1"]]
    Labels=[1,1,2,1,2,1,2,2]
    print("fetures:",Fetures)
    print("labels:",Labels)

if __name__=="__main__":
    main()