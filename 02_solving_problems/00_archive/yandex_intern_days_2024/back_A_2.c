#include <stdio.h>

int main() { 
	int match_count = 0; 
	long long int first_card_count = 0, second_card_count = 0, third_card_count  = 0;
	scanf("%d" , &match_count);
	for (int i = 0; i < match_count; i++)
	{
		scanf("%d %d %d", &first_card_count, &second_card_count, &third_card_count);
		if ((first_card_count % 2 == second_card_count % 2 && first_card_count % 2 == third_card_count % 2) || 
				((first_card_count == 0 && second_card_count == 0) || 
				(second_card_count == 0 && third_card_count == 0) || 
				(first_card_count == 0 && third_card_count == 0))) {
			printf("No\n");
		} else {
			printf("Yes\n");
		}	
	}
	return 0;	
}

// accerted !