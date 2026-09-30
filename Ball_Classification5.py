from sklearn import tree
def main():
    print("ball classification case study")
    #encoding
    independent=[[35,"1"],[47,"1"],[90,"0"],[48,"1"],[92,"0"],[35,"1"]]
    dependent=[1,1,2,1,2,1]
    

    print("independent variables:",independent)
    testing=[[35,"1"],[35,"1"]]
    print("dependent variable:",dependent)
    training=[2,2]
if __name__=="__main__":
    main()