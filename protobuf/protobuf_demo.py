
from example.person_pb2 import people
# from protobuf.example.person_pb2 import people

# pbFirstPeople = people()  
# print(pbFirstPeople)
# pbFirstPeople.name = "joey"  
# pbFirstPeople.height = 160  
# print (pbFirstPeople)  
# print(pbFirstPeople.SerializeToString())

def write():
    pbPeople = people()
    pbPeople.name = "onedi"
    pbPeople.height = 180

    print(pbPeople)

    with open("mybuffer.io", "wb") as f:
        print(pbPeople.SerializeToString())
        f.write(pbPeople.SerializeToString()) 


def read():
    pbPeople = people()
    with open("mybuffer.io", "rb") as f:
        pbPeople.ParseFromString(f.read())
        print(pbPeople)



if __name__ == '__main__':
    # write()
    write()








