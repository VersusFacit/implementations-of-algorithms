#include <iostream>
#include <vector>

// in situ selection sort
std::vector<int>* selection_sort(std::vector<int>* v) {
    unsigned imin;
    int swap;

    for (unsigned i = 0; i != v->size(); ++i) {
        imin = i;
        for (unsigned j = i + 1; j != v->size(); ++j)
            if ((*v)[imin] > (*v)[j])
                imin = j;

        if (imin != i) {
            swap = (*v)[i];
            (*v)[i] = (*v)[imin];
            (*v)[imin] = swap;
        }
    }
    return v;
}

void print_vector(std::vector<int> v) {
    for (unsigned i=0; i != v.size(); ++i)
        std::cout << v[i] << ' ';
    std::cout << std::endl;
}

int main() {

    std::vector<int> v;

    int ns[] = {5,4,102,2,3,1,22,3,2,2};
    int n = 10;
    for (int k = 0; k < n; ++k) {
        v.push_back(ns[k]);
    }

    print_vector(v);
    selection_sort(&v);
    print_vector(v);

    return 0;
}
