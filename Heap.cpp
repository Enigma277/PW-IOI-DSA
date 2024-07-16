#include<bits/stdc++.h>
using namespace std;
class Heap {
public:
    vector<int> a;
    int sz = 0;

    int parent(int x) {
        return (x-1)/2;
    }

    int leftChild(int x) {
        return 2*x+1;
    }
    int rightChild(int x) {
        return 2*x+2;
    }

    void push(int val){
        int ind = sz;
        cout<<"pushing at at index = "<<ind<<endl;
        a.push_back(val);
        sz++;
        while(ind != 0) {
            if(a[ind] > a[parent(ind)]) {
                cout<<"swapping it with parent = "<<parent(ind)<<endl;
                swap(a[ind], a[parent(ind)]);
                ind = parent(ind);
            } else {
                break;
            }
        }
    }


    int top() {
        if(isEmpty()) {
            return INT_MIN;
        }
        return a[0];
    }

    void pop() {
        a[0] = a[sz-1];
        sz--;
        a.pop_back();
        int ind = 0; 
        while(true){
            int cur = a[ind];
            int lc = leftChild(ind) < sz ? a[leftChild(ind)] : INT_MIN;
            int rc = rightChild(ind) < sz ? a[rightChild(ind)] : INT_MIN;

            int maximum = max({cur, lc, rc});

            if(maximum == cur) break;
            if (maximum == lc){
                cout<<"swapping it with leftChild = "<<leftChild(ind)<<endl;
                swap(a[ind],  a[leftChild(ind)]);
                ind = leftChild(ind);
            } else {
                cout<<"swapping it with rightChild = "<<rightChild(ind)<<endl;
                swap(a[ind], a[rightChild(ind)]);
                ind = rightChild(ind);
            }
        }
    }

    bool isEmpty() {
        return size() == 0;
    }

    int size() {
        return sz;
    }

    void display() {
        for(int x: a) {
            cout<<x<<" -- ";
        }
        cout<<endl;
    }

}heap;

signed main(){
    heap.push(100);
    heap.display();
    heap.push(20);
    heap.display();
    heap.push(35);
    heap.display();
    heap.push(50);
    heap.display();
    heap.push(200);
    heap.display();
    heap.pop();
    heap.display();
    
}