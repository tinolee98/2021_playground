// BST.cpp
//
#include<iostream>
using namespace std;
//#include "stdafx.h"
#include "BST.h"

/*
	Implement functions defined in BST.h
*/

int main() {
	SearchTree<Entry<int, char> > *bst = new SearchTree<Entry<int, char> >();
	bst->insert(0, 'A');
	bst->insert(11, 'B');
	bst->insert(1, 'C');
	bst->insert(6, 'D');
	bst->insert(-3, 'E');
	bst->insert(-1, 'F');
	bst->insert(-10, 'G');
	cout << "insert() => ";
	for (SearchTree<Entry<int, char> >::Iterator q = bst->begin(); !(q == bst->end()); ++q) {
		cout << (*q).getKey() << " ";
	}
	cout << endl;
	cout << "isBst() => " << bst->isBst() << endl;
	cout << "size() => " << bst->size() << endl;
	cout << "find(-3) => " << (*bst->find(-3)).getValue() << endl;
	cout << "displayTree() => " << endl;
	bst->displayTree();

	cout << "erase(-3)" << endl;
	bst->erase(-3);
	cout << "size() => " << bst->size() << endl;
	cout << "find(-3) => " << (*bst->find(-3)).getValue() << endl;
	cout << "displayTree() =>" << endl;
	bst->displayTree();
	list<Entry<int, char> > lst = bst->getInterval(-1, 5);
	cout << "getInterval(-1, 5) => ";
	for (list<Entry<int, char> >::const_iterator q = lst.begin(); !(q == lst.end()); ++q) {
		cout << (*q).getKey() << " ";
	}
	cout << endl << endl;
	return 0;
}