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
    
    def calculate_height(self,bst):
        if bst is None or (bst[1] is None and bst[2] is None):
            return 0

        l_subtree_height = self.calculate_height(bst[1])
        r_subtree_height = self.calculate_height(bst[2])
        return 1+ max(l_subtree_height,r_subtree_height)

            
         
                

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
    height_count = {}
    height_total = 0
    bst_count = 0
    for permutation in permutations:
        print("permutations: ",permutation)
        bst = instance.make_bst(permutation)
        print(f"Permutation: {permutation} -> BST: {bst}")
        height = instance.calculate_height(bst)
        print("height: ", height)
        if height not in height_count:
            height_count[height]= 0
        else:
            height_count[height]+=1

        height_total += height
        bst_count+=1
    average_height = height_total/bst_count
    print("height   |   frequency")
    print("_______________________")
    for height in sorted(height_count.keys()):
        print(height,"       |  ", height_count[height]) #values are off by 1?

    print(" Average height of BTSs: ", average_height)

        
    
    
        
        
if __name__ == "__main__":
    main()

