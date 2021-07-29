#pragma once
#include<list>
class RuntimeException { // generic run-time exception
private:
	string errorMsg;
public:
	RuntimeException(const string& err) { errorMsg = err; }
	string getMessage() const { return errorMsg; }
};

// Exception thrown on performing top or pop of an empty stack.
class NonexistentElement : public RuntimeException {
public:
	NonexistentElement(const string& err) : RuntimeException(err) {}
};

template <class T>
class BinaryTree {
private:
	class Node { // a node of the tree
	public:
		T value; // element value
		Node *par, *left, *right; // parent, left child, right child

		Node() : par(NULL), left(NULL), right(NULL) { } // constructor
		Node(T val) { // constructor
			value = val;
			par = left = right = NULL;
		}
		Node(T val, Node parent, Node left, Node right) { // constructor
			this->value = val;
			this->par = parent;
			this->left = left;
			this->right = right;
		}
	};
public:
	class Position { // position in the tree
	private:
		Node *val; // pointer to the node
	public:
		Position(Node *v = NULL) : val(v) { } // constructor
		T& operator*(); // get element
		bool operator==(const Position& p) const; // are iterators equal?
		Position getLeft() const; // get left child
		Position getRight() const; // get right child
		Position getParent() const; // get parent
		bool isRoot() const; // root of the tree?
		bool isExternal() const; // an external node?
		friend class BinaryTree; // give tree access
	};
	typedef std::list<Position> PositionList; // list of positions

	BinaryTree<T>() : root(NULL), n(0) {}   // BinaryTree constructor

private:
	Node *root;
	int n;			// number of nodes
public:
	int size() const; // number of nodes
	bool empty() const; // is tree empty?
	Position getRoot() const; // get the root
	void addRoot(); // add root to empty tree
	// expand external node
	void expandExternal(const Position& p); 
	// remove p and parent
	Position removeAboveExternal(const Position& p);
	// list of all nodes
	PositionList positions() const;
	// preorder traversal
	void preorder(Node *v, PositionList& pl) const;
};

template <typename K, typename V>
class Entry { // a (key, value) pair
public: // public types
	typedef K Key; // key type
	typedef V Value; // value type
public: // public functions
	Entry(const K& k = K(), const V& v = V()) // constructor
		: key(k), value(v) { }
	const K& getKey() const { return key; } // get key (read only)
	const V& getValue() const { return value; } // get value (read only)
	void setKey(const K& k) { key = k; } // set key
	void setValue(const V& v) { value = v; } // set value
private: // private data
	K key; // key
	V value; // value
};

template <typename E>
class SearchTree { // a binary search tree
public: // public types
	typedef typename E::Key K; // a key
	typedef typename E::Value V; // a value
	class Iterator; // an iterator/position
public: // public functions
	SearchTree() // constructor
		: T(), n(0)
	{
		T.addRoot(); T.expandExternal(T.getRoot());
	} // create the super root

	int size() const;  // number of entries
	bool empty() const; // is the tree empty?
	Iterator find(const K& k); // find entry with key k
	Iterator insert(const K& k, const V& x); // insert (k,x)

	void erase(const K& k) throw(NonexistentElement); // remove key k entry
	void erase(const Iterator& p); // remove entry at p
	Iterator begin() {
		TPos v = root();
		while (v.isInternal()) v = v.left();
		return Iterator(v.parent());
		} // iterator to first entry
	Iterator end() {return Iterator(T.getRoot());} // iterator to end entry
  
	// PROBLEM 3 (b)
	void displayTree();
	// PROBLEM 3 (c)
	bool isBst();   
	// PROBLEM 3 (d)
	list<E> getInterval(const K& min, const K& max);

protected: // local utilities
	typedef BinaryTree<E> BTree; // linked binary tree
	typedef typename BTree::Position TPos; // position in the tree

	TPos root() const
	{  return T.getRoot().left();  } // get virtual root
	TPos finder(const K& k, TPos v); // find utility
	TPos inserter(const K& k, const V& x); // insert utility
	TPos eraser(TPos& v); // erase utility
private: // member data
	BTree T; // the binary tree
	int n; // number of entries
public:
	// Iterator class declaration
	class Iterator { // an iterator/position
	private:
		TPos v; // which entry
	public:
		Iterator(const TPos& vv) : v(vv) { } // constructor
		const E& operator*() const; // get entry (read only)
		E& operator*(); // get entry (read/write)
		bool operator==(const Iterator& p) const; // are iterators equal?
		Iterator& operator++(); // inorder successor
		friend class SearchTree; // give search tree access
	};
};
