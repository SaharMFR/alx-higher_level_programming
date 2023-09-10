#include "lists.h"

/**
 * reverse_list - Reverses a singly linked list.
 * @head: pointer to head of list.
 */
void reverse_list(listint_t **head)
{
	listint_t *before = NULL, *after = NULL;
	listint_t *node = *head;

	while (node)
	{
		after = node->next;
		node->next = before;
		before = node;
		node = after;
	}
	*head = before;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: pointer to head of list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *firstHalf = *head, *secondHalf = NULL;

	if (!(*head) || !((*head)->next))
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			secondHalf = slow->next;
			break;
		}
		if (!(fast->next))
		{
			secondHalf = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_list(&secondHalf);

	while (firstHalf && secondHalf)
	{
		if (firstHalf->n != secondHalf->n)
			return (0);
		firstHalf = firstHalf->next;
		secondHalf = secondHalf->next;
	}

	if (!secondHalf)
		return (1);
	return (0);
}
