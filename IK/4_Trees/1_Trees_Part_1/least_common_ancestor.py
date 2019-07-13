'''
Least Common Ancestor (LCA)
Problem Statement
You are given root of a binary tree T of n nodes. You are also given references of two nodes a & b. You need to find the
 lowest common ancestor of a and b. Least or lowest common ancestor (LCA) of two nodes is defined as the lowest node in
 T that has the two nodes as descendants. For this problem, we allow a node to be an ancestor/descendant of itself.
Wikipedia defines LCA as follows:
The LCA of a and b in T is the shared ancestor of a and b that is located farthest from the root. Computation of lowest
 common ancestors may be useful, for instance, as part of a procedure for determining the distance between pairs of nodes
 in a tree: the distance from a to b can be computed as the distance from the root to a, plus the distance from the root
 to b, minus twice the distance from the root to their lowest common ancestor.
Input/Output Format For The Function:
Input Format:
There are three arguments in input: root, a, b.
Structure of tree node is as follows:
class Node {
public:
int data;
Node *left;
Node *right;
};
Output Format:
Return the integer value from the LCA of a and b.
Input/Output Format For The Custom Input:
Input Format:
The first line contains three space separated integers n, the value of node a, and the value of node b.
Next n - 1 lines contain two space separated integers denoting an edge. The first value is the value of from node, and the
 second value is the value of the to node.
Output Format:
The integer value from the LCA of a and b will be printed.
Constraints:
1 <= n <= 100000
1 <= Value at a <= n
1 <= Value at b <= n
Value stored at any node will be between 1 and n and unique.

Sample Test Case:
Sample Input:
Let us assume this is the tree, you are given pointers to 1(the root), and two nodes: 8, 9.
Sample Output:
5
Explanation:
There are three shared parents of 8 and 9 in this tree: 5, 2, 1. Of those three, the farthest from the root is 5.
More examples,
LCA(2,5) = 2
LCA(2,3) = 1
'''
import sys

sys.setrecursionlimit(101000)

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    if node == None:
        return None
    preorder(node.left)
    preorder(node.right)

#class Node(object):
#    def __init__(self, data, left=None, right=None):
#        self.data = data
#        self.left = left
#        self.right = right


def lca(root, a, b):
    #Write your code here
    pass


numbers = [int(n) for n in input().split()]
n=numbers[0]
a=numbers[1]
b=numbers[2]

i=0
xx=[]
while i<=n:
    xx.insert(i,Node(i,None,None))
    i+=1;
i=1
while i<n:
    num = [int(n) for n in input().split()]
    st=num[0]
    en=num[1]
    if xx[st].left==None:
        xx[st].left=xx[en]
    else:
        xx[st].right=xx[en]
    i+=1

print(lca(xx[1], xx[a], xx[b]))


'''
BRUTE FORCE
#include<bits/stdc++.h>
using namespace std ;

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

void parse_input( vector< pair< int , int > >&edges, struct Node * arr_stub[] )
{
    for(int i=0;i<edges.size();i++)
    {
        int from = edges[i].first ;
        int to = edges[i].second ;
        if( (arr_stub[from]->left) == NULL )
            arr_stub[from]->left = arr_stub[to] ;
        else
            arr_stub[from]->right = arr_stub[to] ;
    }
}
void pre_order(Node * head)
{
    if( head == NULL )
        return ;
    pre_order(head->left) ;
    pre_order(head->right);
}

/* you only have to complete the function given below.  
Node is defined as  

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

*/
// ==================================== START ==================================
void dfs(Node * head, int parent , int * level ,int * par)
{
    if(head==NULL)
        return ;
    par[ head->data ] = parent ;
    level[ head->data ] = level[ parent ] + 1 ;
    dfs( head -> left , head->data ,level,par ) ;
    dfs( head -> right , head->data,level,par ) ;
}
bool isAncestor( int node, int a, int * par )
{
	// go up till root with the help of parent arr_stubay we precomputed !! 
	while(a!=0)
	{
		if(node==a)
			return true ;
		a = par[a] ;
	}
	return false ;
}	
  // initialize with minimum so that we can maximize it
                                                                                                    
void traverse_and_update(
    Node * head , int a, int b , int * level, int * par,int &answer_node, int &level_of_answer
){
	if( head == NULL )
		return ;
	int current_node = head->data ;
    if( isAncestor( current_node , a , par ) && isAncestor(current_node , b, par) )
	{
		if( level[ current_node ] > level_of_answer )  // maximize the level of common ancestor!! 
		{
			answer_node = current_node ;
			level_of_answer = level[ current_node ] ; 
		}
	}
	// recursively traverse and update the current global answer !! 
	traverse_and_update(head->left,a,b,level,par,answer_node,level_of_answer) ;
	traverse_and_update(head->right,a,b,level,par,answer_node,level_of_answer) ;
	
}
int lca( Node * head , Node * a, Node  * b )
{
    int par[100020],level[100020]={0},i;
    dfs(head , 0 , level, par ) ; // store parents & level .. preprocessing part!! 
    // according to the definition of LCA, it should be a ancestor with maximum level
    // we will check both the conditions for every node, and update the answer accordingly!! 
    // calculate answer again a new dfs 
    int aa = a -> data ;
    int bb = b -> data ;
    int answer_node, level_of_answer=0;
    traverse_and_update( head ,aa ,bb, level,par,answer_node,level_of_answer);
    return answer_node;
}
// ==================================== END ==================================

int main()
{
    int i , n, a, b;
    vector< pair< int , int > >edges ;
    cin >> n >> a >> b ;
    struct Node * arr_stub[100020] ;
    for(i=1;i<=n;i++)
        arr_stub[i] = new Node(i) ;
    for(i=1;i<n;i++)
    {
        int st,en ;
        cin >> st >> en ;
        edges.push_back(make_pair( st,en )) ;
    }

    parse_input( edges, arr_stub );
    
    pre_order( arr_stub[1] ) ;
    int answer = lca( arr_stub[1] , arr_stub[a] , arr_stub[b] ) ;    
    // we passed the head pointer basically which is arr_stub[1]
    cout<<answer<<endl;
    return 0;
}

'''
'''
OPTIMAL SOLUTION 1
#include<bits/stdc++.h>
using namespace std ;

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

void parse_input( vector< pair< int , int > >&edges, struct Node * arr_stub[])
{
    for(int i=0;i<edges.size();i++)
    {
        int from = edges[i].first ;
        int to = edges[i].second ;
        if( (arr_stub[from]->left) == NULL )
            arr_stub[from]->left = arr_stub[to] ;
        else
            arr_stub[from]->right = arr_stub[to] ;
    }
}
void pre_order(Node * head)
{
    if( head == NULL )
        return ;
    pre_order(head->left) ;
    pre_order(head->right);
}

/* you only have to complete the function given below.  
Node is defined as  

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};
                                                                                                                                                                                                                              
*/
// ==================================== START ==================================
void dfs(Node * head, int parent , int * par)  //PRECOMPUTATION OF PARENT
{
    if(head==NULL)
        return ;
    par[ head->data ] = parent ;
    dfs( head -> left , head->data ,par) ;
    dfs( head -> right , head->data,par ) ;
}
vector< int >get_path( int *par ,int node )    // FUNCTION TO GET THE PATH FROM ROOT
{
    vector< int >path ;     
    while( par[node]!=-1 ) // we do have the parent array now, so going up till the room comes
    { 
        path.push_back( node ) ;  // storing it in a vector 
        node = par[node];
    }
    path.push_back(node) ;     // root left so added explicitly     
    return path ;
}
int lca( Node * head , Node * a, Node * b )
{
    int par[100020],i;
    int aa = a -> data , bb = b->data ;
    dfs(head , -1 , par ) ; // store parents
    vector< int > path_of_a = get_path( par, aa ) ; // got the paths
    vector< int > path_of_b = get_path( par, bb ) ;
    
    reverse(path_of_a.begin(),path_of_a.end()) ; // REVERSED BECAUSE WE GOT REVERSE PATH
    reverse(path_of_b.begin(),path_of_b.end()) ;
    for(i=0;i<path_of_a.size() && i < path_of_b.size();i++)
    {
        if( path_of_a[i] != path_of_b[i] )      // LAST MATCH WAS THE ANSWER 
            return path_of_a[i-1];
    }
    return path_of_a[i-1];   // returned the last match 
}

// ==================================== END ==================================
int main()
{
    int i , n, a, b;
    vector< pair< int , int > >edges ;
    cin >> n >> a >> b ;
    struct Node * arr_stub[100020] ;
    
    for(i=1;i<=n;i++)
        arr_stub[i] = new Node(i) ;
    for(i=1;i<n;i++)
    {
        int st,en ;
        cin >> st >> en ;
        edges.push_back(make_pair( st,en )) ;
    }
    parse_input( edges , arr_stub);
    int answer = lca( arr_stub[1] , arr_stub[a] , arr_stub[b] ) ;
             // we passed the head pointer basically which is arr_stub[1]
    cout<<answer<<endl;
    return 0;
}
'''
'''
OPTMIAL SOLUTION 2
#include<bits/stdc++.h>
using namespace std ;

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

void parse_input( vector< pair< int , int > >&edges, struct Node * arr_stub[] )
{
    for(int i=0;i<edges.size();i++)
    {
        int from = edges[i].first ;
        int to = edges[i].second ;
        if( (arr_stub[from]->left) == NULL )
            arr_stub[from]->left = arr_stub[to] ;
        else
            arr_stub[from]->right = arr_stub[to] ;
    }
}
void pre_order(Node * head)
{
    if( head == NULL )
        return ;
    pre_order(head->left) ;
    pre_order(head->right);
}

/* you only have to complete the function given below.
Node is defined as

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

*/

// ==================================== START ==================================

#define infinity 10002020
void dfs(Node * head, int current_level, int * level, int * first_occurrence, int * euler, int & counter)
{
    if( head == NULL )
        return ;
    int current_node = head->data ;
    euler[counter] = current_node ;     // making up the Euler tour array
    level[ current_node ] = current_level ; // storing level as well
    if( first_occurrence[ current_node ] == -1 )    // storing first occurrence too
        first_occurrence[ current_node ] = counter ;
    counter++;
    dfs( head->left, current_level+1, level, first_occurrence, euler, counter) ;
    if( head->left != NULL )
        euler[ counter++ ] = current_node ;
    dfs( head->right, current_level+1, level, first_occurrence, euler, counter) ;
    if( head->right != NULL )
        euler[ counter++ ] = current_node ;

}

int lca( Node * head , Node * a, Node * b )
{
    int euler[200020] ,level[100020] , first_occurrence[100020];
    // size of euler array will be twice in size !!
    memset( first_occurrence,-1,sizeof first_occurrence );    // initialize all the first occurrence with -1
    int counter = 1 ;  // counter for creating euler tour array
    dfs( head , 1 ,level, first_occurrence, euler,counter);  // PRECOMPUTES euler, level, and first_occurrence
    int aa = a->data ;
    int bb = b->data ;
    int first_occurrence_aa = first_occurrence[aa] ;
    int first_occurrence_bb = first_occurrence[bb] ;
    int mini = min(first_occurrence_aa,first_occurrence_bb),
        maxi = max(first_occurrence_bb,first_occurrence_aa) ;
    int var = infinity,answer;
    for( int i = mini ; i<= maxi ;i++ )   // just a range minimum query
    {
        if( var > level[ euler[i] ] )
        {
            answer = euler[i] ;
            var = level[ euler[i] ] ;
        }
    }
    return answer;
    // We can also use some data-structure to calculate RMQ more efficiently,
    // see https://en.wikipedia.org/wiki/Range_minimum_query and elsewhere.
}

// ==================================== END ==================================
int main()
{
    int i , n, a, b;
    vector< pair< int , int > >edges ;
    cin >> n >> a >> b ;
    struct Node * arr_stub[100020] ;
    for(i=1;i<=n;i++)
        arr_stub[i] = new Node(i) ;
    for(i=1;i<n;i++)
    {
        int st,en ;
        cin >> st >> en ;
        edges.push_back(make_pair( st,en )) ;
    }

    parse_input( edges, arr_stub );
    int answer = lca( arr_stub[1] , arr_stub[a] , arr_stub[b] ) ;
    // we passed the head pointer basically which is arr_stub[1]
    cout<<answer<<endl;
    return 0;
}
'''
