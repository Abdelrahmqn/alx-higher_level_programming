#include "lists.h"
/**
 * insert_node - inserts a number into a sortd singly linked lists.
 * @head: the head of the list.
 *
 * @number: the number that will be added.
 *
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (temp->next != NULL && temp->next->n < number)
	{
		temp = temp->next;
	}
	new->next = temp->next;
	temp->next = new;
	return (new);
}
