#include <iostream>
#include <cmath>

int main() {
    int vasya_p_tree, vasya_range, masha_q_tree, masha_range ;
        
    std::cin >> vasya_p_tree >> vasya_range >> masha_q_tree >> masha_range;
    
    int min_vasya = vasya_p_tree - vasya_range;
    int max_vasya = vasya_p_tree + vasya_range;
    int min_masha = masha_q_tree - masha_range;
    int max_masha = masha_q_tree + masha_range;
    
    if (vasya_p_tree == masha_q_tree) {
        std::cout << ((vasya_range >= masha_range) ? (vasya_range * 2  + 1) : (masha_range * 2 + 1)) << std::endl;
    } else if ((max_vasya < min_masha && min_vasya < max_masha) || (max_masha < min_vasya && min_masha < max_vasya)) {
        std::cout << (vasya_range * 2) + (masha_range * 2) + 2 << std::endl;
    }else{
        std::cout << (abs(min_vasya < min_masha ? min_vasya : min_masha) + abs(max_vasya > max_masha ? max_vasya : max_masha) + 1) << std::endl;
    }
    
    return 0;
}

// ОК