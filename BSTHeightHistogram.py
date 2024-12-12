from itertools import permutations

class BSTHeightHistogram:


    def make_bst(self, permutation):
        bst = None
        for key in permutation:
            #print("key: ", key)
            bst = self.insert_node(bst, key)
            #print("bst: ", bst)
        return bst

    def insert_node(self, bst, key):
        if bst is None:
            return [key, None, None]
        elif key < bst[0]:
            bst[1] = self.insert_node(bst[1], key)
        else:
            bst[2]= self.insert_node(bst[2], key)
        return bst
         
                

    def get_permutations(self, n):
            n_permutations = list(permutations(range(1,n+1)))
            #print("Permutations: ", n_permutations)
            return n_permutations
                #n_permutations = list(permutations(range(1,i+1)))
                #print(n_permutations)
                # for j in range(len(n_permutations)):
                #     #print(n_permutations[j])
                #     BSTHeightHistogram.make_bst(list(n_permutations[j]))





def main():
    instance = BSTHeightHistogram()
    n = int(input("Enter a positive integer: "))
    permutations = instance.get_permutations(n)
    for permutation in permutations:
        print("permutations: ",permutation)
        bst = instance.make_bst(permutation)
        print(f"Permutation: {permutation} -> BST: {bst}")
        
        
if __name__ == "__main__":
    main()

