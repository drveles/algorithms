#include <stdio.h>

int main() { 
	int match_count = 0, first_card_count = 0, second_card_count = 0, third_card_count  = 0;
	scanf("%d" , &match_count);
	for (int i = 0; i < match_count; i++)
	{
		scanf("%d %d %d", &first_card_count, &second_card_count, &third_card_count);
		int flag_no = 0;
		int card_max_count = first_card_count;

		if (second_card_count > first_card_count) {
			card_max_count = second_card_count;
		} 
		if (second_card_count < third_card_count){
			card_max_count = third_card_count;
		}

		if ((first_card_count == second_card_count == third_card_count) )
		{
			flag_no = 1;
		} else if ((card_max_count > (first_card_count + second_card_count + third_card_count - card_max_count))){
			flag_no = 1;
		} else if ((first_card_count == second_card_count) && (((first_card_count % 2) + (third_card_count % 2)) % 2) == 0 ) {
			flag_no = 1;
		} else if ((second_card_count == third_card_count) && ((((second_card_count % 2) + (first_card_count % 2)) % 2) == 0)) {
			flag_no = 1;
		} else if (first_card_count == third_card_count && ((((first_card_count % 2) + (second_card_count % 2))% 2) == 0)) {
			flag_no = 1;
		} 
		
		if (flag_no) {
			printf("No\n");
		} else {
			printf("Yes\n");
		}	
	}
	return 0;	
}

// cringe, not accerted, WA