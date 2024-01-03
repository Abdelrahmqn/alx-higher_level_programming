#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - checking if the next pointer cycle
 *
 * @list: the list of cycle.
 * return: return (0) iif there are no cycle, (1)if there a cycle in it.
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
	slow = slow->next;
	fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
