#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is.
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *prv = NULL;
	listint_t *temp = *head;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		temp->next = NULL;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}
	while (slow != NULL)
	{
	if (prv->n != slow->n)
	{
		return (0);
	}
	prv = prv->next;
	slow = slow->next;
	}
return (1);
}
