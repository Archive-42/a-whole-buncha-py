"""
We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root
Example 1:
	    1
	  /   \
	2	    5
  /	  \    /  \
3	   4  6	   7



Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:
	   	   1
	     /   \
       2	  5
     /	     /    
   3	    6	   
 /         /
4		  7

Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
 

Example 3:



Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]
 

Note:

The number of nodes in the original tree is between 1 and 1000. 
Each node will have a value between 1 and 10^9.
"""


class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import defaultdict

        dp = defaultdict(int)
        # print dp
        for index_i in range(len(A)):
            for index_j in range(index_i):
                diff = A[index_i] - A[index_j]
                dp[(index_i, diff)] = max(dp[(index_i, diff)], dp[(index_j, diff)] + 1)
                # print dp
        return max(dp.itervalues()) + 1
