#include <iostream>
#include <utility>
#include <vector>

class Dumber_list {
    std::vector<int> m_list;
    public:

    Dumber_list(){
        m_list = {};
    }
    Dumber_list(std::vector<int> vec){
        m_list = vec;
    }
    void s_sort(){
        for (int i = 0; i < m_list.size();i++){
            for (int j = i; j < m_list.size();j++){
                if (m_list.at(i) < m_list.at(j)){
                    int tmp = m_list.at(i);
                    m_list.at(i) = m_list.at(j);
                    m_list.at(j) = tmp;
                }
            }
        }
    }
    void debug(){
        for (int i = 0; i < m_list.size(); i++){
            std::cout << m_list.at(i);
        }
    }
};
