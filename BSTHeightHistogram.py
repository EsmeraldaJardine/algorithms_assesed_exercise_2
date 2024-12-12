from itertools import permutations

class BSTHeightHistogram:

    def make_bst(self, permutation):
        bst = None
        for key in permutation:
            bst = self.insert_node(bst, key)
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
            return n_permutations


def main():
    instance = BSTHeightHistogram()
    n = int(input("Enter a positive integer: "))
    height_count = {}
    height_total = 0
    bst_count = 0

    permutations = instance.get_permutations(n)

    for permutation in permutations:
        bst = instance.make_bst(permutation)
        height = instance.calculate_height(bst)
        if height not in height_count:
            height_count[height]= 1
        else:
            height_count[height]+=1

        height_total += height
        bst_count+=1

    average_height = height_total/bst_count

    print("\nheight   |   frequency")
    print("----------------------")
    for height in sorted(height_count.keys()):
        print(height,"       |  ", height_count[height]) #cannot get counts for heights 0 and 1??

    print(" Average height of BTSs: ", average_height)

              
if __name__ == "__main__":
    main()

