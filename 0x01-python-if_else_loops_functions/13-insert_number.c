#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: pointer to head of the list.
 * @number: the number to be inserted.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *node;

	temp = *head;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;

	if (!temp || temp->n > number)
	{
		node->next = temp;
		*head = node;
		return (node);
	}

	while (temp->next && temp->n <= number)
		temp = temp->next;

	node->next = temp->next;
	temp->next = node;

	return (node);
}
