#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: Pointer to list to be checked.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *temp1, *temp2;

	if (!list || !list->next)
		return (0);

	temp1 = list->next;
	temp2 = temp1->next;

	while (temp1 && temp2 && temp2->next)
	{
		if (temp1 == temp2)
			return (1);

		temp1 = temp1->next;
		temp2 = temp2->next->next;
	}

	return (0);
}
